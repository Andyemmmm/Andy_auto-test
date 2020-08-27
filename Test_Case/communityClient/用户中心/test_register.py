#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/11 17:26
# @File     : test_register.py
# @Software : aiwen_ui

import unittest
from Business.communityClient.用户中心.task_注册业务 import register
from Common.selenium_library import SeleniumBase
from Page_Object.page_register import Page_Register


class Test_Register(unittest.TestCase):
    def setUp(self):
        self.driver = SeleniumBase().get_web_driver()
        pass

    def tearDown(self):
        SeleniumBase(self.driver).quit()
        pass

    def test_register(self):
        '''社区B端注册测试用例'''
        se = SeleniumBase(self.driver)
        register(se.driver)
        text = Page_Register(se.driver).get_msg()
        self.assertEqual('操作成功', text)
