#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/20 15:18
# @File     : suite_health_knowledge.py
# @Software : aiwen_ui

import unittest
from Test_Case.communityClient.Application import test_health_knowledge


def get_suite():
    """组织测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_health_knowledge.Test_Health_knowledge))

    return suite