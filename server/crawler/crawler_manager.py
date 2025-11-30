import datetime
import json
import logging
import random
import time
import requests

from apscheduler.schedulers.background import BackgroundScheduler

from model.model import IvdCrawlerList
from utils import utils, const
from utils.db_client import get_db_client
from utils.network_utils import get_current_host


class CrawlerManager(object):
    schedule = BackgroundScheduler()

    def register(self) -> None:
        try:
            owner_host = get_current_host()
            register_rand = utils.get_register_rand()
            url = f"{utils.get_task_manager_register_url()}?ip={owner_host}&rand={register_rand}"
            response = requests.get(url, timeout=const.REQUEST_TIME_OUT)
            json_resp = json.loads(response.text)
            if json_resp['code'] != 0:
                logging.error(f"register crawler return error ,json_resp:{json_resp}")
            else:
                crawler_hash = json_resp['data']['crawler_hash']

        except Exception as ex:
            logging.error(f"register crawler get exception, exception: {ex}")

    def _clean_crawler(self):
        with get_db_client() as db:
            db.query(IvdCrawlerList) \
                .delete()
            db.commit()

    def start(self):
        rand_sleep_sec = random.randint(5, 15)
        self.schedule.add_job(self.register, trigger='cron', second=f"*/{rand_sleep_sec}")
        self.schedule.start()
        while True:
            now = datetime.datetime.now()
            self._handle_task()
            time.sleep(rand_sleep_sec)
            pass

    def _handle_task(self) -> bool:
        return True

    def stop(self):
        self._clean_crawler()


crawler_manager = CrawlerManager()
