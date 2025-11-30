def init():  # init
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    # Define a global variable
    _global_dict[key] = value


def get_value(key):
    # Obtain a global variable.
    # If it does not exist, it will prompt that reading the corresponding variable fails.
    try:
        return _global_dict[key]
    except:
        print('读取' + key + '失败\r\n')
