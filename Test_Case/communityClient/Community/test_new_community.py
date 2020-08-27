#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/29 10:02
# @File     : test_new_community.py
# @Software : aiwen_ui

import unittest
import ddt
import time

from Business.communityClient.用户中心.task_new_community import New_community_hospital, New_community_organization, \
    New_community_doctorteam, New_community_project, New_Test_community_hospital, New_Test_community_organization, \
    New_Test_community_doctorteam, New_Test_community_project
from Business.communityClient.用户中心.task_登录业务 import login_po
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.page_new_community import Page_success, Page_New_community
from Business.adminClient.task_login import start_test
from Business.adminClient.task_audit_management import Review_community
from Page_Object.adminClient.page_audit_management import Page_Community_qualification_audit


@ddt.ddt
class Test_New_community_hospital(unittest.TestCase):
    """
    这是社区B端---新建医院类型社区的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_po(self.driver, 17180654515, 123456)
        Page_CommunityList(self.driver).click_新建社区()

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/新建医院类型社区.txt"))
    def test_001(self, community_name, slogan, abbreviation, brief, png, option, disease, name, addr,
                 option1, option2, name1, png2, png3, name2, phone, assert_type, confirm=None):
        '''
        新建社区---新建医院类型社区的测试用例
        '''

        se = SeleniumBase(self.driver)
        time.sleep(1)
        Page_New_community(se.driver).click_社区(type='医院').click_next()
        time.sleep(2)
        text8 = New_community_hospital(se.driver, community_name, slogan, abbreviation, brief, png, option, disease,
                                       name, addr, option1, option2, name1, png2, png3, name2, phone, confirm)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言添加成员成功")
            text = Page_success(se.driver).get_msg()
            text1 = Page_success(se.driver).get_community_name()
            text2 = Page_success(se.driver).get_status()
            self.assertEqual('社区创建成功，您离社区品牌推广更近一步了', text)
            self.assertEqual(community_name, text1)
            self.assertEqual('未上线', text2)
        elif assert_type == "2":
            # logger().Info("断言社区名称已存在")
            self.assertEqual('社区名称已存在,请重新编辑', text8)
        elif assert_type == "3":
            # logger().Info("断言社区简称已存在")
            self.assertEqual('社区简称已被使用', text8)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_New_community_organization(unittest.TestCase):
    """
    这是社区B端---新建医院类型社区的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_po(self.driver, 17180654515, 123456)
        Page_CommunityList(self.driver).click_新建社区()

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/新建机构类型社区.txt"))
    def test_001(self, community_name, slogan, abbreviation, brief, png, option, disease, name,
                 addr, name1, png2, png3, name2, phone, assert_type):
        '''
        新建社区---新建机构类型社区的测试用例
        '''

        se = SeleniumBase(self.driver)
        time.sleep(1)
        Page_New_community(se.driver).click_社区(type='机构').click_next()
        time.sleep(2)
        text8 = New_community_organization(se.driver, community_name, slogan, abbreviation, brief, png, option, disease,
                                           name, addr, name1, png2, png3, name2, phone)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言添加成员成功")
            text = Page_success(se.driver).get_msg()
            text1 = Page_success(se.driver).get_community_name()
            text2 = Page_success(se.driver).get_status()
            self.assertEqual('社区创建成功，您离社区品牌推广更近一步了', text)
            self.assertEqual(community_name, text1)
            self.assertEqual('未上线', text2)
        elif assert_type == "2":
            # logger().Info("断言社区名称已存在")
            self.assertEqual('社区名称已存在,请重新编辑', text8)
        elif assert_type == "3":
            # logger().Info("断言社区简称已存在")
            self.assertEqual('社区简称已被使用', text8)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_New_community_doctorteam(unittest.TestCase):
    """
    这是社区B端---新建医生团队类型社区的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_po(self.driver, 17180654515, 123456)
        Page_CommunityList(self.driver).click_新建社区()

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/新建医生团队类型社区.txt"))
    def test_001(self, community_name, slogan, abbreviation, brief, png, option, disease, name,
                 name2, name3, png2, job, hospital, job2, job3, png3, assert_type, aiwen=None):
        '''
        新建社区---新建医生团队类型社区的测试用例
        '''
        se = SeleniumBase(self.driver)
        time.sleep(1)
        Page_New_community(se.driver).click_社区(type='医生团队').click_next()
        time.sleep(2)
        text8 = New_community_doctorteam(se.driver, community_name, slogan, abbreviation, brief, png, option, disease,
                                         name, name2, name3, png2, job, hospital, job2, job3, png3, aiwen)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言添加成员成功")
            text = Page_success(se.driver).get_msg()
            text1 = Page_success(se.driver).get_community_name()
            text2 = Page_success(se.driver).get_status()
            self.assertEqual('社区创建成功，您离社区品牌推广更近一步了', text)
            self.assertEqual(community_name, text1)
            self.assertEqual('未上线', text2)
        elif assert_type == "2":
            # logger().Info("断言社区名称已存在")
            self.assertEqual('社区名称已存在,请重新编辑', text8)
        elif assert_type == "3":
            # logger().Info("断言社区简称已存在")
            self.assertEqual('社区简称已被使用', text8)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_New_community_project(unittest.TestCase):
    """
    这是社区B端---新建项目型社区的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_po(self.driver, 17180654515, 123456)
        Page_CommunityList(self.driver).click_新建社区()

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/新建项目类型社区.txt"))
    def test_001(self, community_name, slogan, abbreviation, brief, png, option, disease, name, introduce, assert_type):
        '''
        新建社区---新建项目型社区的测试用例
        '''
        se = SeleniumBase(self.driver)
        time.sleep(1)
        Page_New_community(se.driver).click_社区(type='项目型社区').click_next()
        time.sleep(2)
        New_community_project(se.driver, community_name, slogan, abbreviation, brief, png, option, disease, name,
                              introduce)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言添加成员成功")
            text = Page_success(se.driver).get_msg()
            text1 = Page_success(se.driver).get_community_name()
            text2 = Page_success(se.driver).get_status()
            self.assertEqual('社区创建成功，您离社区品牌推广更近一步了', text)
            self.assertEqual(community_name, text1)
            self.assertEqual('未上线', text2)
        elif assert_type == "2":
            # logger().Info("断言社区名称已存在")
            text = Page_New_community(se.driver).get_msg()
            self.assertEqual('社区名称已存在,请重新编辑', text)
        elif assert_type == "3":
            # logger().Info("断言社区简称已存在")
            text = Page_New_community(se.driver).get_msg()
            self.assertEqual('社区简称已被使用', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


'''**************以下是新建测试类型的社区*******************************以下是新建测试类型的社区*******************************以下是新建测试类型的社区**********************'''


@ddt.ddt
class Test_New_Test_community_hospital(unittest.TestCase):
    """
    这是社区B端---新建测试类型的医院类型社区的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_po(self.driver, 17180654515, 123456)
        Page_CommunityList(self.driver).click_新建社区()

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/测试新建医院类型社区.txt"))
    def test_001(self, community_name, slogan, abbreviation, brief, png, option, disease, name, addr, option1, option2,
                 name1, png2, png3, name2, phone, assert_type, confirm=None):
        '''
        新建社区---新建测试类型的医院类型社区的测试用例
        '''

        se = SeleniumBase(self.driver)
        time.sleep(1)
        text8 = New_Test_community_hospital(se.driver, community_name, slogan, abbreviation, brief, png, option,
                                            disease, name, addr, option1, option2, name1, png2, png3, name2, phone,
                                            confirm)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言社区新建成功")
            text = Page_success(se.driver).get_msg()
            text1 = Page_success(se.driver).get_community_name()
            text2 = Page_success(se.driver).get_status()
            self.assertEqual('社区创建成功，您离社区品牌推广更近一步了', text)
            self.assertEqual(community_name, text1)
            self.assertEqual('未上线', text2)
        elif assert_type == "2":
            # logger().Info("断言社区名称已存在")
            self.assertEqual('社区名称已存在,请重新编辑', text8)
        elif assert_type == "3":
            # logger().Info("断言社区简称已存在")
            self.assertEqual('社区简称已被使用', text8)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_New_Test_community_organization(unittest.TestCase):
    """
    这是社区B端---新建测试类型的医院类型社区的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_po(self.driver, 17180654515, 123456)
        Page_CommunityList(self.driver).click_新建社区()

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/测试新建机构类型社区.txt"))
    def test_001(self, community_name, slogan, abbreviation, brief, png, option, disease, name,
                 addr, name1, png2, png3, name2, phone, assert_type):
        '''
        新建社区---新建测试类型的机构类型社区的测试用例
        '''

        se = SeleniumBase(self.driver)
        time.sleep(1)
        text8 = New_Test_community_organization(se.driver, community_name, slogan, abbreviation, brief, png, option,
                                                disease, name, addr, name1, png2, png3, name2, phone)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言添加成员成功")
            text = Page_success(se.driver).get_msg()
            text1 = Page_success(se.driver).get_community_name()
            text2 = Page_success(se.driver).get_status()
            self.assertEqual('社区创建成功，您离社区品牌推广更近一步了', text)
            self.assertEqual(community_name, text1)
            self.assertEqual('未上线', text2)
        elif assert_type == "2":
            # logger().Info("断言社区名称已存在")
            self.assertEqual('社区名称已存在,请重新编辑', text8)
        elif assert_type == "3":
            # logger().Info("断言社区简称已存在")
            self.assertEqual('社区简称已被使用', text8)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_New_Test_community_doctorteam(unittest.TestCase):
    """
    这是社区B端---新建测试类型的医生团队类型社区的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_po(self.driver, username=17180654515, password=123456)
        Page_CommunityList(self.driver).click_新建社区()

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/测试新建医生团队类型社区.txt"))
    def test_001(self, community_name, slogan, abbreviation, brief, png, option, disease, name,
                 name2, name3, png2, job, hospital, job2, job3, png3, assert_type, aiwen=None):
        '''
        新建社区---新建测试类型的医生团队类型社区的测试用例
        '''
        se = SeleniumBase(self.driver)
        time.sleep(1)
        text8 = New_Test_community_doctorteam(se.driver, community_name, slogan, abbreviation, brief, png, option,
                                              disease, name, name2, name3, png2, job, hospital, job2, job3, png3, aiwen)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言添加成员成功")
            text = Page_success(se.driver).get_msg()
            text1 = Page_success(se.driver).get_community_name()
            text2 = Page_success(se.driver).get_status()
            self.assertEqual('社区创建成功，您离社区品牌推广更近一步了', text)
            self.assertEqual(community_name, text1)
            self.assertEqual('未上线', text2)
        elif assert_type == "2":
            # logger().Info("断言社区名称已存在")
            self.assertEqual('社区名称已存在,请重新编辑', text8)
        elif assert_type == "3":
            # logger().Info("断言社区简称已存在")
            self.assertEqual('社区简称已被使用', text8)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_New_Test_community_project(unittest.TestCase):
    """
    这是社区B端---新建测试类型的项目型社区的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        login_po(self.driver, username=17180654515, password=123456)
        Page_CommunityList(self.driver).click_新建社区()

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/测试新建项目类型社区.txt"))
    def test_001(self, community_name, slogan, abbreviation, brief, png, option, disease, name, introduce, assert_type):
        '''
        新建社区---新建测试类型的项目型社区的测试用例
        '''
        se = SeleniumBase(self.driver)
        time.sleep(1)
        New_Test_community_project(se.driver, community_name, slogan, abbreviation, brief, png, option, disease, name,
                                   introduce)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言新建社区成功")
            text = Page_success(se.driver).get_msg()
            text1 = Page_success(se.driver).get_community_name()
            text2 = Page_success(se.driver).get_status()
            self.assertEqual('社区创建成功，您离社区品牌推广更近一步了', text)
            self.assertEqual(community_name, text1)
            self.assertEqual('未上线', text2)
        elif assert_type == "2":
            # logger().Info("断言社区名称重复")
            text = Page_New_community(se.driver).get_msg()
            self.assertEqual('社区名称已存在,请重新编辑', text)
        elif assert_type == "3":
            # logger().Info("断言社区简称已存在")
            text = Page_New_community(se.driver).get_msg()
            self.assertEqual('社区简称已被使用', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


'''**************以下是新建社区然后去爱问后台检查的测试用例*************************以下是新建社区然后去爱问后台检查的测试用例************************以下是新建社区然后去爱问后台检查的测试用例**********************'''


class Test_Review_community(unittest.TestCase):
    """
    这是审核管理--社区认证审核--社区通过审核的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        start_test(self.driver)
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    def test_001(self):
        '''审核管理---社区认证审核---审核社区'''

        se = SeleniumBase(self.driver)
        Review_community(se.driver)
        time.sleep(1)

        text = Page_Community_qualification_audit(se.driver).get_msg()
        self.assertEqual('操作成功', text)
