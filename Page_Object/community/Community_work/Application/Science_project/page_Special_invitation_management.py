#!/usr/bin/python3
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


class Page_Special_invitation_management(SeleniumBase):
    '''
    这个是社区--应用模块--科普专题--专题邀约管理页面
    '''

    loc_新建邀约 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button[1]/span')
    loc_结束邀约 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button[2]/span')
    loc_邀约状态全部 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[1]')
    loc_邀约状态进行中 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[2]')
    loc_邀约状态已结束 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[3]')
    loc_专题科室全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[3]/ul/li')
    loc_专题分类全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/button/span')

    loc_邀约日期全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[5]/ul/li[1]')
    loc_邀约日期今日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[5]/ul/li[2]')
    loc_邀约日期昨日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[5]/ul/li[3]')
    loc_邀约日期本周 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[5]/ul/li[4]')
    loc_邀约日期本月 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[5]/ul/li[5]')

    loc_成功 = (By.XPATH, '/html/body/div[2]/p')
    loc_列表第一行 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div')
    loc_列表第一行_筛选 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[14]/div/a')
    loc_搜索框 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div/div/div/input')
    loc_清空筛选条件 = (By.XPATH,
                  '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/button/span')

    def click_专题名称_全部(self):
        self.click_element(self.loc_新建邀约)
        return self

    def click_结束邀约(self):
        self.click_element(self.loc_结束邀约)
        return self

    def click_邀约状态全部(self):
        self.click_element(self.loc_邀约状态全部)
        return self

    def click_邀约状态进行中(self):
        self.click_element(self.loc_邀约状态进行中)
        return self

    def click_邀约状态已结束(self):
        self.click_element(self.loc_邀约状态已结束)
        return self

    def click_专题科室全部(self):
        self.click_element(self.loc_专题科室全部)
        return self

    def click_专题分类全部(self):
        self.click_element(self.loc_专题分类全部)
        return self

    def click_邀约日期_全部(self):
        self.click_element(self.loc_邀约日期全部)
        return self

    def click_邀约日期今日(self):
        self.click_element(self.loc_邀约日期今日)
        return self

    def click_邀约日期昨日(self):
        self.click_element(self.loc_邀约日期昨日)
        return self

    def click_邀约日期本周(self):
        self.click_element(self.loc_邀约日期本周)
        return self

    def click_邀约日期本月(self):
        self.click_element(self.loc_邀约日期本月)
        return self

    def click_列表第一行_筛选(self):
        self.click_element(self.loc_列表第一行_筛选)
        return self

    def click_清空筛选条件(self):
        self.click_element(self.loc_清空筛选条件)
        return self

    def get_专题邀约新建成功(self):
        return self.get_element_text(self.loc_成功)

    def get_获取列表第一行(self):
        return self.get_element_text(self.loc_列表第一行)

    def send_搜索框(self):
        self.send_element_key(self.loc_搜索框)
        return self


class Page_Filter_paper(SeleniumBase):
    '''这是专题邀约管理---筛选文章页面'''

    loc_提交日期_全部 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/div/ul/li[1]')
    loc_提交日期_今日 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/div/ul/li[2]')
    loc_提交日期_昨日 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/div/ul/li[3]')
    loc_提交日期_本周 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/div/ul/li[4]')
    loc_提交日期_本月 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/div/ul/li[5]')
    loc_清空筛选条件 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/button/span')
    loc_第一行 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr/td[2]/div/div')
    loc_加入文章库 = (By.XPATH,
                 '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td[10]/div/button[1]/span')
    loc_加入回收站 = (By.XPATH,
                 '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td[10]/div/button[2]/span')
    loc_文章数量 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[3]/span[1]/div[2]/sup')
    loc_文章图案 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[3]/span[1]/div[2]/div')
    loc_文章选择区内容 = (By.XPATH, '//div[2]/div[2]/div/div[1]')
    loc_确定文章选择 = (By.XPATH, '//div[2]/div[3]/button[2]/span')
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
