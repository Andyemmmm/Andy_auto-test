#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/7/8 10:10
# @File     : test_login.py
# @Software : Test_dental

import unittest
import requests
from HTMLReport import logger
import ddt
from common.read_txt import read_txt
from config.url import url_内测
@ddt.ddt
class Test_login(unittest.TestCase):
    def setUp(self):
        logger().info('初始化一个session')
        self.session=requests.Session()

    def tearDown(self):
        logger().info('关闭session')
        self.session.close()
    @ddt.unpack
    @ddt.data(*read_txt('data/管家号60105.txt'))
    def test_login(self,dentalid,doctorname,password):
        session=self.session
        headers={
            'Content-Type':'application/x-www-form-urlencoded'
        }
        data={
            'dentalid':dentalid,
            'doctorname':doctorname,
            'password':password
        }
        logger().info('管家号：',{dentalid})
        logger().info('登陆账号：',{doctorname})
        logger().info('密码：',{password})
        respose=session.post(url_内测+'/member/employeelogin',headers=headers,data=data)
        logger().info(f'状态码：',respose.status_code)
        logger().info(f'url：',respose.url)
        logger().info(f'返回结果：',respose.text)
        logger().info(f'返回结果：',respose.json())

        self.assertEqual(200,respose.status_code)
        self.assertEqual(1,respose.json().get('code'))
        self.assertEqual('登录成功',respose.json().get('info'))
