#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/5/15 11:17
# @File     : iwask_operationtopic.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.datacollect.iw_data_collect import Iw_data_collect
import time


class Page_Iwask_operationtopic(Iw_data_collect):
    """聚合医疗平台运营专题页"""
    url = "https://health.sina.cn/zt/operationtopic/content?subjectId=5e796a2bb3cb1f0006f2ad33&"
    loc_第一个推荐医生卡片 = (By.XPATH, '//div[@class="doc_list_wrapper"]/div[1]//a[1]')
    loc_第一个推荐医生_去咨询 = (By.XPATH, '//div[@class="doc_list_wrapper"]/div[1]//a[2]')
