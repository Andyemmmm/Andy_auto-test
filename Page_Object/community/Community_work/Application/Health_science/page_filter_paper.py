#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/6 16:21
# @File     : page_filter_paper.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Filter_paper(SeleniumBase):
    '''
    这个是健康科普--科普筛选页面
    '''

    loc_提交日期_全部 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[5]/ul/li[1]')
    loc_提交日期_今日 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[5]/ul/li[2]')
    loc_提交日期_昨日 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[5]/ul/li[3]')
    loc_提交日期_本周 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[5]/ul/li[4]')
    loc_提交日期_本月 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[5]/ul/li[5]')
    loc_清空筛选条件 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/button/span')
    loc_第一行 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div')
    loc_加入文章库 = (By.XPATH,
                 '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[10]/div/button[1]/span')
    loc_加入回收站 = (By.XPATH,
                 '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[10]/div/button[2]/span')
    loc_文章数量 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/span[1]/div[2]/sup')
    loc_文章图案 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/span[1]/div[2]/div')
    loc_文章选择区内容 = (By.XPATH, '//body/div[2]/div[2]/div/div[1]')
    loc_确定文章选择 = (By.XPATH, '//body/div[2]/div[3]/button[2]/span')
    loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    def click_提交日期_全部(self):
        self.click_element(self.loc_提交日期_全部)
        return self

    def click_提交日期今日(self):
        self.click_element(self.loc_提交日期_今日)
        return self

    def click_提交日期昨日(self):
        self.click_element(self.loc_提交日期_昨日)
        return self

    def click_提交日期本周(self):
        self.click_element(self.loc_提交日期_本周)
        return self

    def click_提交日期本月(self):
        self.click_element(self.loc_提交日期_本月)
        return self

    def click_清空筛选条件(self):
        self.click_element(self.loc_清空筛选条件)
        return self

    def click_加入文章库(self):
        self.click_element(self.loc_加入文章库)
        return self

    def click_加入回收站(self):
        self.click_element(self.loc_加入回收站)
        return self

    def get_文章数量(self):
        return self.get_element_text(self.loc_文章数量)

    def click_确定文章选择(self):
        self.click_element(self.loc_确定文章选择)
        return self

    def get_消息(self):
        return self.get_element_text(self.loc_消息)

    def get_文章选择区内容(self):
        return self.get_element_text(self.loc_文章选择区内容)

    def get_第一行内容(self):
        return self.get_element_text(self.loc_第一行)

    def click_文章筛选图标(self):
        self.click_element(self.loc_文章图案)
        return self

