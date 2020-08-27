#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/7/8 11:37
# @File     : suite_user.py
# @Software : Test_dental

import unittest

from testcase import test_Bplatfrom_adduser, test_demo, test_communityweb, test_communityweb1


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_communityweb.Test_Community_web))
    # suite.addTests(loader.loadTestsFromTestCase(test_communityweb1.Testpatsplitsub))
    return suite
