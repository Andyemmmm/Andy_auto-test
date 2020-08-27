#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/23 9:01
# @File     : test_doctor_class.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.communityClient.Application.task_doctor_class import New_Doctorclass
from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.Community_work.Application.doctor_class.page_doctor_class import Page_Doctor_class


@ddt.ddt
class Test_Doctor_class(unittest.TestCase):
    """
    这是医生课堂模块的测试类
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
    @ddt.data(*read_txt("Test_Data/Application/新建医生课堂.txt"))
    def test_doctor_class_new(self, title, about, video, cover, introduce, outline, name, header, photo,
                              survey, newname, phone, assert_type):
        '''
        新建医生课堂的测试用例
        '''

        se = SeleniumBase(self.driver)
        New_Doctorclass(se.driver, title, about, video, cover, introduce, outline, name, header, photo,
                        survey, newname, phone)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_Doctor_class(se.driver).get_新建成功()
            self.assertIn('成功', text)
        elif assert_type == "2":
            # logger().Info("断言为空")
            text = Page_Doctor_class(se.driver).get_新建成功()
            self.assertEqual('提交成功', text)
        elif assert_type == "3":
            text = Page_Doctor_class(se.driver).get_新建成功()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
