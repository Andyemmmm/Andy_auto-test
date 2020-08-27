#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/5/15 11:17
# @File     : iwask_doctorinfo.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.datacollect.iw_data_collect import Iw_data_collect
import time


class Page_Iwask_doctorinfo(Iw_data_collect):
    """聚合医疗平台医生详情页"""
    url = "https://health.sina.cn/c/iwask/doctorInfo?doctorId=1910178%20&source=1&"
    lco_图文咨询按钮 = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div[1]/div[4]')
    lco_去咨询 = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]')
