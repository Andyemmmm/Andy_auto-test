#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 17:17
# @File     : test_audit_management.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.adminClient.task_audit_management import Review_community, Online_application
from Business.adminClient.task_login import login_admin, start_test
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.adminClient.page_audit_management import Page_Community_qualification_audit, \
    Page_Community_online_application


@ddt.ddt
class Test_Review_community(unittest.TestCase):
    """
    这是审核管理--社区认证审核--社区认证审核的测试类
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

    @ddt.unpack
    @ddt.data(*read_txt("Test_Data/adminClient/audit_management/审核社区"))
    def test_001(self, name, cause=None, reason=None):
        '''审核管理---社区认证审核---审核社区'''

        se = SeleniumBase(self.driver)
        Review_community(se.driver, name, cause, reason)
        time.sleep(0.5)
        text = Page_Community_qualification_audit(se.driver).get_msg()
        self.assertEqual('操作成功', text)


@ddt.ddt
class Test_Online_application(unittest.TestCase):
    """
    这是审核管理--社区上线申请--社区上线审核的测试类
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

    @ddt.unpack
    @ddt.data(*read_txt("Test_Data/adminClient/audit_management/上线社区"))
    def test_001(self, name, reason=None):
        '''审核管理---社区上线申请---上线社区'''

        se = SeleniumBase(self.driver)
        Online_application(se.driver, name, reason)
        time.sleep(0.5)
        text = Page_Community_online_application(se.driver).get_msg()
        self.assertEqual('操作成功', text)
