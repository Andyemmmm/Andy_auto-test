#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/23 15:36
# @File     : get_redis.py
# @Software : aiwen_api

import redis


def do_redis(phone):
    '''获取手机验证码'''
    r = redis.Redis("192.168.254.143", "8001")
    # try:
    res = r.get(f'{phone}_VERIFICATION_CODE')
    res = res.decode()
    return res.replace('"', '')
    # except:
    #     r = redis.Redis("192.168.254.142", "8001")
    #     res = r.get(f'{phone}_VERIFICATION_CODE')
    #     res = res.decode()
    #     return res.replace('"', '')
