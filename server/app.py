import argparse
import atexit
import logging
import os
import platform
import signal
import sys

from flask import Flask, request
from flask_babel import Babel
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from crawler.utils.yt_dlp_utils import ytdlp_support_manager
from modules.about import about_router
from modules.async_routes import async_routes_router
from modules.crawler import crawler_router
from modules.index import index_router
from modules.library import library_router
from modules.log import log_router
from modules.login import login_router
from modules.settings import settings_router
from modules.task import task_router
from modules.user import user_router
from task.task_manager import g_task_manager
from utils import global_var, const, log_utils
from utils.db import db
from utils.result import result_failure


def parse_args() -> None:
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--debug', action=argparse.BooleanOptionalAction, default=False)
    args = parser.parse_args()
    global_var.set_value(const.DEBUG_KEY, args.debug)
    global_var.set_value(const.PORT_KEY, os.environ.get(const.PORT_KEY, 9001))


def load_config(env_file: str):
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=env_file, verbose=True)


def handle_app_exists(signum, frame):
    print(f"handle_dispatcher_exists called with signal: {signum}")
    sys.exit()


def app_exists():
    g_task_manager.stop()
    pass


if __name__ == "__main__":
    ytdlp_support_manager.init()
    load_config(os.environ['IVD_CONFIG'])
    global_var.init()
    log_utils.init_logging()
    parse_args()

    # init TaskManager
    g_task_manager.start()

    # Flask
    app = Flask(__name__)
    # 跨域
    CORS(app, supports_credentials=True)
    # i18n
    babel = Babel(app)
    # configure
    if 'IS_USE_DB' not in os.environ:
        logging.error("environment has not IS_USE_DB")
        raise Exception("environment has not IS_USE_DB")
    is_use_db = os.environ['IS_USE_DB']
    url = None
    if is_use_db == 'mysql':
        if 'MYSQL_URL' not in os.environ:
            logging.error("environment has not MYSQL_URL!!!")
            raise Exception("environment has not MYSQL_URL!!!")
        url = os.environ['MYSQL_URL']
    elif is_use_db == 'sqlite':
        if 'SQLITE_URL' not in os.environ:
            logging.error("environment has not SQLITE_URL!!!")
            raise Exception("environment has not SQLITE_URL!!!")
        url = os.environ['SQLITE_URL']
    app.config['SQLALCHEMY_DATABASE_URI'] = url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "pool_pre_ping": True,
        "pool_recycle": 28,
        'pool_timeout': 900,
        'pool_size': 10,
        'max_overflow': 50,
    }
    # mysql or sqlite init
    db.init_app(app)
    # web module register
    app.register_blueprint(about_router)
    app.register_blueprint(login_router)
    app.register_blueprint(user_router)
    app.register_blueprint(index_router)
    app.register_blueprint(task_router)
    app.register_blueprint(settings_router)
    app.register_blueprint(log_router)
    app.register_blueprint(async_routes_router)
    app.register_blueprint(library_router)
    app.register_blueprint(crawler_router)

    # process when exit
    if not platform.system().lower() == 'windows':
        signal.signal(signal.SIGINT, handle_app_exists)
        signal.siginterrupt(signal.SIGINT, False)
        signal.signal(signal.SIGTERM, handle_app_exists)
        signal.siginterrupt(signal.SIGTERM, False)
    atexit.register(app_exists)


@app.before_request
def before_request():
    pass


@app.errorhandler(HTTPException)
def handle_error(e):
    code = e.code
    msg = e.description
    return result_failure(code, msg)


if __name__ == "__main__":
    app.run(debug=global_var.get_value(const.DEBUG_KEY), host='0.0.0.0', port=global_var.get_value(const.PORT_KEY),
            threaded=True)


@app.after_request
def after_request(response):
    origin = request.headers.get('Origin')
    response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response
