import hashlib


def get_md5(s):
    """获取md5加密值

    :param s:
    :return:
    """
    m = hashlib.md5()
    m.update(str(s).encode("utf-8"))
    return m.hexdigest()
