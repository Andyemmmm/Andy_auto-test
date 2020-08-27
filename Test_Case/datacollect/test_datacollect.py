#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/5/15 10:30
# @File     : test_datacollect.py
# @Software : aiwen_ui

import unittest
import time
import ddt
from Common.tools.domysql import Do_mysql
from HTMLReport import logger
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Common.datacollect.iw_data_collect import Iw_data_collect
from Page_Object.datacollect.iwask.iwask_home import Page_Iwask_Home
from Page_Object.datacollect.iwask.iwask_operationtopic import Page_Iwask_operationtopic
from Page_Object.datacollect.iwask.iwask_list import Page_Iwask_List
from Page_Object.datacollect.iwask.iwask_doctorInfo import Page_Iwask_doctorinfo
from Page_Object.datacollect.iwask.iwask_shareContent import Page_Iwask_shareContent


@ddt.ddt
class Test_datacollect(unittest.TestCase, Iw_data_collect):
    def setUp(self):
        self.logger = logger()
        self.logger.info('打开浏览器')
        self.driver = SeleniumBase().get_web_driver()
        self.logger.info("打开数据库")
        self.Do_mysql = Do_mysql()
        s = time.localtime()
        self.begin_date = time.strftime('%Y-%m-%d %H-%M-%S', s)
        self.logger.info(f'开始时间是：{self.begin_date}')

    def tearDown(self):
        self.logger.info('关闭数据库')
        self.Do_mysql.close()
        self.logger.info('关闭浏览器')
        SeleniumBase(self.driver).quit()

    @unittest.skip('跳过')
    @ddt.unpack
    @ddt.data(*read_txt('Test_Data/datacollect/remain_event.txt'))
    def test_remain(self, num=None, stay=None):
        '''
        停留事件的测试方法
        :param num: 停留的次数
        :param stay:   停留的时间
        :return:
        '''
        # 初始化数据
        if num:
            num = int(num)
        if stay:
            stay = int(stay)

        t = time.localtime()
        channel = time.strftime('%Y%m%d', t)
        home_url = f"{Page_Iwask_Home.url}channel=love{channel}"
        list_url = f"{Page_Iwask_List.url}channel=love{channel}"
        doctorinfo_url = f"{Page_Iwask_doctorinfo.url}channel=love{channel}"
        share_content = f"{Page_Iwask_shareContent.url}channel=love{channel}"
        operation_url = f"{Page_Iwask_operationtopic.url}channel=love{channel}"
        self.logger.info(f'配置了channel后的URL为：{home_url}')
        self.logger.info(f'配置了channel后的URL为：{list_url}')
        self.logger.info(f'配置了channel后的URL为：{doctorinfo_url}')
        self.logger.info(f'配置了channel后的URL为：{share_content}')
        self.logger.info(f'配置了channel后的URL为：{operation_url}')
        self.remain_event(home_url, num, stay)
        self.remain_event(list_url, num, stay)
        self.remain_event(doctorinfo_url, num, stay)
        self.remain_event(share_content, num, stay)
        self.remain_event(operation_url, num, stay)
        s = time.localtime()
        self.end_date = time.strftime('%Y-%m-%d %H-%M-%S', s)

        # 链接数据库

        result = self.Do_mysql.fetch_all(
            f"SELECT * from wenwo.t_basic_datadanalysis_data_point_{channel[0:2]}_{channel[4:6]}_{channel[6:8]} "
            f"WHERE channel_id='love{channel}' and create_time BETWEEN '{self.begin_date}' and '{self.end_date}'"
        )

        L = []
        for i in result:
            event_type = i.get("event_type")
            L.append(event_type)
        l = len(set(L))

        remain_num = len(result)
        event_type = result[0].get('event_type')
        stay_time = result[0].get('stay_time')

        self.logger.info(f'页面停留的次数：{remain_num} 次')
        self.logger.info(f'页面停留的时间是{stay_time}')
        self.logger.info(f'事件类型是：{event_type}     Tip：1 点击事件  2 停留事件')
        self.assertEqual(int(num * 5), remain_num)
        self.assertEqual(2, event_type)
        # 循环遍历event_type字段是否一致
        self.assertEqual(1, l)
        # if stay:
        #     self.assertEqual(int(stay * 1000), stay_time)

    @unittest.skip
    @ddt.unpack
    @ddt.data(*read_txt('Test_Data/datacollect/click_event.txt'))
    def test_click(self, num):
        '''
        点击事件的测试方法
        :param num: 点击的次数
        :return:
        '''
        # 初始化数据
        if num:
            num = int(num)

        t = time.localtime()
        channel = time.strftime('%Y%m%d', t)
        url = f"{Page_Iwask_Home.url}channel=test_love{channel}"
        self.logger.info(f'配置了channel后的URL为：{url}')
        self.driver.get(url)

        self.click_event_back(Page_Iwask_Home.loc_热门科室全部, num)
        self.click_event_back(Page_Iwask_Home.lco_热门科室_儿科, num)

        s = time.localtime()
        self.end_date = time.strftime('%Y-%m-%d %H-%M-%S', s)

        # 链接数据库

        result = self.Do_mysql.fetch_all(
            f"SELECT * from wenwo.t_basic_datadanalysis_data_point_{channel[0:2]}_{channel[4:6]}_{channel[6:8]} "
            f"WHERE channel_id='test_love{channel}'and event_type=1 and create_time BETWEEN '{self.begin_date}' and "
            f"'{self.end_date}'"
        )
        click_num = len(result)

        L = []
        for i in result:
            event_type = i.get("event_type")
            L.append(event_type)
        l = len(set(L))

        event_type = result[0].get('event_type')
        stay_time = result[0].get('stay_time')

        self.logger.info(f'按钮点击的次数：{click_num} 次')
        self.logger.info(f'事件类型是：{event_type}     Tip：1 点击事件  2 停留事件')
        self.assertEqual(int(num) * 2, click_num)
        self.assertEqual(1, event_type)
        # 循环遍历event_type字段是否一致
        self.assertEqual(1, l)
        self.assertEqual(0, stay_time)
