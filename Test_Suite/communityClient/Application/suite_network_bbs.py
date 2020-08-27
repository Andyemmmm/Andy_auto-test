#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/30 14:19
# @File     : suite_network_bbs.py
# @Software : aiwen_ui

import unittest
from Test_Case.communityClient.Application import test_network_bbs


def get_suite():
    """组织测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_network_bbs.Test_Network_bbs_search))
    suite.addTests(loader.loadTestsFromTestCase(test_network_bbs.Test_Post_label_management))

    return suite