import os
import random

G_RAND = None


def get_register_rand():
    global G_RAND
    if G_RAND is None:
        G_RAND = random.randint(10000, 99999)
        pass
    return G_RAND


CRAWLER_REGISTER_PATH = "/register"


def get_task_manager_register_url():
    return f"{os.environ['TASKMANAGER_URL']}{CRAWLER_REGISTER_PATH}"
