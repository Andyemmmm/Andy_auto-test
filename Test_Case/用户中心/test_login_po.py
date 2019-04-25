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
import unittest
import ddt
from selenium.webdriver.common.by import By

from Business.base_url import url_index
from Business.用户中心.task_登录业务 import lgoin, login_po
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.page_index import Page_Index
from Page_Object.page_login import Page_Login


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
        se.get(url_index)

        login_po(se.driver, username, password)

        if assert_type == "1":
            # logger().info("断言登录成功")
            # 断言出现您好字样
            text = Page_Index(se.driver).get_登录成功提示您好()
            self.assertIn("您好", text)
        elif assert_type == "2":
            # logger().info("断言用户名为空")
            text = Page_Login(se.driver).get_登录错误提示()
            self.assertEqual("请输入用户名", text)
        elif assert_type == "3":
            text = Page_Login(se.driver).get_登录错误提示()
            self.assertEqual("请输入密码", text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
