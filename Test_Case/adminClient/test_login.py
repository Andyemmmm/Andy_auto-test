#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 15:45
# @File     : test_login.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.adminClient.task_login import login_admin
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.adminClient.page_login import Page_Login
from Page_Object.adminClient.page_home import Page_Home


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/admin_login.txt"))
    def test_login(self, username, password, assert_type):
        """登录的测试用例

        :param username: 用户名
        :param password: 密码
        :param assert_type: 断言类型：1-成功，2-用户名或用户名与密码都为空，3-密码为空
        :return:
        """
        se = SeleniumBase(self.driver)
        login_admin(se.driver, username, password)
        time.sleep(2)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_Home(se.driver).get_消息()
            self.assertEqual('登录成功!', text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Login(se.driver).get_登录错误提示()
            self.assertEqual("账号密码错误，请重新输入!", text)
        elif assert_type == "3":
            text = Page_Login(se.driver).get_登录错误提示()
            self.assertEqual("密码错误", text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
