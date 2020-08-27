#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 15:47
# @File     : page_home.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Home(SeleniumBase):
    '''这个爱问大后台首页'''
    loc_会员管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[1]/div[2]/p')
    loc_社区管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[2]/div[2]/p')
    loc_APP管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[3]/div[2]/p')
    loc_审核管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[4]/div[2]/p')
    loc_运营支撑 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[5]/div[2]/p')
    loc_系统设置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[6]/div[2]/p')
    loc_内容管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[7]/div[2]/p')
    loc_频道管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[8]/div[2]/p')
    loc_iask运营管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[9]/div[2]/p')
    loc_接口应用设置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[10]/div[2]/p')
    loc_药店地图 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[11]/div[2]/p')
    loc_消息 = (By.XPATH, '/html/body/div[2]/p')

    def click_会员管理(self):
        self.click_element(self.loc_会员管理)
        return self

    def click_社区管理(self):
        self.click_element(self.loc_社区管理)
        return self

    def click_APP管理(self):
        self.click_element(self.loc_APP管理)
        return self

    def click_审核管理(self):
        self.click_element(self.loc_审核管理)
        return self

    def click_运营支撑(self):
        self.click_element(self.loc_运营支撑)
        return self

    def click_系统设置(self):
        self.click_element(self.loc_系统设置)
        return self

    def click_内容管理(self):
        self.mouse_over_click(self.loc_内容管理)
        return self

    def click_频道管理(self):
        self.click_element(self.loc_频道管理)
        return self

    def click_iask运营管理(self):
        self.click_element(self.loc_iask运营管理)
        return self

    def click_接口应用设置(self):
        self.click_element(self.loc_接口应用设置)
        return self

    def click_药店地图(self):
        self.click_element(self.loc_药店地图)
        return self

    def get_消息(self):
        return self.get_element_text(self.loc_消息)
