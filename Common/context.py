import re
from common.config import ReadConfig
from common.loging import Log
import configparser
from common.psd import get_base64


class Context:
    name = None


# def replace(data):
#     p = '#(.*?)#'
#     m = re.findall(p, data)#查找这个正则表达式里面的内容并返回一个列表
#     for i in m:#遍历这个列表
#         try:
#             v = ReadConfig().get('data', i) #取配置文件里面的值
#         except configparser.NoOptionError as e: # 如果配置文件里面没有的时候，去Context里面取
#             if hasattr(Context,i):
#                 v = getattr(Context,i)
#             else:
#                 print('找不到该参数')
#             raise e
#         data = re.sub(p, v, data, count=1)#替换掉data里面的值
#     return data
logger = Log(__name__)


def replace(data):
    p = "#(.*?)#"  # 正则表达式
    while re.search(p, data):
        print(data)
        m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
        g = m.group(1)  # 拿到参数化的KEY
        try:
            v = ReadConfig().get('data', g)  # 根据KEY取配置文件里面的值
        except configparser.NoOptionError as e:  # 如果配置文件里面没有的时候，去Context里面取
            if hasattr(Context, g):
                v = getattr(Context, g)
            else:
                logger.error('找不到参数化的值:{}'.format(e))
                raise e
        print(v)
        # 记得替换后的内容，继续用data接收
        data = re.sub(p, str(v), data, count=1)  # 查找替换,count查找替换的次数

    return data


def replaces(data):
    p = "#(.*?)#"  # 正则表达式
    while re.search(p, data):
        print(data)
        m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
        g = m.group(1)  # 拿到参数化的KEY
        try:
            v = ReadConfig().get('data', g)  # 根据KEY取配置文件里面的值
            if g == 'password':
                v = get_base64(v)
                setattr(Context, 'password', v)
        except configparser.NoOptionError as e:  # 如果配置文件里面没有的时候，去Context里面取
            if hasattr(Context, g):
                v = getattr(Context, g)
            else:
                logger.error('找不到参数化的值:{}'.format(e))
                raise e
        print(v)
        # 记得替换后的内容，继续用data接收
        data = re.sub(p, str(v), data, count=1)  # 查找替换,count查找替换的次数

    return data
