#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/3 9:44
# @File     : page_index.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Index(SeleniumBase):
    '''这是医端的首页'''
    loc_登录 = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/a[2]')
    loc_医生账号注册 = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/a[1]')

    def click_登陆(self):
        self.logger.info("点击请登录")
        return self.click_element(self.loc_登录)

    def click_医生账号注册(self):
        self.click_element(self.loc_医生账号注册)
        return self
