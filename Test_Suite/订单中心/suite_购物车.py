#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/4/21 11:09
# @File     : suite_购物车.py
# @Software : auto_web_ui_test

import unittest
from Test_Case.订单中心 import test_购物车


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_购物车.Test_购物车))
    return suite
