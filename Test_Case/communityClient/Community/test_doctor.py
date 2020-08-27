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

from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Business.communityClient.用户中心.task_邀请医生业务 import Doctor_invite, Lable_management
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.page_login import Page_Login
from Page_Object.community.Community_work.doctor.page_doctor import Page_Doctor, Page_Label_Management


@ddt.ddt
class TestDoctor(unittest.TestCase):
    """
    这是医生模块的测试类
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
    @ddt.data(*read_txt("Test_Data/doctor.txt"))
    def test_doctor_invite(self, name, phone, assert_type):
        """医生管理---邀请医生的测试用例
        :param name: 邀请医生名称
        :param phone: 邀请医生手机号
        :param assert_type: 断言类型
        :return:
        """
        se = SeleniumBase(self.driver)
        Doctor_invite(se.driver, name, phone)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_Doctor(se.driver).get_邀请成功()
            self.assertEqual("andy", text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Doctor(se.driver).get_邀请成功()
            self.assertEqual("请输入用户名", text)
        elif assert_type == "3":
            text = Page_Doctor(se.driver).get_邀请成功()
            self.assertEqual("请输入密码", text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_Lable_Management(unittest.TestCase):
    """
    这是医生模块的测试类
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
    @ddt.data(*read_txt("Test_Data/user.txt"))
    def test_001(self, name, assert_type):
        """标签管理--新建标签的测试用例
        :param name: 标签名
        :param assert_type: 断言类型
        :return:
        """
        se = SeleniumBase(self.driver)
        Lable_management(se.driver, name)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_Label_Management(se.driver).get_消息()
            self.assertEqual("新增成功", text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Label_Management(se.driver).get_消息()
            self.assertEqual("不能重复添加", text)
        elif assert_type == "3":
            text = Page_Label_Management(se.driver).get_消息()
            self.assertEqual("请输入密码", text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
