import argparse
import atexit
import logging
import os
import signal
from argparse import Namespace

from crawler.crawler_manager import crawler_manager


def signal_exists(signum, frame):
    pass


def app_exists():
    crawler_manager.stop()


def load_config(env_file: str):
    from dotenv import load_dotenv
    try:
        load_dotenv(dotenv_path=env_file, verbose=True)
    except Exception as ex:
        logging.error(ex)


if __name__ == "__main__":
    load_config(os.environ['IVD_CONFIG'])
    pass

G_CURR_PATH = os.path.dirname(os.path.abspath(__file__))


def parse_args() -> Namespace:
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--debug', action=argparse.BooleanOptionalAction, default=True)
    return parser.parse_args()


G_ARGS = parse_args()
G_ARGS_IS_DEBUG = G_ARGS.debug

if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.abspath(__file__))

    logging.info("crawler started!")
    # 退出处理
    signal.signal(signal.SIGINT, signal_exists)
    signal.siginterrupt(signal.SIGINT, False)
    atexit.register(app_exists)
    # 启动
    crawler_manager.start()
