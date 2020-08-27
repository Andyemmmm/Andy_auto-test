#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/23 14:26
# @File     : test_hospital.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.communityClient.Application.task_hospital import New_Hospital
from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.Community_work.Application.Hospital.page_hospital_recommend import Page_Hospital_recommend


@ddt.ddt
class Test_Hospital(unittest.TestCase):
    """
    这是医院推荐模块的测试类
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
    @ddt.data(*read_txt("Test_Data/Application/新建医院.txt"))
    def test_hospital_add(self, photo, name, about, mark, addre, introduce, remark, png, phone,
                          assert_type):
        '''
        新建医院的测试用例
        '''

        se = SeleniumBase(self.driver)
        New_Hospital(se.driver, photo, name, about, mark, addre, introduce, remark, png, phone)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_Hospital_recommend(se.driver).get_新建成功()
            self.assertIn('成功', text)
        elif assert_type == "2":
            # logger().Info("断言为空")
            text = Page_Hospital_recommend(se.driver).get_错误提示()
            self.assertEqual('医院名称不能重复', text)
        elif assert_type == "3":
            text = Page_Hospital_recommend(se.driver).get_错误提示()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
