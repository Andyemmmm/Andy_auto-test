#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/4/14 17:01
# @File     : test_register.py
# @Software : auto_web_ui_test

import unittest

from Business.base_url import url_index
from Business.用户中心.task_注册业务 import register
from Common.selenium_library import SeleniumBase
from Page_Object.page_index import Page_Index


class Test_Register(unittest.TestCase):
    def setUp(self):
        self.driver = SeleniumBase().get_web_driver()
        pass

    def tearDown(self):
        SeleniumBase(self.driver).quit()
        pass

    def test_register(self):
        username = "liu007"
        password = "123456"
        pwdRepeat = "123456"
        mobile_phone = "13058157849"

        se = SeleniumBase(self.driver)
        se.logger.info("打开首页")
        se.get(url_index)
        se.logger.info("进入注册页")
        Page_Index(self.driver).click_免费注册()
        se.logger.info("注册流程")
        register(self.driver, username, password, pwdRepeat, mobile_phone)

        # 断言
        text = Page_Index(self.driver).get_登录成功提示您好()
        self.assertIn("您好", text)
        with open("Test_Data/user.txt", "a", encoding="utf-8") as f:
            f.write(f"{username}|{password}\n")
