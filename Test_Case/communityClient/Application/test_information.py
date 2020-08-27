#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/19 17:32
# @File     : test_information.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Business.communityClient.Application.task_咨询公告 import New_Information
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.Community_work.Application.Info.page_info import Page_Info


@ddt.ddt
class Test_Information(unittest.TestCase):
    """
    这是咨询公告模块的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        start_test(self.driver, 1)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Application/新建咨询公告.txt"))
    def test_information(self, title, cover, promulgator, photo, text, assert_type):
        '''新建咨询公告的测试用例'''
        se = SeleniumBase(self.driver)
        New_Information(se.driver, title, cover, promulgator, photo, text)
        time.sleep(2)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_Info(se.driver).get_提交成功()
            self.assertEqual('提交成功', text)
        elif assert_type == "2":
            # logger().Info("断言为空")
            text = Page_Info(se.driver).get_提交成功()
            self.assertEqual('提交成功', text)
        elif assert_type == "3":
            text = Page_Info(se.driver).get_提交成功()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
