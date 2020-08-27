"""
1、打开浏览器
2、输入网址
3、进入登录页
4、输入{账号}
5、输入{密码}
6、点击登录
7、{验证结果}
8、关闭浏览器
"""
import time
import unittest
import ddt

from Business.communityClient.用户中心.task_登录业务 import login_po, loginout, start_test, login_code, experience_community
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.page_login import Page_Login
from Page_Object.community.page_communityList import Page_CommunityList


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/login_user_password.txt"))
    def test_login(self, username, password, assert_type):
        """登录的测试用例

        :param username: 用户名
        :param password: 密码
        :param assert_type: 断言类型：1-成功，2-用户名或用户名与密码都为空，3-密码为空
        :return:
        """
        se = SeleniumBase(self.driver)
        login_po(se.driver, username, password)
        time.sleep(1.5)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言登陆成功
            text = Page_CommunityList(se.driver).get_msg()
            self.assertEqual('登录成功', text)
        elif assert_type == "2":
            # logger().Info("断言密码错误")
            text = Page_Login(se.driver).get_msg()
            self.assertEqual("账号密码输入有误，请重新输入", text)
        elif assert_type == "3":
            text = Page_Login(se.driver).get_登录错误提示()
            self.assertEqual("密码不能为空", text)
        elif assert_type == "4":
            text = Page_Login(se.driver).get_登录错误提示()
            self.assertEqual("请输入11位手机号码", text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


class TestLogin_code(unittest.TestCase):
    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    def test_login_code(self):
        """登录的测试用例

        :param username: 用户名
        :param password: 密码
        :param assert_type: 断言类型：1-成功，2-用户名或用户名与密码都为空，3-密码为空
        :return:
        """

        se = SeleniumBase(self.driver)
        login_code(se.driver)
        time.sleep(1.5)
        text = Page_CommunityList(se.driver).get_msg()
        self.assertEqual('登录成功', text)


class Test_Loginout(unittest.TestCase):
    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        start_test(self.driver)

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    def test_loginout(self):
        """
        退出登录的测试用例
        """
        se = SeleniumBase(self.driver)
        loginout(se.driver)
        time.sleep(1.5)
        title = self.driver.title
        self.assertEqual('爱问医生-新浪健康(企业)-用户登录', title)


@ddt.ddt
class Test_experience_community(unittest.TestCase):
    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack
    @ddt.data(*read_txt("Test_Data/experience.txt"))
    def test_experience_community(self, name, phone, company=None):
        """
        申请体验社区的测试用例
        """
        se = SeleniumBase(self.driver)
        # Page_Login(se.driver).mouse_scan()
        experience_community(se.driver, name, phone, company)
        time.sleep(1.5)
        title = self.driver.title
        self.assertEqual('404提示信息', title)
