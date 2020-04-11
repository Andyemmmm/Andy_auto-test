#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/4/21 10:57
# @File     : test_购物车.py
# @Software : auto_web_ui_test

import time
import unittest
import ddt
from Business.base_url import url_index
from Business.sync_user_data import acquire_user, release_user
from Business.用户中心.task_登录业务 import login_po
from Business.订单中心.task_首页搜索商品 import 首页开始搜索商品
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.page_goods import Page_Good
from Page_Object.page_index import Page_Index
from Page_Object.page_search import Page_Search


@ddt.ddt
class Test_购物车(unittest.TestCase):
    def setUp(self):
        # 获取用户
        self.user = acquire_user("Test_Data/user.txt")
        try:
            self.driver = SeleniumBase().get_web_driver()
        except Exception:
            # 如果打开浏览器失败，释放用户
            release_user()
            raise

    def tearDown(self):
        # 释放用户
        release_user()
        SeleniumBase(self.driver).quit()

    @ddt.unpack
    @ddt.data(*read_txt("Test_Data/商品列表"))
    def test_购物车(self, goods, assert_type):
        # 1、用户登录
        username, password = self.user

        se = SeleniumBase(self.driver)
        se.get(url_index)

        login_po(se.driver, username, password)

        page_index = Page_Index(self.driver)
        # 2、清空原有购物车
        page_index.click_移除购物车内所有商品()

        # 3、加入商品进入购物车
        首页开始搜索商品(self.driver, goods)
        Page_Search(self.driver).click_第一个商品()
        se.switch_to_window_url("goods.php")
        page_good = Page_Good(self.driver)
        text = page_good.get_价格()
        page_good.click_加入购物车()
        time.sleep(2)

        # 4、断言
        self.assertEqual(float(text), float(page_good.get_提示价格()[1:]))
        self.assertEqual("宝贝已成功添加到购物车！", page_good.get_加入购物车提示())
        self.assertEqual("1", page_good.get_加入购物车提示数量())
        pass
