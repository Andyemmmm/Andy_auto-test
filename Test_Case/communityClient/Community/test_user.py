import unittest
import ddt
import time

from Business.communityClient.Community.task_user import New_label
from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.Community_work.user.page_user import Page_label_management


@ddt.ddt
class Test_New_label_management(unittest.TestCase):
    """
    这是用户模块的测试类
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
    @ddt.data(*read_txt("Test_Data/Community/用户新建标签管理.txt"))
    def test_001(self, content, assert_type):
        '''
        用户模块--标签管理---新建标签的测试用例
        '''

        se = SeleniumBase(self.driver)
        New_label(se.driver, content)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言新建成功")
            text = Page_label_management(se.driver).get_msg()
            self.assertEqual('新增成功', text)
        elif assert_type == "2":
            # logger().Info("断言为空")
            text = Page_label_management(se.driver).get_msg()
            self.assertEqual('不能重复添加', text)
        elif assert_type == "3":
            text = Page_label_management(se.driver).get_msg()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
