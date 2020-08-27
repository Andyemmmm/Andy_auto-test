#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/31 18:02
# @File     : page_Subject_classification_management.py
# @Software : aiwen_ui

# !/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/31 17:31
# @File     : page_Special_invitation_management.py
# @Software : aiwen_ui

# !/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/31 17:15
# @File     : page_Management_of_special_articles.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Subject_classification_management(SeleniumBase):
    '''
    这个是社区--应用模块--科普专题--专题分类管理页面
    '''

    loc_新建专题分类 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button/span')
    loc_输入名称 = (
        By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/input')
    loc_输入名称_确定 = (
        By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')
    loc_输入名称_取消 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[1]/span')

    loc_消息 = (By.XPATH, '/html/body/div[3]')
    loc_列表第一行 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div')
    loc_搜索框 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div/div/div/input')

    def click_新建专题分类(self):
        self.click_element(self.loc_新建专题分类)
        return self

    def send_输入名称(self, name):
        self.send_keys(self.loc_输入名称, name)
        return self

    def click_输入名称_确定(self):
        self.click_element(self.loc_输入名称_确定)
        return self

    def click_输入名称_取消(self):
        self.click_element(self.loc_输入名称_取消)
        return self

    def get_消息(self):
        return self.get_element_text(self.loc_消息)

    def get_获取列表第一行(self):
        return self.get_element_text(self.loc_列表第一行)

    def send_搜索框(self):
        self.send_element_key(self.loc_搜索框)
        return self
