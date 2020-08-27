#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/11 15:18
# @File     : do_redis.py
# @Software : aiwen_ui

import redis


def do_redis(phone):
    '''获取手机验证码'''
    r = redis.Redis("192.168.254.143", "8001")
    res = r.get(f'{phone}_VERIFICATION_CODE')
    res = res.decode()
    return res.replace('"', '')


# a = do_redis(15323751280)
# a = a.replace('"', '')
# print(a)
