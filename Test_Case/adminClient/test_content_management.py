#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 17:17
# @File     : test_content_management.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.adminClient.task_content_management import article_view, article_detail, del_article
from Business.adminClient.task_login import login_admin
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.adminClient.page_content_management import Page_Content_Management, Page_Article_Detail


class Test_Article_Detail(unittest.TestCase):
    """
    这是内容管理--文章管理--医生文章的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_admin(self.driver, username='tina', password=111111)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    def test_001(self):
        ''' 查看内容管理--文章管理--医生文章列表详情数据的测试用例'''

        se = SeleniumBase(self.driver)
        article_view(se.driver)
        text = Page_Content_Management(se.driver).get_列表第一行_标题()

        article_detail(se.driver)
        time.sleep(3)
        text1 = Page_Article_Detail(se.driver).get_标题()
        text2 = Page_Article_Detail(se.driver).get_文章内容()
        time.sleep(1)
        self.assertEqual(text, text1)
        self.assertEqual('文章内容', text2)


class Test_Article_Detail_del(unittest.TestCase):
    """
    这是删除内容管理--文章管理--医生文章的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_admin(self.driver, username='tina', password=111111)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    def test_001(self):
        '''删除内容管理--文章管理--医生文章详情页删除'''

        se = SeleniumBase(self.driver)
        article_view(se.driver)
        time.sleep(1)
        article_detail(se.driver)
        time.sleep(1)
        del_article(se.driver)
        text = Page_Content_Management(se.driver).get_消息()
        self.assertEqual('操作成功!', text)
