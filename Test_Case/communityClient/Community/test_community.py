import unittest
import ddt
import time

from Business.communityClient.Community.task_home_management import Home_management
from Business.communityClient.用户中心.task_登录业务 import login_po, start_test
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Business.base_url import C_client
from Page_Object.community.Community_work.community.page_community_management import Page_Community_management


@ddt.ddt
class Test_home_management(unittest.TestCase):
    """
    这是社区管理模块的测试类
    """

    def setUp(self):
        """测试前"""
        self.driver = SeleniumBase().get_web_driver()
        start_test(self.driver, 1, "5df303cabfe5230006187832")
        pass

    def tearDown(self):
        """测试后"""
        SeleniumBase(self.driver).quit()
        pass

    @ddt.unpack  # 解包
    @ddt.data(*read_txt("Test_Data/Community/首页管理.txt"))
    def test_001(self, title, title1, png, png1, title2, title3, classname, classname1, doctor,
                 doctor1, doctor2, title4, title5, title6, title7, assert_type):
        '''
        首页管理的测试用例
        '''

        se = SeleniumBase(self.driver)
        Home_management(se.driver, title, title1, png, png1, title2, title3, classname, classname1, doctor,
                        doctor1, doctor2, title4, title5, title6, title7)
        time.sleep(1)

        communityID = Page_Community_management(se.driver).get_社区ID()
        se.driver.get(f'{C_client}{communityID}')
        se.switch_to_window_url(communityID)
        if assert_type == "1":
            # logger().Info("断言登录成功")

            text = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[4]/div/div[2]/div[1]/ul/li/a/div[2]/h3').text
            self.assertEqual(title2, text)
            se.driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[4]/div/div[1]/ul/li[2]').click()
            text1 = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[4]/div/div[2]/div[2]/ul/li[1]/a/div[2]/h3').text
            self.assertEqual(title3, text1)
            text2 = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[5]/div[2]/ul[1]/li/a/div[2]/h3').text
            self.assertEqual(doctor, text2)
            text3 = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[5]/div[2]/ul[2]/li[1]/a/div[2]/h3/b').text
            self.assertEqual(doctor1, text3)
            text4 = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[5]/div[2]/ul[2]/li[2]/a/div[2]/h3/b').text
            self.assertEqual(doctor2, text4)
            text5 = se.driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[6]/div[2]/ul/li[1]/a/p').text
            self.assertEqual(title6, text5)
            text6 = se.driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[6]/div[2]/ul/li[2]/a/p').text
            self.assertEqual(text6, title7)
            text7 = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[7]/ul/li[1]/a/div/div[2]/div[1]').text
            self.assertEqual(text7, classname)
            text8 = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[7]/ul/li[2]/a/div/div[2]/div[1]').text
            self.assertEqual(text8, classname1)

            text9 = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[8]/div[2]/div/div[3]/div/a/dl/dt').text
            self.assertIn(title4, text9)
            text10 = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[8]/div[2]/div/div[4]/div/a/dl/dt').text
            self.assertIn(title5, text10)
            time.sleep(5)
            text11 = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[9]/ul/li[1]/a/div[1]/div[1]').text
            self.assertEqual(title, text11)
            text12 = se.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[9]/ul/li[2]/a/div[1]/div[1]').text
            self.assertEqual(text12, title1)

        # elif assert_type == "2":
        #     # logger().Info("断言为空")
        #     text = Page_Questionnaire_add(se.driver).get_错误提示()
        #     self.assertEqual('医院名称不能重复', text)
        # elif assert_type == "3":
        #     text = Page_Questionnaire_add(se.driver).get_错误提示()
        #     self.assertEqual('提交成功', text)
        # else:
        #     # 针对不存在对的断言类型预警
        #     se.logger.info("断言类型错误")
        #     raise ValueError(f"断言类型错误：{assert_type}")
