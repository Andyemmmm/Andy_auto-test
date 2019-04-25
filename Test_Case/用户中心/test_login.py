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

from selenium import webdriver

from Business.base_url import url_index


class TestLogin(unittest.TestCase):
    def setUp(self):
        """测试前"""
        # 1、打开浏览器
        self.driver = webdriver.Chrome()
        pass

    def tearDown(self):
        """测试后"""
        # 8、关闭浏览器
        self.driver.quit()
        pass

    def test_login_成功(self):
        """登录成功的测试用例"""
        username = "liu01"
        password = "123456"
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
        # 7、{验证结果}
        # 断言出现您好字样
        text = self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/span[1]').text
        self.assertIn("您好", text)
        # 断言出现退出字样
        text = self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/span[3]/a').text
        self.assertEqual("退出", text)
        pass

    def test_login_用户名为空(self):
        """用户名为空的测试用例"""
        username = ""
        password = "123456"
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

        # 7、断言
        text = self.driver.find_element_by_class_name("msg-error").text
        self.assertEqual("请输入用户名", text)

    def test_login_用户名密码为空(self):
        """用户名密码都为空的测试用例"""
        username = ""
        password = ""
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

        # 7、断言
        text = self.driver.find_element_by_class_name("msg-error").text
        self.assertEqual("请输入用户名", text)

    def test_login_密码为空(self):
        """用户名密码都为空的测试用例"""
        username = "liu"
        password = ""
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

        # 7、断言
        text = self.driver.find_element_by_class_name("msg-error").text
        self.assertEqual("请输入密码", text)
