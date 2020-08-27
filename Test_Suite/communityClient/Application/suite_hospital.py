#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/23 14:36
# @File     : suite_hospital.py
# @Software : aiwen_ui

import unittest
from Test_Case.communityClient.Application import test_hospital


def get_suite():
    """组织测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_hospital.Test_Hospital))

    return suite