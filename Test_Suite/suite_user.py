#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/7/8 11:37
# @File     : suite_user.py
# @Software : Test_dental

import unittest

from testcase import test_Bplatfrom_adduser, test_demo, test_communityweb


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # suite.addTests(loader.loadTestsFromTestCase(test_login.Test_login))
    # suite.addTests(loader.loadTestsFromTestCase(test_新建患者.Test_新建患者))
    # suite.addTests(loader.loadTestsFromTestCase(test_demo.Test_demo))
    suite.addTests(loader.loadTestsFromTestCase(test_communityweb.Test_Community_web))
    return suite
