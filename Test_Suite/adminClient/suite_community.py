#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/10 15:50
# @File     : suite_community.py
# @Software : aiwen_ui

import unittest
from Test_Case.adminClient import test_community_management
from Test_Case.communityClient.Community import test_home_page


def up_online_community():
    """组织测试用例--社区管理--社区信息--社区操作上线"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_community_management.Test_up_online_community))
    suite.addTests(loader.loadTestsFromTestCase(test_home_page.Test_Online_application))

    return suite


def down_online_community():
    """组织测试用例--社区管理--社区信息--社区操作下架"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_community_management.Test_down_online_community))

    return suite
