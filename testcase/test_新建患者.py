#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/7/8 13:51
# @File     : test_新建患者.py
# @Software : Test_dental

import unittest
import requests
from HTMLReport import logger
import ddt
from common.read_txt import read_txt
from config.url import url_内测
@ddt.ddt
class Test_新建患者(unittest.TestCase):
    def setUp(self):
        logger().info('初始化一个session')
        self.session=requests.Session()
        pass

    def tearDown(self):
        logger().info('关闭会话')
        self.session.close()
        pass

    @ddt.unpack
    @ddt.data(*read_txt('data/管家号60105.txt'))
    def test_新建患者(self,dentalid,doctorname,password):
        session = self.session
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        data = {
            'dentalid': dentalid,
            'doctorname': doctorname,
            'password': password
        }
        respose=session.post(url_内测+'/member/employeelogin',headers=headers,data=data)
        logger().info(f'状态码：', respose.status_code)
        logger().info(f'url：', respose.url)
        logger().info(f'返回结果：', respose.text)
        logger().info(f'返回结果：', respose.json())

        logger().info('新建患者')

        name='晓m'
        sex='女'
        age=19
        phone=133682
        headers={
            'Content-Type':'application/x-www-form-urlencoded'
        }

        data={
            'customer[Name]':{name},
            'customer[Sex]':{sex},
            'customer[Age]':{age},
            'customer[PatientStar]':'1',
            'customer[Phone]':{phone}
        }
        respose=session.post(url_内测+'patient/addpatient',headers=headers,data=data)
        logger().info(respose.status_code)
        logger().info(respose.url)
        logger().info(respose.text)
        logger().info(respose.json())
        customerid=respose.json().get('list').get('customerid')
        self.assertEqual(1,respose.json().get('code'))
        self.assertEqual(200, respose.status_code)
        self.assertEqual('ok',respose.json().get('info'))
        self.assertIn('customerid',respose.json().get('list'))
        self.assertIn('command',respose.json())
        with open('data/患者ID.txt','a',encoding='utf-8')as f:
            f.write(f'{customerid}\n')