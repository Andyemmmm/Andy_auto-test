#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/23 9:33
# @File     : suite_doctor_class.py
# @Software : aiwen_ui

import unittest
from Test_Case.communityClient.Application import test_doctor_class


def get_suite():
    """组织测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_doctor_class.Test_Doctor_class))

    return suite