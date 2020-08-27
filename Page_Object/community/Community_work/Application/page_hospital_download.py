#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/23 11:04
# @File     : page_hospital_download.py
# @Software : aiwen_ui


from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Hospital_download(SeleniumBase):
    '''
    这个是应用市场里面的医院推荐模块开通页面
    '''

    loc_开通确定 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')
    loc_开通 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div[1]/div[3]/button/span')

    def click_确定开通(self):
        self.click_element(self.loc_开通确定)
        return self

    def click_开通(self):
        self.click_element(self.loc_开通)
        return self
