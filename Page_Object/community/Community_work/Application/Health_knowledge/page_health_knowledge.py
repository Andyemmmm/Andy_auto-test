#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/20 10:05
# @File     : page_health_knowledge.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_health_knowledge(SeleniumBase):
    """
    这是健康知识--列表页面
    """

    loc_新建健康知识 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button')
    loc_发布日期_全部 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[2]/div/div/div[1]/div[1]/input')
    loc_发布日期_今日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[3]/div/div/input')
    loc_发布日期_昨日 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[4]/div/div/div[1]/div[1]/input')
    loc_发布日期_本周 = (By.XPATH, '/html/body')
    loc_发布日期_本月 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[6]/div/button[1]/span')
    loc_发布者_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[6]/div/button[2]/span')
    loc_开始日期 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/input[1]')
    loc_结束日期 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/input[2]')
    loc_清空筛选条件 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/button/span')
    loc_新建成功 = (By.XPATH, '/html/body/div[3]/p')

    def send_开始日期(self, start_date):
        self.send_keys(self.loc_开始日期, start_date)
        return self

    def send_结束日期(self, end_date):
        self.send_png(self.loc_结束日期, end_date)
        return self

    def click_新建健康知识(self):
        self.click_element(self.loc_新建健康知识)
        return self

    def send_发布日期_全部(self):
        self.click_element(self.loc_发布日期_全部)
        return self

    def switch_发布日期_今日(self):
        self.click_element(self.loc_发布日期_今日)
        return self

    def send_发布日期_昨日(self):
        self.click_element(self.loc_发布日期_昨日)
        return self

    def click_发布日期_本周(self):
        self.click_element(self.loc_发布日期_本周)
        return self

    def click_发布日期_本月(self):
        self.click_element(self.loc_发布日期_本月)
        return self

    def click_发布者_全部(self):
        self.click_element(self.loc_发布者_全部)
        return self

    def click_清空筛选条件(self):
        self.click_element(self.loc_清空筛选条件)
        return self

    def get_上传成功(self):
        return self.get_element_text(self.loc_新建成功)
