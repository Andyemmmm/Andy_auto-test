#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/5/26 10:30
# @File     : test_iwask_home_click.py
# @Software : aiwen_ui

import unittest
import time
import ddt
from Common.tools.domysql import Do_mysql
from HTMLReport import logger
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.datacollect.iwask.iwask_home import Page_Iwask_Home
from Common.datacollect.iw_data_collect import Iw_data_collect


@ddt.ddt
class Test_iwask_home_click(unittest.TestCase, Iw_data_collect):
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
        url = f"{Page_Iwask_Home.url}channel=test_zrp{channel}"
        self.logger.info(f'配置了channel后的URL为：{url}')
        self.driver.get(url)

        self.click_event_back(Page_Iwask_Home.loc_热门科室全部, num)
        self.click_event_back(Page_Iwask_Home.lco_热门科室_儿科, num)
        self.click_event_back(Page_Iwask_Home.loc_热门科室_妇产科, num)
        self.click_event_back(Page_Iwask_Home.loc_热门科室_皮肤科, num)
        self.click_event_back(Page_Iwask_Home.loc_热门科室_消化内科, num)
        self.click_event_back(Page_Iwask_Home.loc_热门科室_口腔科, num)
        self.click_event_back(Page_Iwask_Home.loc_热门科室_泌尿外科, num)
        self.click_event_back(Page_Iwask_Home.loc_热门科室_骨科, num)
        self.click_event_back(Page_Iwask_Home.loc_热门科室_耳鼻咽喉科, num)
        self.click_event_back(Page_Iwask_Home.loc_banner, num)
        self.click_event_back(Page_Iwask_Home.loc_医生推荐全部, num)
        self.click_event_back(Page_Iwask_Home.loc_第一个医生卡片, num)
        self.click_event_back(Page_Iwask_Home.loc_第一个医生图文咨询按钮, num)
        print('**********================start====================***************')
        # self.driver.execute_script('window.scrollBy(0,5000)')  # 将页面纵向向下滚动1000像素
        # self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # 将页面的滚动条滑动到页面的最下方
        # self.ex_script(Page_Iwask_Home.loc_文章六)
        self.click_event_back(Page_Iwask_Home.loc_文章一, num)
        self.click_event_back(Page_Iwask_Home.loc_文章二, num)
        self.click_event_back(Page_Iwask_Home.loc_文章三, num)
        self.click_event_back(Page_Iwask_Home.loc_文章四, num)
        self.click_event_back(Page_Iwask_Home.loc_文章五, num)
        self.click_event_back(Page_Iwask_Home.loc_文章六, num)

        s = time.localtime()
        self.end_date = time.strftime('%Y-%m-%d %H-%M-%S', s)

        # 链接数据库

        result = self.Do_mysql.fetch_all(
            f"SELECT * from wenwo.t_basic_datadanalysis_data_point_{channel[0:2]}_{channel[4:6]}_{channel[6:8]} "
            f"WHERE channel_id='test_zrp{channel}'and event_type=1 and create_time BETWEEN '{self.begin_date}' and "
            f"'{self.end_date}'"
        )

        click_num = len(result)

        # L = []
        # for i in result:
        #     event_type = i.get("event_type")
        #     L.append(event_type)
        # l = len(set(L))

        event_type = result[0].get('event_type')
        stay_time = result[0].get('stay_time')

        self.logger.info(f'按钮点击的次数：{click_num} 次')
        self.logger.info(f'事件类型是：{event_type}     Tip：1 点击事件  2 停留事件')
        self.assertEqual(int(num) * 19, click_num)
        # self.assertEqual(num, click_num)
        self.assertEqual(1, event_type)
        # 循环遍历event_type字段是否一致
        # self.assertEqual(1, l)
        self.assertEqual(0, stay_time)
