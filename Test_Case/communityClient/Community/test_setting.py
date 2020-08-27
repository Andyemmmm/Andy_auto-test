import unittest
import ddt
import time

from Business.communityClient.Community.task_setting import Add_members, Remove_members, New_role, del_role
from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.Community_work.set.page_member_management import Page_Memberm_management
from Page_Object.community.Community_work.set.page_role_management import Page_role_management


@ddt.ddt
class Test_Add_members(unittest.TestCase):
    """
    这是设置模块---成员管理的测试类
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
    @ddt.data(*read_txt("Test_Data/Community/设置成员管理添加成员.txt"))
    def test_001(self, name, option, assert_type):
        '''
        成员管理---添加成员的测试用例
        '''

        se = SeleniumBase(self.driver)
        Add_members(se.driver, name, option)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言添加成员成功")
            text = Page_Memberm_management(se.driver).get_msg()
            self.assertEqual('添加成功', text)
        elif assert_type == "2":
            # logger().Info("断言不填写成员或不选择角色分配的返回结果")
            text = Page_Memberm_management(se.driver).get_msg()
            self.assertEqual('请选择添加员工,选择用户权限', text)
        elif assert_type == "3":
            text = Page_Memberm_management(se.driver).get_msg()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_Remove_members(unittest.TestCase):
    """
    这是设置模块---成员管理管理的测试类
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

    # @ddt.unpack  # 解包
    @ddt.data('1')
    def test_001(self, assert_type):
        '''
        成员管理---移除成员的测试用例
        '''

        se = SeleniumBase(self.driver)
        Remove_members(se.driver)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言添加成员成功")
            text = Page_Memberm_management(se.driver).get_msg()
            self.assertEqual('修改成功', text)
        elif assert_type == "2":
            # logger().Info("断言不填写成员或不选择角色分配的返回结果")
            text = Page_Memberm_management(se.driver).get_msg()
            self.assertEqual('请选择添加员工,选择用户权限', text)
        elif assert_type == "3":
            text = Page_Memberm_management(se.driver).get_msg()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_New_role(unittest.TestCase):
    """
    这是设置模块---角色管理的测试类
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
    @ddt.data(*read_txt('Test_Data/Community/设置角色管理新增角色.txt'))
    def test_001(self, name, describe, assert_type):
        '''
        角色管理---新建角色的测试用例
        '''

        se = SeleniumBase(self.driver)
        New_role(se.driver, name, describe)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言添加成员成功")
            text = Page_role_management(se.driver).get_msg()
            self.assertEqual('提交成功！', text)
        elif assert_type == "2":
            # logger().Info("断言不填写成员或不选择角色分配的返回结果")
            text = Page_role_management(se.driver).get_msg()
            self.assertEqual('请选择添加员工,选择用户权限', text)
        elif assert_type == "3":
            text = Page_role_management(se.driver).get_msg()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_Del_role(unittest.TestCase):
    """
    这是设置模块---角色管理的测试类
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

    # @ddt.unpack  # 解包
    @ddt.data('1')
    def test_001(self, assert_type):
        '''
        角色管理---删除角色的测试用例
        '''

        se = SeleniumBase(self.driver)
        del_role(se.driver)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言删除成员成功")
            text = Page_role_management(se.driver).get_msg()
            self.assertEqual('删除成功！', text)
        elif assert_type == "2":
            # logger().Info("断言不填写成员或不选择角色分配的返回结果")
            text = Page_role_management(se.driver).get_msg()
            self.assertEqual('请选择添加员工,选择用户权限', text)
        elif assert_type == "3":
            text = Page_role_management(se.driver).get_msg()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
