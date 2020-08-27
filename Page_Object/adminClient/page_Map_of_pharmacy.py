#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/16 15:50
# @File     : page_Map_of_pharmacy.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Common.selenium_library import SeleniumBase


class Page_Doctor_information_management(SeleniumBase):
    '''爱问后台---药店地图---医生信息管理页面'''
    loc_医生信息管理 = (By.XPATH, '//div/div[1]/div/div/div/div[1]/ul/li/ul/li/ul/li[1]')
    loc_优惠券统计 = (By.XPATH, '//div/div[1]/div/div/div/div[1]/ul/li/ul/li/ul/li[2]')
    loc_用户绑定明细 = (By.XPATH, '//div/div[1]/div/div/div/div[1]/ul/li/ul/li/ul/li[3]')
    loc_标签管理 = (By.XPATH, '//div/div[1]/div/div/div/div[1]/ul/li/ul/li/ul/li[4]')
    loc_医生名称输入框 = (By.XPATH, "//label[text()='医生名称：']/following-sibling::div//input")
    loc_医生ID = (By.XPATH, "//label[text()='医生ID：']/following-sibling::div//input")
    loc_时间输入框_开始 = (By.XPATH, '//input[@placeholder="开始日期"]')
    loc_时间输入框_结束 = (By.XPATH, '//input[@placeholder="结束日期"]')
    loc_医院名称 = (By.XPATH, "//label[text()='医院名称：']/following-sibling::div//input")
    loc_科室 = (By.XPATH, "//label[text()='科室：']/following-sibling::div//input")


class Page_Coupon_statistics(SeleniumBase):
    '''爱问后台---药店地图---优惠券统计页面'''


class Page_User_binding_details(SeleniumBase):
    '''爱问后台---药店地图---用户绑定明细页面'''


class Page_label_management(SeleniumBase):
    '''爱问后台---药店地图---标签管理页面'''
