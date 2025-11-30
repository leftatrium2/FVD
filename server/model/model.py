# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IvdCrawlerList(Base):
    __tablename__ = 'ivd_crawler_list'

    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"))
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    crawler_name = Column(String(200, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='爬虫名字')
    crawler_host = Column(String(200, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='爬虫所在的IP地址')
    crawler_hash = Column(String(200, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='爬虫唯一序列号')
    crawler_status = Column(Integer, nullable=False, server_default=text("'0'"), comment='爬虫状态')


class IvdMaterial(Base):
    __tablename__ = 'ivd_material'

    id = Column(Integer, primary_key=True)
    title = Column(String(200, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='标题')
    description = Column(String(500, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='描述')
    author = Column(String(100, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='作者')
    video = Column(String(50, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='视频path')
    audio = Column(String(50, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='音频path')
    subtitle = Column(String(50, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='字幕path')
    material_library_id = Column(Integer, nullable=False, server_default=text("'0'"), comment='素材库ID')
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"))


class IvdMaterialLibrary(Base):
    __tablename__ = 'ivd_material_library'

    id = Column(Integer, primary_key=True)
    name = Column(String(100, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='名称')
    description = Column(String(200, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='描述')
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"))


class IvdOnlineList(Base):
    __tablename__ = 'ivd_online_list'
    __table_args__ = {'comment': '用户在线表'}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, server_default=text("'0'"), comment='所属UserID')
    user_name = Column(String(60, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='用户名')
    token = Column(String(100, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='token')
    valid_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"), comment='到期时间')
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"))


class IvdPlugin(Base):
    __tablename__ = 'ivd_plugin'

    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"))
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class IvdSetting(Base):
    __tablename__ = 'ivd_setting'
    __table_args__ = {'comment': '设置表'}

    id = Column(Integer, primary_key=True)
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"))


class IvdTaskList(Base):
    __tablename__ = 'ivd_task_list'
    __table_args__ = {'comment': '任务列表'}

    id = Column(Integer, primary_key=True)
    task_id = Column(String(200, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='任务ID，全局唯一')
    user_id = Column(Integer, nullable=False, server_default=text("'0'"), comment='所属UserID')
    task_execution_mode = Column(Integer, nullable=False, server_default=text("'0'"), comment='任务执行方式，1：单次执行，2：重复执行（Crontab）')
    task_execution_content = Column(String(200, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='批量任务具体执行')
    task_priority = Column(Integer, nullable=False, server_default=text("'0'"), comment='优先级')
    task_limit = Column(Integer, nullable=False, server_default=text("'0'"), comment='每小时或每天任务最大条数，0不限制')
    task_limit_type = Column(Integer, nullable=False, server_default=text("'0'"), comment='限制类型，1：按小时，2：按天')
    is_custom_queue = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='是否单独任务队列，0：默认不单独队列')
    should_retry = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='是否需要重试')
    task_url = Column(String(300, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='任务URL')
    create_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"))
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class IvdTaskLog(Base):
    __tablename__ = 'ivd_task_log'

    id = Column(Integer, primary_key=True)
    task_type = Column(Integer, nullable=False, server_default=text("'0'"), comment='任务类别')
    task_desc = Column(String(255, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='任务描述')
    material_id = Column(Integer, nullable=False, server_default=text("'0'"), comment='素材ID')
    material_library_id = Column(Integer, nullable=False, server_default=text("'0'"), comment='素材库ID')
    create_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"))
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class IvdTaskQueue(Base):
    __tablename__ = 'ivd_task_queue'
    __table_args__ = {'comment': '任务队列表'}

    id = Column(Integer, primary_key=True)
    url = Column(String(300, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='爬虫爬取的URL')
    status = Column(Integer, nullable=False, comment='状态，0：队列中，1：执行中，2：成功，3：错误')
    task_id = Column(String(200, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='任务ID')
    error_code = Column(Integer, nullable=False, server_default=text("'0'"), comment='错误码')
    error_desc = Column(String(200, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='错误描述')
    create_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"))
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    material_id = Column(Integer, nullable=False, server_default=text("'0'"), comment='素材ID')
    material_library_id = Column(Integer, nullable=False, server_default=text("'0'"), comment='素材库ID')
    crawler_hash = Column(String(200, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='爬虫hash')


class IvdUserList(Base):
    __tablename__ = 'ivd_user_list'
    __table_args__ = {'comment': '用户表'}

    id = Column(Integer, primary_key=True)
    user_name = Column(String(60, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='用户名')
    password = Column(String(40, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='密码，MD5')
    privilege = Column(Integer, nullable=False, server_default=text("'0'"), comment='权限，0：管理员，1：普通')
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("'0000-01-01 00:00:00'"))
    avatar = Column(String(255, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='头像')
    nickname = Column(String(40, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='昵称')
    roles = Column(String(255, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='权限')
    permissions = Column(String(255, 'utf8mb4_0900_as_cs'), nullable=False, server_default=text("''"), comment='按钮级别权限')
