import unittest
import ddt
import time

from Business.communityClient.Application.task_common import switch_H5
from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Business.communityClient.Application.task_健康科普 import New_article_invitation, New_article_TAB, Filter_paper, \
    Filter_paper_next
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.community.Community_work.Application.Health_science.page_science_classification_management import \
    Page_science_classification_management
from Page_Object.community.page_login import Page_Login
from Page_Object.community.Community_work.Application.Health_science.page_health_science import Page_Health_science
from Page_Object.community.Community_work.Application.Health_science.page_filter_paper import Page_Filter_paper


@ddt.ddt
class Test_New_articles_invite(unittest.TestCase):
    """
    这是健康科普模块的测试类
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
    @ddt.data(*read_txt("Test_Data/Application/新建文章邀约.txt"))
    # @unittest.skip('跳过')
    def test_001(self, name, about, start_date, start_time, end_date, end_time, value, value1, num,
                 number, assert_type):
        '''健康科普--科普管理--新建文章邀约的测试用例'''
        se = SeleniumBase(self.driver)
        New_article_invitation(se.driver, name, about, start_date, start_time, end_date, end_time, value,
                               value1, num, number)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            text = Page_Health_science(se.driver).get_发布成功()
            self.assertEqual(name, text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Login(se.driver).get_登录错误提示()
            self.assertEqual("请输入用户名", text)
        elif assert_type == "3":
            text = Page_Login(se.driver).get_登录错误提示()
            self.assertEqual("请输入密码", text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Application/新建文章标签.txt"))
    @unittest.skip('跳过')
    def test_002(self, name, assert_type):
        '''科普专题--专题管理--新建专题分类管理的测试用例'''

        se = SeleniumBase(self.driver)
        New_article_TAB(se.driver, name)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            # 断言出现用户昵称
            text = Page_science_classification_management(se.driver).get_消息()
            self.assertEqual('新增标签成功', text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_science_classification_management(se.driver).get_消息()
            self.assertEqual(name, text)
        elif assert_type == "3":
            text = Page_science_classification_management(se.driver).get_消息()
            self.assertEqual(name, text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")


@ddt.ddt
class Test_Filter_paper(unittest.TestCase):
    """
    这是健康科普模块的测试类
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

    # @ddt.unpack
    @ddt.data('1')
    def test_001(self, assert_type):
        '''健康科普--科普筛选--筛选文章的测试用例'''

        se = SeleniumBase(self.driver)
        title = Filter_paper(se.driver)
        time.sleep(1)
        if assert_type == "1":
            # logger().Info("断言登录成功")
            text = Page_Filter_paper(se.driver).get_文章数量()
            self.assertEqual('1', text)
        elif assert_type == "2":
            # logger().Info("断言用户名为空")
            text = Page_Filter_paper(se.driver).get_文章数量()
            self.assertEqual('1', text)
        elif assert_type == "3":
            text = Page_Filter_paper(se.driver).get_文章数量()
            self.assertEqual('1', text)
        else:
            # 针对不存在对的断言类型预警
            se.logger.info("断言类型错误")
            raise ValueError(f"断言类型错误：{assert_type}")
        text = Filter_paper_next(se.driver)
        time.sleep(1.5)
        text1 = Page_Filter_paper(se.driver).get_消息()
        self.assertEqual(title, text)
        self.assertEqual('采纳成功', text1)
        time.sleep(1)
        # 跳转到H5页面的流程
        # switch_H5(se.driver, se)
        # se.driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[6]/div[2]/ul/li[1]/a/div/img').click()
        # text_h5 = se.driver.find_element_by_xpath(
        #     '//*[@id="__layout"]/div/section/div[3]/div[2]/ul/li/a/div[1]/dl/dt').text
        # self.assertEqual(title, text_h5)
