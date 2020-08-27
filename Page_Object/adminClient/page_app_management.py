#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/11 17:05
# @File     : app_management.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Common.selenium_library import SeleniumBase


class Page_Home_configuration(SeleniumBase):
    '''这个是爱问大后台--APP管理--首页--首页管理页面'''
    lco_首页 = (By.XPATH, '//div[1]/ul/li[1]/div')
    loc_社区广场 = (By.XPATH, '//div[1]/ul/li[2]/div')
    loc_首页配置 = (By.XPATH, '//div/div[1]/ul/li[1]/ul/li/ul/li')
    loc_社区广场配置 = (By.XPATH, '//div/div[1]/ul/li[2]/ul/li/ul/li')
    loc_banner = (By.XPATH, '//section/div/div/div/div[2]')


class Page_Community_square(SeleniumBase):
    '''这个是爱问后台---APP管理---社区广场---社区广场配置'''
