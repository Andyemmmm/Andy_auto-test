#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/23 14:23
# @File     : test_communityweb.py
# @Software : aiwen_api

import unittest
import requests
import base64
from common.psd import get_base64
from common.get_redis import do_redis
from common.api_request import Api_request
from ddt import ddt, data
from common.Excel_data import Do_Excel
from common.domysql import Do_mysql
from common import context
from common import contants
from common import loging
from config.url import host
from common.split_str import spl
from requests_toolbelt.multipart.encoder import MultipartEncoder
from common import randomname
import json

logger = loging.Log(__name__)


class Test_Community_web(unittest.TestCase):
    '''社区web改版第一期登录，忘记密码的测试方法'''
    excel = Do_Excel(contants.case_file, 'patsplitsub')
    case = excel.read_Excel()

    def setUp(self):
        logger.info('开始测试')
        logger.info('初始化一个session')
        self.session = requests.Session()

    def tearDown(self):
        logger.info('测试结束')
        self.session.close()

    def test_001(self):
        '''
        用户操作 - 用户密码登录
        '''
        s = self.session
        phone = 18679610587
        pwd3 = get_base64(123456)
        data = {
            "phone": phone,
            "password": pwd3
        }

        res = s.get(host + '/api/bcustomer/login', params=data)
        print(res.request)
        self.assertEqual('请求成功', res.json()['message'])

    def test_002(self):
        '''
        用户操作 - 验证码登录
        '''
        s = self.session
        mobile = {
            "mobile": 13762106743
        }
        c = s.get(host + '/api/bcustomer/sendCode', params=mobile)
        print(c.text)
        self.assertEqual('请求成功', c.json().get('message'))
        phone = 13762106743
        code = do_redis(phone)
        print(code)
        data = {
            "phone": phone,
            "code": code
        }

        res = s.get(host + '/api/organization/login', params=data)
        print(res.request)
        self.assertEqual('请求成功', res.json()['message'])

    def test_003(self):
        '''
        用户操作 - 忘记密码/重置密码
        '''
        s = self.session
        mobile = {
            "mobile": 18589036892
        }
        d = s.get(host + '/api/bcustomer/sendCode', params=mobile)
        print(d.text)
        self.assertEqual('请求成功', d.json().get('message'))
        phone = 18589036892
        code = do_redis(phone)
        print(code)
        data = {
            "phone": phone,
            "code": code,
            "pwd": 123456
        }

        res = s.post(host + '/api/bcustomer/resetPwd', data=data)
        print(res.request)
        self.assertEqual('操作成功', res.json()['message'])

    def test_004(self):
        '''
        用户操作 - 申请体验社区用户信息
        '''
        s = self.session
        phone = 18616673703
        data = {
            "phone": phone,
            "type": 1,
            "name": 'andy'
        }

        res = s.post(host + '/api/customerinfo/add', data=data)
        print(res.request)
        self.assertEqual('您已体验过社区，快创建属于自己的社区吧', res.json()['message'])
