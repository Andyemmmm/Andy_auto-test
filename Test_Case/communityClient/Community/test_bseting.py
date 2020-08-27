import unittest
import ddt
import time
from Common.tools.rw_ini import write_config
from Business.communityClient.用户中心.task_bseting import organization_update_name, Add_members, \
    remove_members, update_personal, change_password
from Business.communityClient.用户中心.task_登录业务 import start_test
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.page_bseting import Page_Organization, Page_Staff_Management, Page_personal_data, \
    Page_security_settings


@ddt.ddt
class Test_organization_update_name(unittest.TestCase):
    """
    这是机构设置的测试类
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

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/更新机构名称.txt"))
    def test_001(self, name, assert_type):
        '''
        机构信息--机构设置---更新机构名称的测试用例
        '''

        se = SeleniumBase(self.driver)
        organization_update_name(se.driver, name)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言新建成功")
            text = Page_Organization(se.driver).get_msg()
            self.assertEqual('修改成功', text)
        elif assert_type == "2":
            # logger().Info("断言为空")
            text = Page_Organization(se.driver).get_err_msg()
            self.assertEqual('机构名称请以中英文开头', text)
        elif assert_type == "3":
            text = Page_Organization(se.driver).get_msg()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_Add_members(unittest.TestCase):
    """
    这是添加机构成员的测试类
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

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/添加机构成员.txt"))
    def test_001(self, phone, assert_type, phone1=None, phone2=None):
        '''
        机构信息--添加机构成员---添加员工的测试用例
        '''

        se = SeleniumBase(self.driver)
        Add_members(se.driver, phone, phone1, phone2)

        if assert_type == "1":
            time.sleep(2)
            # logger().Info("断言新建成功")
            text = Page_Staff_Management(se.driver).get_msg()
            self.assertIn('已成功发送', text)
        elif assert_type == "2":
            # logger().Info("断言为空")
            text = Page_Staff_Management(se.driver).get_err_msg()
            self.assertEqual('请输入正确的手机号码', text)
        elif assert_type == "3":
            text = Page_Staff_Management(se.driver).get_err_msg()
            self.assertEqual('已被邀请', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_remove_members(unittest.TestCase):
    """
    这是移除机构成员的测试类
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

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/机构移除员工.txt"))
    def test_001(self, phone, assert_type):
        '''
        机构信息--添加机构成员---移除员工的测试用例
        '''

        se = SeleniumBase(self.driver)
        remove_members(se.driver, phone)

        if assert_type == "1":
            time.sleep(1)
            # logger().Info("断言移除成功")
            text = Page_Staff_Management(se.driver).get_msg()
            self.assertEqual('移除成功!', text)
        elif assert_type == "2":
            # logger().Info("断言为空")
            text = Page_Staff_Management(se.driver).get_err_msg()
            self.assertEqual('请输入正确的手机号码', text)
        elif assert_type == "3":
            text = Page_Staff_Management(se.driver).get_err_msg()
            self.assertEqual('已被邀请', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_update_personal(unittest.TestCase):
    """
    这是更新个人信息的测试类
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

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/更新个人资料.txt"))
    def test_001(self, assert_type, name=None, head=None):
        '''
        用户信息--个人资料---更新个人信息的测试用例
        '''

        se = SeleniumBase(self.driver)
        update_personal(se.driver, name, head)

        if assert_type == "1":
            time.sleep(1)
            # logger().Info("断言保存成功")
            text = Page_personal_data(se.driver).get_msg()
            self.assertEqual('保存成功', text)
        elif assert_type == "2":
            # logger().Info("断言输入错误")
            text = Page_personal_data(se.driver).get_err_msg()
            self.assertEqual('输入错误,少于20位的中英文数字._的名称,英文中文开头', text)
        elif assert_type == "3":
            text = Page_personal_data(se.driver).get_err_msg()
            self.assertEqual('已被邀请', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_change_password(unittest.TestCase):
    """
    这是安全设置修改密码的测试类
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

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/修改密码.txt"))
    def test_001(self, password, newpassword, pwd, assert_type):
        '''
        用户信息--安全设置---修改密码的测试用例
        '''

        se = SeleniumBase(self.driver)
        change_password(se.driver, password, newpassword, pwd)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言保存成功")
            text = Page_security_settings(se.driver).get_msg()
            self.assertEqual('修改密码成功!', text)
            write_config("Config/env.ini", "default", "password", pwd)
        elif assert_type == "2":
            # logger().Info("断言旧密码错误")
            text = Page_security_settings(se.driver).get_msg()
            self.assertEqual('旧密码错误', text)
        elif assert_type == "3":
            text = Page_security_settings(se.driver).get_err_msg()
            self.assertEqual('请输入旧密码', text)
        elif assert_type == '4':
            text = Page_security_settings(se.driver).get_err_msg()
            self.assertEqual('请输入密码', text)
        elif assert_type == '5':
            text = Page_security_settings(se.driver).get_err_msg()
            self.assertEqual('请再次输入密码', text)
        elif assert_type == '6':
            text = Page_security_settings(se.driver).get_err_msg()
            self.assertEqual('两次输入密码不一致!', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
