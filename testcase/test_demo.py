#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/10/28 10:10
# @File     : test_demo.py
# @Software : Test_dental

import unittest
import time
from common.domysql import Do_mysql
from selenium import webdriver
from common import loging
import ddt
from common.read_txt import read_txt
from config.url import appointment

logger = loging.Log(__name__)


@ddt.ddt
class Test_demo(unittest.TestCase):
    def setUp(self):
        logger.info('打开浏览器')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(appointment)
        s = time.localtime()
        self.begin_date = time.strftime('%Y-%m-%d %H-%M-%S', s)
        logger.info(f'开始时间是：{self.begin_date}')
        self.Do_mysql = Do_mysql()

    def tearDown(self):
        logger.info('关闭数据库')
        self.Do_mysql.close()
        logger.info('关闭浏览器')
        self.driver.quit()

    @ddt.unpack
    @ddt.data(*read_txt('data/预约埋点点击次数.txt'))
    def test_city_addr(self, c,ip):
        '''
        此函数为点击城市功能次数的测试方法
        :param n: 点击的次数
        :return:
        '''
        time.sleep(8)
        n = int(c)
        for i in range(n):
            self.driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/div/div[1]/div[1]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[7]/div[2]/div/div[1]/span[1]').click()
            time.sleep(2)
        s = time.localtime()
        self.end_date = time.strftime('%Y-%m-%d %H-%M-%S', s)

        # 链接数据库
        result = self.Do_mysql.fetch_all(
            f"SELECT * from datacollection.t_basic_datadanalysis_data_point WHERE element_id=23 and create_time BETWEEN '{self.begin_date}' and '{self.end_date}' and ip='{ip}'")
        click_Num = len(result)
        element_ID = result[0].get('element_id')
        logger.info(f'当前时间是：{self.end_date}')
        logger.info(f'城市功能点击次数是：{click_Num} 次')
        logger.info(f'点击城市功能按钮元素的id是：{element_ID}')
        self.assertEqual(n, click_Num)
        self.assertEqual(23, element_ID)

    @ddt.unpack
    @ddt.data(*read_txt('data/预约埋点点击次数.txt'))
    def test_select_time(self, c,ip):
        '''
        此函数为点击选择日期的次数的测试方法
        :param n: 点击的次数
        :return:
        '''
        time.sleep(8)
        n = int(c)
        for i in range(n):
            self.driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/div/div[2]/div[1]/b').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[8]/div[1]').click()
            time.sleep(2)
        s = time.localtime()
        self.end_date = time.strftime('%Y-%m-%d %H-%M-%S', s)

        # 链接数据库
        result = self.Do_mysql.fetch_all(
            f"SELECT * from datacollection.t_basic_datadanalysis_data_point WHERE element_id=24 and create_time BETWEEN '{self.begin_date}' and '{self.end_date}' and ip='{ip}'")
        click_Num = len(result)
        element_ID = result[0].get('element_id')
        logger.info(f'当前时间是：{self.end_date}')
        logger.info(f'选择日期点击次数：{click_Num} 次')
        logger.info(f'点击选择日期按钮元素的id是：{element_ID}')
        self.assertEqual(n, click_Num)
        self.assertEqual(24, element_ID)

    @ddt.unpack
    @ddt.data(*read_txt('data/预约埋点点击次数.txt'))
    def test_select_project(self, c,ip):
        '''
        此函数为点击选择全部项目次数的测试方法
        :param n: 点击的次数
        :return:
        '''
        time.sleep(8)
        n = int(c)
        for i in range(n):
            self.driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/div/div[2]/div[2]/b').click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[6]/div[2]/div/div[1]/span[1]').click()
            time.sleep(1)
        s = time.localtime()
        self.end_date = time.strftime('%Y-%m-%d %H-%M-%S', s)

        # 链接数据库
        result = self.Do_mysql.fetch_all(
            f"SELECT * from datacollection.t_basic_datadanalysis_data_point WHERE element_id=25 and create_time BETWEEN '{self.begin_date}' and '{self.end_date}' and ip='{ip}'")
        click_Num = len(result)
        element_ID = result[0].get('element_id')
        logger.info(f'当前时间是：{self.end_date}')
        logger.info(f'选择全部项目的点击次数：{click_Num} 次')
        logger.info(f'点击选择全部项目按钮元素的id是：{element_ID}')
        self.assertEqual(n, click_Num)
        self.assertEqual(25, element_ID)

    @ddt.unpack
    @ddt.data(*read_txt('data/预约埋点点击次数.txt'))
    def test_doctor_order(self, c,ip):
        '''
        此函数为不同医生对应的预约点击次数的测试方法
        :param n: 点击次数
        :return:
        '''
        time.sleep(8)
        n = int(c)
        for i in range(n):
            self.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[2]/ul/li[1]/div[2]').click()  # 点击立即预约
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[8]/div[2]/div/div[3]/div').click()  # 点击确定按钮
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/div[5]/div[2]/div/div[3]/div[2]').click()  # 点击立即预约
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[5]/div[1]').click()  # 点击其它地方关闭弹窗
            time.sleep(1)
        s = time.localtime()
        self.end_date = time.strftime('%Y-%m-%d %H-%M-%S', s)

        # 链接数据库
        result = self.Do_mysql.fetch_all(
            f"SELECT * from datacollection.t_basic_datadanalysis_data_point WHERE element_id=18 and create_time BETWEEN '{self.begin_date}' and '{self.end_date}' and ip='{ip}'")
        result1 = self.Do_mysql.fetch_all(
            f"SELECT * from datacollection.t_basic_datadanalysis_data_point WHERE element_id=20 and create_time BETWEEN '{self.begin_date}' and '{self.end_date}' and ip='{ip}'")
        result2 = self.Do_mysql.fetch_all(
            f"SELECT * from datacollection.t_basic_datadanalysis_data_point WHERE element_id=21 and create_time BETWEEN '{self.begin_date}' and '{self.end_date}' and ip='{ip}'")

        logger.info(f'当前时间是：{self.end_date}')

        click_Num = len(result)
        element_ID = result[0].get('element_id')
        logger.info(f'点击医生的立即预约按钮次数是：{click_Num} 次')
        logger.info(f'点击医生的立即预约按钮元素的id是：{element_ID}')

        click_Num1=len(result1)
        element_ID1=result1[0].get('element_id')
        logger.info(f'点击确定按钮的次数是：{click_Num1} 次')
        logger.info(f'点击确定按钮元素的id是：{element_ID1}')

        click_Num2=len(result2)
        element_ID2=result2[0].get('element_id')
        logger.info(f'点击预约框里的立即预约按钮的次数是：{click_Num2} 次')
        logger.info(f'点击预约框里的立即预约按钮的元素id是：{element_ID2}')

        self.assertEqual(n, click_Num)
        self.assertEqual(18, element_ID)

        self.assertEqual(n,click_Num1)
        self.assertEqual(20,element_ID1)

        self.assertEqual(n,click_Num2)
        self.assertEqual(21,element_ID2)

