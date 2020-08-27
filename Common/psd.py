#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/23 14:51
# @File     : psd.py
# @Software : aiwen_api

import hashlib
import base64


def get_md5(s):
    """获取md5加密值

    :param s:
    :return:
    """
    m = hashlib.md5()
    m.update(str(s).encode("utf-8"))
    return m.hexdigest()


def get_base64(s):
    '''
    获取base64加密值
    :param s:
    :return:
    '''

    result = base64.b64encode(str(s).encode('utf-8'))
    return result
