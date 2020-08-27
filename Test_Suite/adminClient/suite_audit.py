#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/10 15:50
# @File     : suite_audit.py
# @Software : aiwen_ui

import unittest
from Test_Case.adminClient import test_audit_management


def Review_community():
    """组织测试用例--审核管理--社区资质审核--审核社区"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_audit_management.Test_Review_community))

    return suite


def Online_application():
    """组织测试用例--审核管理--社区上线申请--社区上线"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_audit_management.Test_Online_application))

    return suite
