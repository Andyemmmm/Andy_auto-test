#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/6 15:57
# @File     : page_Management_of_popularization_invitation.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Management_of_popularization_invitation(SeleniumBase):
    '''
    这个是健康科普--科普邀约管理页面
    '''

    loc_文章邀约 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/a/button/span')
    loc_结束邀约 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button/span')
    loc_筛选 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[3]/div')
    loc_第一行筛选 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[13]/div/button')

    def click_文章邀约(self):
        self.click_element(self.loc_文章邀约)
        return self

    def click_结束邀约(self):
        self.send_keys(self.loc_结束邀约)
        return self

    def click_筛选(self):
        self.click_element(self.loc_筛选)
        return self

    def click_第一行筛选(self):
        self.click_element(self.loc_第一行筛选)
        return self
