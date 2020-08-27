#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/30 10:38
# @File     : test_network_bbs.py
# @Software : aiwen_ui

import unittest
import ddt
import time
from Common.tools.read_txt import read_txt
from Business.communityClient.Application.task_network_bbs import screen_开始, screen_普通贴, screen_精华帖, screen_是推荐, \
    screen_否推荐, screen_是置顶, screen_否置顶, new_新建帖子标签
from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Common.selenium_library import SeleniumBase
from Page_Object.community.Community_work.Application.Network_BBS.page_Network_management import Page_Network_management
from Page_Object.community.Community_work.Application.Network_BBS.page_Post_label_management import \
    Page_Post_label_management


@ddt.ddt
class Test_Network_bbs_search(unittest.TestCase):
    """
    这是圈子论坛模块----圈子管理的筛选功能的测试类
    """

    @classmethod
    def setUpClass(cls):
        """测试前"""
        cls.driver = SeleniumBase().get_web_driver()
        start_test(cls.driver, 1, '5df303cabfe5230006187832')
        pass

    @classmethod
    def tearDownClass(cls):
        """测试后"""
        SeleniumBase(cls.driver).quit()
        pass

    def test_01(self):
        '''筛选普通贴'''

        se = SeleniumBase(self.driver)
        screen_开始(se.driver)
        screen_普通贴(se.driver)
        time.sleep(2)
        text = Page_Network_management(se.driver).find_number('帖子类型')
        asserts = len(set(text))
        try:
            self.assertEqual(1, asserts)
            self.assertIn('普通帖', text)
            Page_Network_management(se.driver).click_帖子类型_全部()
        except Exception as e:
            Page_Network_management(se.driver).click_帖子类型_全部()
            raise e

    def test_02(self):
        '''筛选精华帖'''
        se = SeleniumBase(self.driver)
        screen_精华帖(se.driver)
        time.sleep(2)
        text = Page_Network_management(se.driver).find_number('帖子类型')
        asserts = len(set(text))
        try:
            self.assertEqual(1, asserts)
            self.assertIn('精华帖', text)
            Page_Network_management(se.driver).click_帖子类型_全部()
        except Exception as e:
            Page_Network_management(se.driver).click_帖子类型_全部()
            raise e

    def test_03(self):
        '''筛选是推荐'''
        se = SeleniumBase(self.driver)
        screen_是推荐(se.driver)
        time.sleep(2)
        text = Page_Network_management(se.driver).find_number('是否推荐')
        asserts = len(set(text))
        try:
            self.assertEqual(1, asserts)
            self.assertIn('是', text)
            Page_Network_management(se.driver).click_是否推荐_全部()
        except Exception as e:
            Page_Network_management(se.driver).click_是否推荐_全部()
            raise e

    def test_04(self):
        '''否推荐'''
        se = SeleniumBase(self.driver)
        screen_否推荐(se.driver)
        time.sleep(2)
        text = Page_Network_management(se.driver).find_number('是否推荐')
        asserts = len(set(text))
        try:
            self.assertEqual(1, asserts)
            self.assertIn('否', text)
            Page_Network_management(se.driver).click_是否推荐_全部()
        except Exception as e:
            Page_Network_management(se.driver).click_是否推荐_全部()
            raise e

    def test_05(self):
        '''是置顶'''
        se = SeleniumBase(self.driver)
        screen_是置顶(se.driver)
        time.sleep(2)
        text = Page_Network_management(se.driver).find_number('是否置顶')
        asserts = len(set(text))
        try:
            self.assertEqual(1, asserts)
            self.assertIn('是', text)
            Page_Network_management(se.driver).click_是否置顶_全部()
        except Exception as e:
            Page_Network_management(se.driver).click_是否置顶_全部()
            raise e

    def test_06(self):
        '''否置顶'''
        se = SeleniumBase(self.driver)
        screen_否置顶(se.driver)
        time.sleep(2)
        text = Page_Network_management(se.driver).find_number('是否置顶')
        asserts = len(set(text))
        try:
            self.assertEqual(1, asserts)
            self.assertIn('否', text)
            Page_Network_management(se.driver).click_是否置顶_全部()
        except Exception as e:
            Page_Network_management(se.driver).click_是否置顶_全部()
            raise e

    def test_07(self):
        '''组合搜索1'''
        se = SeleniumBase(self.driver)
        screen_普通贴(se.driver)
        screen_否推荐(se.driver)
        screen_是置顶(se.driver)
        time.sleep(2)
        text = Page_Network_management(se.driver).find_number('帖子类型')
        text1 = Page_Network_management(se.driver).find_number('是否推荐')
        text2 = Page_Network_management(se.driver).find_number('是否置顶')
        asserts1 = len(set(text))
        asserts2 = len(set(text))
        asserts3 = len(set(text))
        try:
            self.assertEqual(1, asserts1)
            self.assertEqual(1, asserts2)
            self.assertEqual(1, asserts3)
            self.assertIn('普通帖', text)
            self.assertIn('否', text1)
            self.assertIn('是', text2)
            Page_Network_management(se.driver).click_帖子类型_全部()
            Page_Network_management(se.driver).click_是否推荐_全部()
            Page_Network_management(se.driver).click_是否置顶_全部()
        except Exception as e:
            Page_Network_management(se.driver).click_帖子类型_全部()
            Page_Network_management(se.driver).click_是否推荐_全部()
            Page_Network_management(se.driver).click_是否置顶_全部()
            raise e


@ddt.ddt
class Test_Post_label_management(unittest.TestCase):
    """
    这是圈子论坛模块----帖子标签管理的测试类
    """

    @classmethod
    def setUpClass(cls):
        """测试前"""
        cls.driver = SeleniumBase().get_web_driver()
        start_test(cls.driver, 1)
        pass

    @classmethod
    def tearDownClass(cls):
        """测试后"""
        SeleniumBase(cls.driver).quit()
        pass

    @ddt.unpack
    @ddt.data(*read_txt('Test_Data/Application/新建帖子标签.txt'))
    def test_01(self, content):
        '''帖子标签管理---新建帖子标签'''
        se = SeleniumBase(self.driver)
        new_新建帖子标签(se.driver, content)
        text = Page_Post_label_management(se.driver).get_返回结果()
        time.sleep(0.5)
        self.assertEqual('新增标签成功！', text)
