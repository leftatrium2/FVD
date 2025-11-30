import logging
from datetime import datetime

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import and_

from model.model import FvdTaskList, FvdTaskQueue
from task import task_const
from utils import const
from utils.db_client import get_db_client

g_executors = {
    'default': ThreadPoolExecutor(const.TASKMANAGER_MAX_THREADS)
}
g_job_defaults = {
    'coalesce': True,
    'max_instances': 1
}
g_schedule = BackgroundScheduler(job_defaults=g_job_defaults, executors=g_executors)


# task manager for video crawler
# 将当前的单次或者批量任务，放到 task_queue 表中
class TaskManager(object):
    def parse_crontab_str(crontab: str) -> bool or list:
        crontab_split = crontab.split(' ')
        if len(crontab_split) != 6:
            return False
        return crontab_split

    # 从队列中获取一个task
    # 1. 先从Queue中获取
    # 2. 并更新此记录
    def get_task(self) -> dict or None:
        with get_db_client() as db:
            with db.begin():
                res = db.query(FvdTaskQueue) \
                    .filter(FvdTaskQueue.is_deleted == 0, FvdTaskQueue.status == task_const.TASK_STATUS_QUEUE) \
                    .order_by(FvdTaskQueue.create_time.desc()) \
                    .with_for_update() \
                    .first()
                if res:
                    db.query(FvdTaskQueue) \
                        .filter(FvdTaskQueue.id == res.id) \
                        .update({FvdTaskQueue.status: task_const.TASK_STATUS_RUNNING})
                    task = {'task_id': res.task_id, 'url': res.url}
                    return task
        return None

    # 批量任务的时候：
    # 1. 将任务信息读出来
    # 2. 解析url，并获取url中视频的信息
    # 3. 将获取的信息，插入到queue表中，以便后面的爬虫爬取
    def add_batch_task(self, task: FvdTaskList):
        if not task:
            logging.error(f"the task is None!")
            return False
        if task.task_execution_mode != task_const.TASK_EXECUTION_BATCH_MODE:
            logging.error(f"the task id:{task.task_id} execution_mode is not TASK_EXECUTION_BATCH_MODE")
            return False

        return True

    # 添加一个task
    # 简单任务，立即执行类型，单独的URL
    def add_simple_task(self, task: FvdTaskList):
        if not task:
            return False
        if task.task_execution_mode != task_const.TASK_EXECUTION_EXECUTE_MODE:
            logging.error(f"the task id:{task.task_id} execution_mode is not TASK_EXECUTION_EXECUTE_MODE")
            return False
        task_queue_item = FvdTaskQueue()
        task_queue_item.task_id = task.task_id
        task_queue_item.create_time = datetime.now()
        task_queue_item.url = task.task_url
        task_queue_item.status = task_const.TASK_STATUS_QUEUE
        with get_db_client() as db:
            db.add(task_queue_item)
            db.commit()
            return True

    def _query_scheduled_task(self) -> list:
        with get_db_client() as db:
            res_list = db.query(FvdTaskList) \
                .filter(
                and_(FvdTaskList.is_deleted == 0,
                     FvdTaskList.task_execution_mode == task_const.TASK_EXECUTION_BATCH_MODE)) \
                .all()
            return res_list

    def start(self):
        from task.apscheduler_listener import my_listener
        logging.getLogger('apscheduler.executors.default').setLevel(logging.ERROR)
        g_schedule.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
        task_list = self._query_scheduled_task()
        for task in task_list:
            if not self.add_batch_task(task):
                logging.error(f"add task error, task: {task}")
        if not g_schedule.running:
            g_schedule.start()

    def stop(self):
        if g_schedule.running:
            g_schedule.shutdown()


g_task_manager = TaskManager()
