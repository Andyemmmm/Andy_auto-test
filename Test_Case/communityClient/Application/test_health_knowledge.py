#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/20 15:00
# @File     : test_health_knowledge.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Business.communityClient.Application.task_health_knowledge import New_Health_knowledge
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.Community_work.Application.Health_knowledge.page_health_knowledge import \
    Page_health_knowledge


@ddt.ddt
class Test_Health_knowledge(unittest.TestCase):
    """
    这是健康知识模块的测试类
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
    @ddt.data(*read_txt("Test_Data/Application/新建咨询公告.txt"))
    def test_health_knowledge(self, title, cover, promulgator, photo, text, assert_type):
        '''
        新建健康知识的测试用例
        '''

        se = SeleniumBase(self.driver)
        New_Health_knowledge(se.driver, title, cover, promulgator, photo, text)
        time.sleep(2)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_health_knowledge(se.driver).get_上传成功()
            self.assertEqual('提交成功', text)
        elif assert_type == "2":
            # logger().Info("断言为空")
            text = Page_health_knowledge(se.driver).get_上传成功()
            self.assertEqual('提交成功', text)
        elif assert_type == "3":
            text = Page_health_knowledge(se.driver).get_上传成功()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
