#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/24 15:42
# @File     : test_questionnaire.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.communityClient.Application.task_questionnaire import New_Questionnaire, New_Labeling_management
from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.Community_work.Application.questionnaire.page_Labeling_management import \
    Page_Labeling_management
from Page_Object.community.Community_work.Application.questionnaire.page_questionnaire_add import Page_Questionnaire_add


@ddt.ddt
class Test_Questionnaire(unittest.TestCase):
    """
    这是调查问卷模块的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        start_test(self.driver, 1)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Application/新建问卷调查.txt"))
    def test_questionnaire_add(self, title, describe, png, cover, remark, option1, option2, png1, option3,
                               png2, hint, body, content, name, nickname, hospital, major, url, assert_type):
        '''
        新建调查问卷的测试用例
        '''

        se = SeleniumBase(self.driver)
        New_Questionnaire(se.driver, title, describe, png, cover, remark, option1, option2, png1, option3,
                          png2, hint, body, content, name, nickname, hospital, major, url)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_Questionnaire_add(se.driver).get_投放成功()
            self.assertIn('投放成功', text)
        elif assert_type == "2":
            # logger().Info("断言为空")
            text = Page_Questionnaire_add(se.driver).get_错误提示()
            self.assertEqual('医院名称不能重复', text)
        elif assert_type == "3":
            text = Page_Questionnaire_add(se.driver).get_错误提示()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")

    @ddt.unpack
    @ddt.data(*read_txt('Test_Data/Application/新建标注.txt'))
    def test_labeling_management(self, content, expect):
        '''
        新建标注管理的测试用例
        '''

        se = SeleniumBase(self.driver)
        New_Labeling_management(se.driver, content)

        if expect == "成功":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_Labeling_management(se.driver).get_返回结果()
            self.assertIn(expect, text)
        elif expect == "已存在":
            # logger().Info("断言为空")
            text = Page_Labeling_management(se.driver).get_返回结果()
            self.assertIn(expect, text)
        elif expect == "3":
            text = Page_Labeling_management(se.driver).get_返回结果()
            self.assertEqual(expect, text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{expect}")
