#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 16:07
# @File     : suite_login.py
# @Software : aiwen_ui

import unittest
from Test_Case.adminClient import test_login


def get_suite():
    """组织测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_login.TestLogin))

    return suite
