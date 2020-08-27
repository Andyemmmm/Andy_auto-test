#!/usr/bin/python3
# @Author   : Andy
# @time     : 2019/7/2 10:31
# @File     : test_online_class.py
# @Software : Test_dental

import requests
from common.config import ReadConfig
from common import loging
from common.split_str import spl
import json

logger = loging.Log(__name__)


class Api_request:

    def __init__(self):
        self.session = requests.sessions.session()

    def Url(self, url):
        config = ReadConfig()
        url = config.get('api', 'wenwo_url') + url
        return url

    def http_request(self, method, url, data=None, json=None, headers=None):
        method = method.upper()

        if type(data) == str:
            data = eval(data)

        logger.debug("请求的url:{}".format(self.Url(url)))
        logger.debug("请求的数据:{}".format(data))
        if method == 'GET':
            resp = self.session.request(method=method, url=self.Url(url), params=data, headers=headers)

        elif method == 'POST':
            if type(data) == str:
                data, n = spl(data)
                print(f'post请求的数据是：{data}')
                print(f'post请求的数据类型是：{type(data)}')
                if json:
                    resp = self.session.request(method=method, url=self.Url(url), json=json)

                else:
                    resp = self.session.request(method=method, url=self.Url(url), data=data, headers=headers)

        elif method == 'DELETE':
            pass
        elif method == 'PUT':
            pass
        else:
            logger.error('没有这个请求方式')
        return resp

    def close(self):
        self.session.close()
