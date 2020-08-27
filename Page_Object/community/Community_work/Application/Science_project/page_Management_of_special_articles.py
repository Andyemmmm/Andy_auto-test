#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/31 17:15
# @File     : page_Management_of_special_articles.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Management_of_special_articles(SeleniumBase):
    '''
    这个是社区--应用模块--科普专题--专题文章管理页面
    '''

    loc_专题名称全部 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[1]')
    loc_发布日期全部 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[1]')
    loc_发布日期今日 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[2]')
    loc_发布日期昨日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[3]')
    loc_发布日期本周 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[4]')
    loc_发布日期本月 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[5]')

    loc_清空筛选条件 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/button/span')
    loc_成功 = (By.XPATH, '/html/body/div[2]/p')
    loc_列表第一行 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr/td[2]/div/a')
    loc_搜索框 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div/div/div/input')
    loc_移出专题 = (By.XPATH,
                '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td[10]/div/button/span')
    loc_确定移出 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')
    loc_取消移出 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[1]/span')
    loc_消息 = (By.XPATH, '/html/body/div[3]')

    def click_专题名称_全部(self):
        self.click_element(self.loc_专题名称全部)
        return self

    def click_发布日期_全部(self):
        self.click_element(self.loc_发布日期全部)
        return self

    def click_发布日期今日(self):
        self.click_element(self.loc_发布日期今日)
        return self

    def click_发布日期昨日(self):
        self.click_element(self.loc_发布日期昨日)
        return self

    def click_发布日期本周(self):
        self.click_element(self.loc_发布日期本周)
        return self

    def click_发布日期本月(self):
        self.click_element(self.loc_发布日期本月)
        return self

    def click_清空筛选条件(self):
        self.click_element(self.loc_清空筛选条件)

    def get_专题邀约新建成功(self):
        return self.get_element_text(self.loc_成功)

    def get_获取列表第一行(self):
        return self.get_element_text(self.loc_列表第一行)

    def send_搜索框(self):
        self.send_element_key(self.loc_搜索框)
        return self

    def click_移出专题(self):
        self.click_element(self.loc_移出专题)
        return self

    def click_确定移出(self):
        self.click_element(self.loc_确定移出)
        return self

    def click_取消移出(self):
        self.click_element(self.loc_取消移出)
        return self

    def get_消息(self):
        return self.get_element_text(self.loc_消息)
