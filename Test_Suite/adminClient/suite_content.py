#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/10 15:50
# @File     : suite_content.py
# @Software : aiwen_ui

import unittest
from Test_Case.adminClient import test_content_management


def article_detail():
    """组织测试用例--查看内容管理--文章管理--医生文章详情页"""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_content_management.Test_Article_Detail))

    return suite


def article_detail_del():
    '''组织测试用例--删除内容管理--文章管理--医生文章详情页'''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(test_content_management.Test_Article_Detail_del))

    return suite
