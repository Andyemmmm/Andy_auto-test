#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/25 13:52
# @File     : community_management.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Community_management(SeleniumBase):
    '''
    这个是社区模块--社区管理页面
    '''

    loc_社区管理 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[1]/li/span')
    loc_首页管理 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[2]/li/ul/div[1]/li/span')
    loc_首页排序 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[2]/li/ul/div[2]/li/span')

    loc_返回结果 = (By.XPATH, '/html/body/div[3]/p')

    loc_微博 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[3]/li/ul/div[1]/li/span')
    loc_微信公众号 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[3]/li/ul/div[2]/li/span')
    loc_广告配置 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[4]/li/span')

    loc_社区介绍 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[5]/li/span')
    loc_社区信息_ID = (By.XPATH, "//span[text()='ID：']/following-sibling::span")
    loc_社区上线信息 = (By.XPATH, '//div[1]/div[1]/div[1]/h1/div/span[1]')

    loc_修改 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div[1]/div[2]/button/span/span')

    def click_社区管理(self):
        self.mouse_over_click(self.loc_社区管理)
        return self

    def click_首页管理(self):
        self.mouse_over_click(self.loc_首页管理)
        return self

    def click_首页排序(self):
        self.mouse_over_click(self.loc_首页排序)
        return self

    def click_微博(self):
        self.mouse_over_click(self.loc_微博)
        return self

    def click_微信公众号(self):
        self.mouse_over_click(self.loc_微信公众号)
        return self

    def click_广告配置(self):
        self.mouse_over_click(self.loc_广告配置)
        return self

    def click_社区介绍(self):
        self.mouse_over_click(self.loc_社区介绍)
        return self

    def click_修改(self):
        self.click_element(self.loc_修改)
        return self

    def get_社区ID(self):
        return self.get_element_text(self.loc_社区信息_ID)

    def get_社区上线信息(self):
        return self.get_element_text(self.loc_社区上线信息)
