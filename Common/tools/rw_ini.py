from configparser import ConfigParser


def read_config(file):
    """读取配置文件

    :param file: 路径
    :return: 配置文件对象
    """
    rc = ConfigParser()
    rc.read(file, encoding="utf-8")
    return rc
