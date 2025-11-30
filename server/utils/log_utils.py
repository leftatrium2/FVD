import logging
import os
import re
from logging.handlers import TimedRotatingFileHandler

LOG_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# g_log_dir = LOG_PROJECT_DIR + f'{os.sep}log'
g_log_dir = os.getcwd() + f'{os.sep}log'


def init_logging() -> None:
    init_console_out()


def init_console_out() -> None:
    os.makedirs(g_log_dir, exist_ok=True)
    fmt_str = '%(asctime)s pid:%(process)d tid:%(thread)d line:%(lineno)d %(filename)s %(funcName)s : %(levelname)s  %(message)s'
    formatter = logging.Formatter(fmt_str)
    logging.basicConfig(
        level=logging.DEBUG,
        format=fmt_str,
        datefmt='%Y-%m-%d %A %H:%M:%S',
        filemode='w')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

    # filename is the prefix of the output log file name
    # when is a string defined as follows:
    # “S”: Seconds
    # “M”: Minutes
    # “H”: Hours
    # “D”: Days
    # “W”: Week day (0=Monday)
    # “midnight”: Roll over at midnight
    # interval refers to how many units of time to wait before Logger will automatically rebuild the file. Of course, the creation of this file
    # Depends on filename+suffix. If this file has the same name as the previous file, the previous file will be automatically overwritten, so
    # In some cases, the suffix to be defined cannot be repeated because of when.
    # backupCount is the number of retained logs. The default value of 0 will not automatically delete the log. If set to 10, during the creation process of the file
    # The library will determine whether there are more than 10. If it exceeds, it will be deleted starting from the first created one.
    log_file_handler = TimedRotatingFileHandler(filename=g_log_dir + f"{os.sep}fvd", when='midnight', interval=1,
                                                backupCount=7, encoding='utf-8')
    log_file_handler.suffix = '%Y-%m-%d.log'
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(log_file_handler)
