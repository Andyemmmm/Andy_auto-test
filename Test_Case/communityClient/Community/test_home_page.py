#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/11 9:23
# @File     : test_home_page.py
# @Software : aiwen_ui

import unittest
import time
from Business.adminClient.task_audit_management import Online_application
from Business.communityClient.用户中心.task_new_community import up_online
from Common.selenium_library import SeleniumBase
from Business.communityClient.用户中心.task_登录业务 import login_po
from Page_Object.adminClient.page_audit_management import Page_Community_online_application
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Business.adminClient.task_login import start_test


class Test_up_online(unittest.TestCase):
    """
    这是社区首页操作上线的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_po(self.driver, username=18679610587, password=123456)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    def test_001(self):
        '''首页--操作立即上线的测试用例'''

        se = SeleniumBase(self.driver)
        up_online(se.driver)
        time.sleep(1)
        text = Page_Home(se.driver).get_msg()
        self.assertEqual('操作成功', text)


class Test_Online_application(unittest.TestCase):
    """
    这是爱问大后台的----审核管理----的社区上线申请的测试用例
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        start_test(self.driver)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    def test_001(self):
        '''审核管理---社区上线申请---上线审核通过'''

        se = SeleniumBase(self.driver)
        Online_application(se.driver)
        time.sleep(0.5)
        text = Page_Community_online_application(se.driver).get_msg()
        if text is None:
            print('运行循环')
            while True:
                text = Page_Community_online_application(se.driver).get_msg()
                if text:
                    break
        self.assertEqual('操作成功', text)
