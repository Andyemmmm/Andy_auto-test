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
import time
from Business.doctorClient.task_login import login_doctor
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.doctorClient.PC.page_login import Page_Login
from Page_Object.doctorClient.PC.page_home import Page_Home


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
    @ddt.data(*read_txt("Test_Data/doctorClient_login.txt"))
    def test_login(self, username, password, assert_type):
        """登录的测试用例

        :param username: 用户名
        :param password: 密码
        :param assert_type: 断言类型：1-成功，2-用户名或用户名与密码都为空，3-密码为空
        :return:
        """
        se = SeleniumBase(self.driver)
        login_doctor(se.driver, username, password)
        time.sleep(1.5)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_Home(se.driver).get_信息()
            self.assertEqual('首页', text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Login(se.driver).get_登录错误提示()
            self.assertEqual("密码错误", text)
        elif assert_type == "3":
            text = Page_Login(se.driver).get_登录错误提示()
            self.assertEqual("密码错误", text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
