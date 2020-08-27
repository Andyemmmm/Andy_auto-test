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
# from selenium import webdriver
# from HTMLReport import logger, AddImage
from selenium.webdriver.common.by import By

from Business.base_url import url_index
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        # 1、打开浏览器
        # self.driver = webdriver.Chrome()
        # logger().Info(f"打开浏览器：{self.driver.name}")
        # self.driver.maximize_window()
        # logger().Info("最大化浏览器")
        # self.driver.implicitly_wait(3)
        # logger().Info("设置隐式等待 3s")
        pass

    def tearDown(self):
        """测试后"""
        # 8、关闭浏览器
        # logger().Info("关闭浏览器")
        # self.driver.quit()
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
        # username = "liu01"
        # password = "123456"
        # 2、输入网址
        se.get(url_index)
        # self.driver.get(url_index)
        # logger().Info(f"输入网址：{url_index}")
        # 3、进入登录页
        se.click_element((By.LINK_TEXT, "请登录"))
        # logger().Info(f"进入登录页")
        # self.driver.find_element_by_link_text("请登录").click()
        # 4、输入 {账号}
        # self.driver.find_element_by_id("username").send_keys(username)
        se.logger.info(f"输入用户名：{username}")
        se.send_keys((By.ID, "username"), username)
        # 5、输入密码
        # self.driver.find_element_by_id("nloginpwd").send_keys(password)
        # logger().Info(f"输入密码：{password}")
        se.send_keys((By.ID, "nloginpwd"), password)
        # 添加截图
        # AddImage(self.driver.get_screenshot_as_base64())
        # 6、点击登录
        # self.driver.find_element_by_id("loginSubmit").click()
        # logger().Info("点击登录")
        se.click_element((By.ID, "loginSubmit"))
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现您好字样
            # text = self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/span[1]').text
            text = se.get_element_text((By.XPATH, '//*[@id="ECS_MEMBERZONE"]/span[1]'))
            self.assertIn("您好", text)
            # 断言出现退出字样
            # text = self.driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/span[3]/a').text
            text = se.get_element_text((By.XPATH, '//*[@id="ECS_MEMBERZONE"]/span[3]/a'))
            self.assertEqual("退出", text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            # text = self.driver.find_element_by_class_name("msg-error").text
            text = se.get_element_text((By.CLASS_NAME, "msg-error"))
            self.assertEqual("请输入用户名", text)
        elif assert_type == "3":
            # text = self.driver.find_element_by_class_name("msg-error").text
            text = se.get_element_text((By.CLASS_NAME, "msg-error"))
            self.assertEqual("请输入密码", text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
