import unittest
import ddt
import time

from Business.communityClient.Community.task_finance import Gold_Deposits
from Business.communityClient.Application.task_common import switch_webpage
from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.Community_work.finance.page_finance_management import Page_Finance_Management


@ddt.ddt
class Test_Finance(unittest.TestCase):
    """
    这是财务模块的测试类
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
    @ddt.data(*read_txt("Test_Data/Community/金币充值.txt"))
    def test_001(self, num, assert_type):
        '''
        金币充值的测试用例
        '''

        se = SeleniumBase(self.driver)
        Gold_Deposits(se.driver, num)
        time.sleep(1)

        if assert_type == "1":
            # logger().Info("断言充值成功")
            text = Page_Finance_Management(se.driver).get_num()
            self.assertEqual(num, text)
            text = switch_webpage(se)
            self.assertEqual('确认充值成功', text)
        elif assert_type == "2":
            # logger().Info("断言为空")
            text = Page_Finance_Management(se.driver).get_error_msg()
            self.assertEqual('充值金额大于100,小于99999', text)
        elif assert_type == "3":
            text = Page_Finance_Management(se.driver).get_error_msg()
            self.assertEqual('提交成功', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
