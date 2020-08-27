#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/24 16:08
# @File     : suite_questionnaire.py
# @Software : aiwen_ui

import unittest
from Test_Case.communityClient.Application import test_questionnaire


def get_suite():
    """组织测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_questionnaire.Test_Questionnaire))

    return suite