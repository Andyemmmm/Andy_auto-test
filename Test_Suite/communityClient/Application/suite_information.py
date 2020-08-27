#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/19 17:47
# @File     : suite_information.py
# @Software : aiwen_ui

import unittest
from Test_Case.communityClient.Application import test_information


def get_suite():
    """组织测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_information.Test_Information))

    return suite