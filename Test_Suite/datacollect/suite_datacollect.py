#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/5/18 8:45
# @File     : suite_datacollect.py
# @Software : aiwen_ui

import unittest
from Test_Case.datacollect import test_datacollect, test_datacollect_iwask_home_click, \
    test_datacollect_iwask_list_click, test_datacollect_iwask_doctorinfo_click, \
    test_datacollect_iwask_shareContent_click, test_datacollect_iwask_operationtopic_click


def remain_event():
    """停留事件测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_datacollect.Test_datacollect))

    return suite


def iwask_home_click_event():
    """聚合首页的点击事件测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_datacollect_iwask_home_click.Test_iwask_home_click))

    return suite


def iwask_list_click_event():
    """聚合列表页的点击事件测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_datacollect_iwask_list_click.Test_iwask_list_click))

    return suite


def iwask_doctorinfo_click_event():
    """聚合医生详情页的点击事件测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_datacollect_iwask_doctorinfo_click.Test_iwask_doctorinfo_click))

    return suite


def iwask_share_click_event():
    """聚合套壳分享页的点击事件测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(
        loader.loadTestsFromTestCase(test_datacollect_iwask_shareContent_click.Test_iwask_shareContent_click))

    return suite


def iwask_operationtopic_click_event():
    """聚合专题运营页的点击事件测试用例"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(
        loader.loadTestsFromTestCase(test_datacollect_iwask_operationtopic_click.Test_iwask_operationtopic_click))

    return suite
