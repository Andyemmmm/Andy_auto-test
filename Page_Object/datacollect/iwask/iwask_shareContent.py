#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/5/15 11:17
# @File     : iwask_shareContent.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.datacollect.iw_data_collect import Iw_data_collect
import time


class Page_Iwask_shareContent(Iw_data_collect):
    """聚合医疗平台套壳分享页"""
    url = "https://health.sina.cn/c/iwask/shareContent?id=47&"
    loc_第一个推荐医生卡片 = (By.XPATH, '//div[@class="doc_list_wrapper"]/div[1]//a[1]')
    loc_第一个推荐医生_去咨询 = (By.XPATH, '//div[@class="doc_list_wrapper"]/div[1]//a[2]')
    loc_share = (By.XPATH, '//p[text()="分享"]')
    loc_share_q = (By.XPATH, '//span[text()="确定"]')
    loc_医生推荐更多 = (By.XPATH, '//a[@class="more"]')
    loc_阅读全文 = (By.XPATH, '//span[text()="展开阅读全文"]')
