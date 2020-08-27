#!/usr/bin/python3
# @Author   : Andy
# @time     : 2019/11/28 14:31
# @File     : split_str.py
# @Software : Test_dental


import json
from requests_toolbelt.multipart.encoder import MultipartEncoder


def spl(data):
    '''
    这是一个对接口数据序列化的方法
    :param data: 接口的入参
    :return: 序列化之后的接口参数
    '''
    if data[1:9] == 'dataJson':
        c = data[11:]
        a = {
            'dataJson': str(c)
        }
        b = None

    elif data[1:5] == 'live':
        c = data[7:]
        a = {
            'live': str(c)
        }
        b = None
    elif data[2:9] == 'file_id' or data[2:6] == 'file':
        data = eval(data)
        a = MultipartEncoder(fields=data)
        b = a.content_type

    else:
        a = json.loads(data)
        b = None
    return a, b


spl('"dataJson":{"phone":"18679610587","password":"654321"}')
