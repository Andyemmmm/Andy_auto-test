#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/17 13:38
# @File     : page_finance_management.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Finance_Management(SeleniumBase):
    '''这个是社区--财务模块--财务管理页面'''
    loc_立即充值 = (By.XPATH, '//div[1]/div[1]/div/div/div[1]/div/span')
    loc_输入金币数 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div/div/div[1]/input')
    loc_msg_error = (By.XPATH, '//div[2]/div/div[2]/form/div/div/div[2]')
    loc_提交申请 = (By.XPATH, '//div[2]/div/div[3]/span/button[2]/span')
    loc_取消 = (By.XPATH, '//div[2]/div/div[3]/span/button[1]/span')
    loc_付款信息确定 = (By.XPATH, '//div[3]/div/div[3]/span/button')
    loc_num = (By.XPATH, '//div[3]/div/div[2]/p/span[2]/span[2]')

    loc_交易明细 = (By.XPATH, '//*[@id="tab-all"]')
    loc_充值申请 = (By.XPATH, '//*[@id="tab-invest"]')
    loc_交易时间_开始时间 = (By.XPATH, '//*[@id="pane-all"]/div[1]/div[1]/div/div/input[1]')
    loc_交易时间_结束时间 = (By.XPATH, '//*[@id="pane-all"]/div[1]/div[1]/div/div/input[2]')
    loc_交易对象名称 = (By.XPATH, '//*[@id="pane-all"]/div[1]/div[2]/div/div/input')
    loc_搜索 = (By.XPATH, '//*[@id="pane-all"]/div[1]/div[2]/div/button/span')

    # loc_设置 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[7]/li/span')

    def click_立即充值(self):
        self.click_element(self.loc_立即充值)
        return self

    def click_付款信息确定(self):
        self.click_element(self.loc_付款信息确定)
        return self

    def send_输入金币数(self, num):
        self.send_keys(self.loc_输入金币数, num)
        return self

    def click_取消(self):
        self.click_element(self.loc_取消)
        return self

    def click_提交申请(self):
        self.click_element(self.loc_提交申请)
        return self

    def get_num(self):
        return self.get_element_text(self.loc_num)

    def click_交易明细(self):
        self.click_element(self.loc_交易明细)
        return self

    def click_充值申请(self):
        self.click_element(self.loc_充值申请)
        return self

    def send_交易对象名称(self, name):
        self.send_keys(self.loc_交易对象名称, name)
        return self

    def send_交易时间_开始时间(self, time):
        self.send_keys(self.loc_交易时间_开始时间, time)
        return self

    def send_交易时间_结束时间(self, time):
        self.send_keys(self.loc_交易时间_结束时间, time)
        return self

    def click_搜索(self):
        self.click_element(self.loc_搜索)
        return self

    def get_error_msg(self):
        return self.get_element_text(self.loc_msg_error)
