#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/3 16:17
# @File     : test_updatearticle.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.adminClient.task_content_management import article_view
from Business.adminClient.task_login import login_admin
from Business.doctorClient.task_login import login_doctor
from Business.doctorClient.task_updatearticle import Updatearticle, Updatearticle_Clinic_and_diary, \
    Updatearticle_case_analysis, Updatearticle_health
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.adminClient.page_content_management import Page_Content_Management
from Page_Object.doctorClient.PC.page_updatearticle import Page_UpdateArticle_success
from Page_Object.doctorClient.PC.page_updatearticle_Clinic_and_diary import Page_UpdateArticle_success_Clinic_and_diary


@ddt.ddt
class Test_Updatearticle(unittest.TestCase):
    """
    这是社区活动--新建文章的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_doctor(self.driver, username=15323751280, password=123456)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/doctorClient/社区活动新建文章.txt"))
    def test_001(self, content, title, png, assert_type):
        '''参与社区邀约活动的  新建文章的测试用例'''

        se = SeleniumBase(self.driver)
        Updatearticle(se.driver, content, title, png)
        time.sleep(1)
        if assert_type == "1":
            text = Page_UpdateArticle_success(se.driver).get_消息()
            text1 = Page_UpdateArticle_success(se.driver).get_文章名称()
            self.assertEqual('即时发布成功', text)
            self.assertEqual(title, text1)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_UpdateArticle_success(se.driver).get_消息()
            self.assertEqual(title, text)
        elif assert_type == "3":
            text = Page_UpdateArticle_success(se.driver).get_消息()
            self.assertEqual(title, text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_Updatearticle_health(unittest.TestCase):
    """
    这是新建健康科普文章的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_doctor(self.driver, username=15323751280, password=123456)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @unittest.skip('跳过')
    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/doctorClient/新建科普文章.txt"))
    def test_001(self, content, title, png, date, H, M, assert_type):
        ''' 新建健康科普文章的测试用例'''

        se = SeleniumBase(self.driver)
        Updatearticle_health(se.driver, content, title, png, date, H, M)
        time.sleep(1)
        if assert_type == "1":
            text = Page_UpdateArticle_success(se.driver).get_消息()
            text1 = Page_UpdateArticle_success(se.driver).get_文章名称()
            self.assertIn('发布', text)
            self.assertEqual(title, text1)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_UpdateArticle_success(se.driver).get_消息()
            self.assertEqual(title, text)
        elif assert_type == "3":
            text = Page_UpdateArticle_success(se.driver).get_消息()
            self.assertEqual(title, text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/doctorClient/新建科普文章.txt"))
    def test_002(self, content, title, png, date, H, M, assert_type):
        ''' 新建健康科普文章的测试用例--去爱问后台检查'''

        se = SeleniumBase(self.driver)
        Updatearticle_health(se.driver, content, title, png, date, H, M)
        time.sleep(1)
        login_admin(se.driver, 'tina', 111111)
        time.sleep(1)
        article_view(se.driver)
        if assert_type == "1":
            text = Page_Content_Management(se.driver).get_列表第一行_标题()
            text1 = Page_Content_Management(se.driver).get_列表第一行_文章状态()
            self.assertEqual(title, text)
            self.assertEqual('待发布', text1)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Content_Management(se.driver).get_列表第一行_标题()
            self.assertEqual(title, text)
        elif assert_type == "3":
            text = Page_Content_Management(se.driver).get_列表第一行_标题()
            self.assertEqual(title, text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_Updatearticle_Clinic_and_diary(unittest.TestCase):
    """
    这是写诊间日记文章的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_doctor(self.driver, username=13762106743, password=123456)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/doctorClient/新建诊间日记.txt"))
    def test_001(self, content, png, date, H, M, assert_type):
        '''写诊间日记文章的测试用例'''

        se = SeleniumBase(self.driver)
        Updatearticle_Clinic_and_diary(se.driver, content, png, date, H, M)
        time.sleep(1)
        if assert_type == "1":
            text = Page_UpdateArticle_success_Clinic_and_diary(se.driver).get_消息()
            self.assertEqual('授权发布', text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_UpdateArticle_success_Clinic_and_diary(se.driver).get_消息()
            self.assertEqual('', text)
        elif assert_type == "3":
            text = Page_UpdateArticle_success_Clinic_and_diary(se.driver).get_消息()
            self.assertEqual('', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_Updatearticle_case_analysis(unittest.TestCase):
    """
    这是写病例分析文章的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_doctor(self.driver, username=13762106743, password=123456)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/doctorClient/新建病例分析.txt"))
    def test_001(self, content, notes, title, png, date, H, M, assert_type, select=None):
        '''写病例分析文章的测试用例'''

        se = SeleniumBase(self.driver)
        Updatearticle_case_analysis(se.driver, content, notes, title, png, date, H, M, select)
        time.sleep(1)
        if assert_type == "1":
            text = Page_UpdateArticle_success_Clinic_and_diary(se.driver).get_消息()
            self.assertIn('发布', text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_UpdateArticle_success_Clinic_and_diary(se.driver).get_消息()
            self.assertEqual('', text)
        elif assert_type == "3":
            text = Page_UpdateArticle_success_Clinic_and_diary(se.driver).get_消息()
            self.assertEqual('', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
