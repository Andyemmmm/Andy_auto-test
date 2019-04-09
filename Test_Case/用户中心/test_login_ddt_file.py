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
from selenium import webdriver

from Business.base_url import url_index
from Common.tools.read_txt import read_txt


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        """测试前"""
        # 1、打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        pass

    def tearDown(self):
        """测试后"""
        # 8、关闭浏览器
        self.driver.quit()
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
        # username = "liu01"
        # password = "123456"
        # 2、输入网址
        self.driver.get(url_index)
        # 3、进入登录页
        self.driver.find_element_by_link_text("请登录").click()
        # 4、输入 {账号}
        self.driver.find_element_by_id("username").send_keys(username)
        # 5、输入密码
        self.driver.find_element_by_id("nloginpwd").send_keys(password)
        # 6、点击登录
        self.driver.find_element_by_id("loginSubmit").click()

        if assert_type == "1":
            # 断言出现您好字样
            text = self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/span[1]').text
            self.assertIn("您好", text)
            # 断言出现退出字样
            text = self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/span[3]/a').text
            self.assertEqual("退出", text)
        elif assert_type == "2":
            text = self.driver.find_element_by_class_name("msg-error").text
            self.assertEqual("请输入用户名", text)
        elif assert_type == "3":
            text = self.driver.find_element_by_class_name("msg-error").text
            self.assertEqual("请输入密码", text)
        else:
            # 针对不存在对的断言类型预警
            raise ValueError(f"断言类型错误：{assert_type}")
