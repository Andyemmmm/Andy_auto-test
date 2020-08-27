import datetime
import threading

count = 0
now = datetime.datetime.now().strftime("%m%d%H%M")
_lock = threading.Lock()


def get_rendom_username(n: int, prefix="t") -> list:
    """获取随机不重复的用户名序列

    :param n: 数量
    :param prefix: 前缀
    :return: 列表
    """
    _lock.acquire()
    global count
    L = []
    for i in range(n):
        L.append(f"{prefix}{now}{count}")
        count += 1
    _lock.release()
    return L


count_phone = 0
_lock_phone = threading.Lock()


def get_random_phone(prefix="133"):
    """随机获取收集号码

    :param prefix: 前缀
    :return:
    """
    _lock_phone.acquire()
    global count_phone
    phone = f"{prefix}{now[2:]}{count_phone:02}"
    count_phone += 1
    _lock_phone.release()
    return phone
