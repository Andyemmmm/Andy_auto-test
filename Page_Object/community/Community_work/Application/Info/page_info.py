#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/19 14:44
# @File     : page_info.py
# @Software : aiwen_ui
from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Info(SeleniumBase):
    """这是咨询公告的页面"""
    loc_新建咨询公告 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button')
    loc_发布日期_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[1]')
    loc_发布日期_今日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[2]')
    loc_发布日期_昨日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[3]')
    loc_发布日期_本周 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[4]')
    loc_发布日期_本月 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[5]')
    loc_发布者_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li')
    loc_清空筛选条件 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/button/span')
    loc_提交成功 = (By.XPATH, '/html/body/div[3]/p')

    def click_新建咨询公告(self):
        self.click_element(self.loc_新建咨询公告)

    def click_发布日期_全部(self):
        self.click_element(self.loc_发布日期_全部)

    def click_发布日期_今日(self):
        self.click_element(self.loc_发布日期_今日)

    def click_发布日期_昨日(self):
        self.click_element(self.loc_发布日期_昨日)

    def click_发布日期_本周(self):
        self.click_element(self.loc_发布日期_本周)

    def click_发布日期_本月(self):
        self.click_element(self.loc_发布日期_本月)

    def click_发布者_全部(self):
        self.click_element(self.loc_发布者_全部)

    def click_清空筛选条件(self):
        self.click_element(self.loc_清空筛选条件)

    def get_提交成功(self):
        return self.get_element_text(self.loc_提交成功)
