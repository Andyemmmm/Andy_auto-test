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
from common.config import ReadConfig
import configparser
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


@ddt
class Testpatsplitsub(unittest.TestCase):
    '''分类管理-添加B端官网用户信息的测试类'''
    excel = Do_Excel(contants.case_file, 'community_web')
    case = excel.read_Excel()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = Api_request()

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()

    @data(*case)
    def test_001(self, case):
        '''分类管理-添加B端官网用户信息'''
        logger.info('开始测试:{}'.format(case.title))
        case.data = context.replaces(case.data)
        if case.title == '用户密码登录':
            phone = ReadConfig().get('data', "phone")
            password = ReadConfig().get('data', "password")
            password = get_base64(password)
            case.data = {
                "phone": phone,
                "password": password
            }
        res = self.http_request.http_request(method=case.method, url=case.url, data=case.data)
        print(res.request)
        print(res.url)
        try:
            self.assertEqual(str(case.expected), res.json()['message'])
            # if case.title == '登陆':
            #     setattr(context.Context, 'token', res.json()['data']['token'])
            #
            # if case.title == '首页-工作台':
            #     pass
            # setattr(context.Context,'patientname',randomname.random_name())
            # print(context.Context.patientname)
            # if case.title == '新建患者成功':
            #     # sql = eval(context.replace(case.sql))
            #     doctorid = Do_mysql().fetch_one(case.sql)['DoctorID']
            #     setattr(context.Context,'doctorid',doctorid)
            #     setattr(context.Context, 'customerid', res.json()['list']['customerid'])

            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='PASS')
        except AssertionError as e:
            self.excel.write_excel(row=case.case_id + 1, actual=res.text, result='FAIL')
            logger.error('报错:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))
