#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/19 10:05
# @File     : test_science_project.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.communityClient.Application.task_common import switch_H5, get_online_msg
from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Business.communityClient.Application.task_科普专题 import New_project, New_topic_category, Filter_paper, \
    Publish_project, Filter_paper_next, Management_of_special_articles
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.Community_work.Application.Science_project.page_Management_of_special_articles import \
    Page_Management_of_special_articles
from Page_Object.community.Community_work.Application.Science_project.page_Special_invitation_management import \
    Page_Filter_paper
from Page_Object.community.Community_work.Application.Science_project.page_Subject_classification_management import \
    Page_Subject_classification_management
from Page_Object.community.Community_work.Application.Science_project.page_invitation_topic import Page_Invitation_topic
from Page_Object.community.Community_work.Application.Science_project.page_science_management import \
    Page_Science_mangement


@ddt.ddt
class Test_New_Project_doctor(unittest.TestCase):
    """
    这是科普专题模块--邀约医生写专题的测试类
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
    @ddt.data(*read_txt("Test_Data/Application/新建专题.txt"))
    def test_001(self, name, about, start_date, start_time, end_date, end_time, nickname, niabout, png,
                 value, value1, num, number, assert_type):
        '''科普专题--专题管理--新建专题--邀约医生写专题的测试用例'''

        se = SeleniumBase(self.driver)
        New_project(se.driver, name, about, start_date, start_time, end_date, end_time, nickname, niabout,
                    png, value, value1, num, number)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言专题邀约新建成功")
            text = Page_Science_mangement(se.driver).get_专题邀约新建成功()
            self.assertEqual('专题邀约新建成功', text)
            # 发布文章流程
            text = Publish_project(se.driver)
            self.assertEqual(nickname, text)
            time.sleep(1)
            msg = get_online_msg(se.driver)
            if msg == '已上线':
                # 跳转到H5页面的流程
                switch_H5(se.driver, se)
                text = se.driver.find_element_by_xpath(
                    '//*[@id="__layout"]/div/section/div[6]/div[2]/ul/li[1]/a/p').text
                self.assertEqual(nickname, text)
            else:
                pass

        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Invitation_topic(se.driver).get_金币数不足提示()
            self.assertEqual(name, text)

        elif assert_type == "3":
            text = Page_Invitation_topic(se.driver).get_金币数()
            self.assertEqual(name, text)
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Application/新建专题分类.txt"))
    @unittest.skip('跳过')
    def test_002(self, name, assert_type):
        '''科普专题--专题管理--新建专题分类管理的测试用例'''

        se = SeleniumBase(self.driver)
        New_topic_category(se.driver, name)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_Subject_classification_management(se.driver).get_消息()
            self.assertEqual('新增标签成功', text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Subject_classification_management(se.driver).get_消息()
            self.assertEqual(name, text)
        elif assert_type == "3":
            text = Page_Subject_classification_management(se.driver).get_消息()
            self.assertEqual(name, text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_Filter_paper(unittest.TestCase):
    """
    这是科普专题模块的测试类
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

    # @ddt.unpack
    @ddt.data('1')
    def test_001(self, assert_type):
        '''科普专题--专题邀约管理--筛选文章的测试用例'''

        se = SeleniumBase(self.driver)
        title = Filter_paper(se.driver)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            text = Page_Filter_paper(se.driver).get_文章数量()
            self.assertEqual('1', text)
            text = Filter_paper_next(se.driver)
            time.sleep(1.5)
            text1 = Page_Filter_paper(se.driver).get_消息()
            self.assertEqual(title, text)
            self.assertEqual('采纳成功', text1)
            time.sleep(1)
            msg = get_online_msg(se.driver)
            if msg == '已上线':
                # 跳转到H5页面的流程
                switch_H5(se.driver, se)
                se.driver.find_element_by_xpath(
                    '//*[@id="__layout"]/div/section/div[6]/div[2]/ul/li[1]/a/div/img').click()
                text_h5 = se.driver.find_element_by_xpath(
                    '//*[@id="__layout"]/div/section/div[3]/div[2]/ul/li/a/div[1]/dl/dt').text
                self.assertEqual(title, text_h5)
            else:
                pass
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Filter_paper(se.driver).get_文章数量()
            self.assertEqual('1', text)
        elif assert_type == "3":
            text = Page_Filter_paper(se.driver).get_文章数量()
            self.assertEqual('1', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_Remove_the_projects(unittest.TestCase):
    """
    这是科普专题模块的测试类
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

    # @ddt.unpack
    @ddt.data('1')
    def test_001(self, assert_type):
        '''科普专题--专题文章管理--移出文章的测试用例'''

        se = SeleniumBase(self.driver)
        Management_of_special_articles(se.driver)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            text = Page_Management_of_special_articles(se.driver).get_消息()
            self.assertEqual('移出成功', text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Management_of_special_articles(se.driver).get_消息()
            self.assertEqual('1', text)
        elif assert_type == "3":
            text = Page_Management_of_special_articles(se.driver).get_消息()
            self.assertEqual('1', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
