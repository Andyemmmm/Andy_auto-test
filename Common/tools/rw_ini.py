from configparser import ConfigParser


def read_config(file):
    """读取配置文件

    :param file: 路径
    :return: 配置文件对象
    """
    rc = ConfigParser()
    rc.read(file, encoding="utf-8")
    return rc


def write_config(file: str, section, option, value=None):
    """写配置文件

    :param file: 文件路径
    :param section: 目标
    :param option: 选项
    :param value: 值
    :return:
    """
    rc = ConfigParser()
    rc.read(file, encoding="utf-8")
    rc.set(section, option, value)
    with open(file, "w", encoding="utf-8") as f:
        rc.write(f)
