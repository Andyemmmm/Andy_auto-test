#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/10 17:17
# @File     : test_content_management.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.adminClient.task_community_management import operation_online_community
from Business.adminClient.task_login import login_admin, start_test
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.adminClient.page_community_management import Page_Community_message


@ddt.ddt
class Test_up_online_community(unittest.TestCase):
    """
    这是社区管理--社区信息--社区上线的测试类
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
    @ddt.data(*read_txt("Test_Data/adminClient/community_management/社区操作上线"))
    def test_001(self, value, args, arguments, reason, assert_type):
        '''社区管理---社区信息---社区操作上线'''

        se = SeleniumBase(self.driver)
        if args == '社区名称':
            operation_online_community(se.driver, community_name=value, arguments=arguments, reason=reason)
        if args == '社区id':
            operation_online_community(se.driver, community_id=value, arguments=arguments, reason=reason)
        if args == '机构名称':
            operation_online_community(se.driver, organization_name=value, arguments=arguments, reason=reason)
        if args == '机构id':
            operation_online_community(se.driver, organization_id=value, arguments=arguments, reason=reason)
        time.sleep(1)
        if assert_type == '1':
            text = Page_Community_message(se.driver).get_msg()
            if text is None:
                text = Page_Community_message(se.driver).get_msg()
            self.assertEqual('操作成功', text)
        if assert_type == '2':
            text = Page_Community_message(se.driver).get_msg()
            self.assertEqual('该社区未认证，无法执行上线操作', text)


@ddt.ddt
class Test_down_online_community(unittest.TestCase):
    """
    这是社区管理--社区信息--社区下架的测试类
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
    @ddt.data(*read_txt("Test_Data/adminClient/community_management/社区操作下架"))
    def test_001(self, value, args, arguments, reason):
        '''社区管理---社区信息---社区操作下架'''

        se = SeleniumBase(self.driver)
        if args == '社区名称':
            operation_online_community(se.driver, community_name=value, arguments=arguments, reason=reason)
        if args == '社区id':
            operation_online_community(se.driver, community_id=value, arguments=arguments, reason=reason)
        if args == '机构名称':
            operation_online_community(se.driver, organization_name=value, arguments=arguments, reason=reason)
        if args == '机构id':
            operation_online_community(se.driver, organization_id=value, arguments=arguments, reason=reason)
        time.sleep(1)

        text = Page_Community_message(se.driver).get_msg()
        self.assertEqual('操作成功', text)
