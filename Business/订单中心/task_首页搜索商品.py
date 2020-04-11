#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/4/21 11:01
# @File     : task_首页搜索商品.py
# @Software : auto_web_ui_test

from Page_Object.page_index import Page_Index


def 首页开始搜索商品(driver, goods):
    Page_Index(driver).send_搜索商品(goods)
    Page_Index(driver).click_搜索商品按钮()
