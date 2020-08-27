#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/23 16:48
# @File     : page_questionnaire.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Questionnaire(SeleniumBase):
    '''
    这个是调查问卷模块--列表页面
    '''

    loc_新建问卷 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button/span')
    loc_创建日期_全部 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[1]')
    loc_创建日期_今日 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[2]')
    loc_创建日期_昨日 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]')
    loc_创建日期_本周 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]')
    loc_创建日期_本月 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[5]')
    loc_错误提示 = (By.XPATH, '/html/body/div[5]/p')
    loc_标注管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[2]')

    def click_新建问卷(self):
        self.mouse_over_click(self.loc_新建问卷)

    def click_课程状态_全部(self):
        self.click_element(self.loc_创建日期_全部)
        return

    def click_创建日期_今日(self):
        self.click_element(self.loc_创建日期_今日)
        return self

    def click_创建日期_昨日(self):
        self.click_element(self.loc_创建日期_昨日)
        return self

    def click_创建日期_本周(self):
        self.click_element(self.loc_创建日期_本周)
        return self

    def get_创建日期_本月(self):
        self.click_element(self.loc_创建日期_本月)
        return self

    def click_标注管理(self):
        self.click_element(self.loc_标注管理)
        return self
