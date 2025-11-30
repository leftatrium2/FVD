import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class SNScopedSession(object):
    s_session: scoped_session = None

    def __enter__(self):
        if 'IS_USE_DB' not in os.environ:
            logging.error("environment has not IS_USE_DB")
            return None
        is_use_db = os.environ['IS_USE_DB']
        url = None
        if is_use_db == 'mysql':
            if 'MYSQL_URL' not in os.environ:
                logging.error("environment has not MYSQL_URL!!!")
                return None
            url = os.environ['MYSQL_URL']
        elif is_use_db == 'sqlite':
            if 'SQLITE_URL' not in os.environ:
                logging.error("environment has not SQLITE_URL!!!")
                return None
            url = os.environ['SQLITE_URL']
        if not url:
            logging.error("url is None!")
            return None
        engine = create_engine(url=url, pool_pre_ping=True, pool_size=10, max_overflow=50, pool_recycle=28)
        new_session = sessionmaker(engine)
        self.s_session = scoped_session(new_session)
        return self.s_session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s_session.remove()


def get_db_client():
    return SNScopedSession()
