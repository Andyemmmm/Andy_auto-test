#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/23 11:31
# @File     : page_hospital_add.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_New_hospital(SeleniumBase):
    '''
    这个是医院推荐--新建医院页面
    '''

    loc_医院头像 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[1]/div/div/div[1]/input')
    loc_裁切头像确定 = (By.XPATH, '/html/body/div[2]/div/div[3]/span/button[2]/span')
    loc_医院名称 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[2]/div/div/div[1]/input')
    loc_医院简介 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[3]/div/div/textarea')
    loc_医院擅长 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[4]/div/div/textarea')
    loc_医院地址 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[5]/div/div[1]/input')
    loc_医院地址输入 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/div[2]/div/div[1]/input')
    loc_医院地址点击 = (By.XPATH,
                  '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ol/li[1]/div/div[1]/span')
    loc_医院地址确定 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/div[3]/span/button[2]/span')
    loc_医院介绍 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[6]/div/div/textarea')
    loc_点评 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[7]/div/div/textarea')
    loc_医院电话 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[8]/div/div/div/input')
    loc_医院电话_添加 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[8]/div/div/button/span')
    loc_医院图片 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[10]/div/div/div[1]/ul/li/input')
    loc_裁切图片确定 = (By.XPATH, '/html/body/div[4]/div/div[3]/span/button[2]/span')
    loc_裁切图片取消 = (By.XPATH, '/html/body/div[4]/div/div[3]/span/button[1]/span')
    loc_确定 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[11]/div/button[1]/span')
    loc_取消 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/form/div[11]/div/button[2]/span')

    def click_医院地址点击(self):
        self.mouse_over_click(self.loc_医院地址点击)
        return self

    def send_医院地址输入(self, addre):
        self.send_keys(self.loc_医院地址输入, addre)
        return self

    def click_医院地址确定(self):
        self.click_element(self.loc_医院地址确定)
        return self

    def click_医院地址(self, ):
        self.click_element(self.loc_医院地址)
        return self

    def click_裁切头像确定(self):
        self.click_element(self.loc_裁切头像确定)
        return self

    def send_医院简介(self, about):
        self.send_keys(self.loc_医院简介, about)
        return self

    def send_点评(self, remark):
        self.send_keys(self.loc_点评, remark)
        return self

    def send_医院擅长(self, mark):
        self.send_keys(self.loc_医院擅长, mark)
        return self

    def send_医院介绍(self, introduce):
        self.send_keys(self.loc_医院介绍, introduce)
        return self

    def send_医院电话(self, phone):
        self.send_keys(self.loc_医院电话, phone)
        return self

    def send_医院名称(self, name):
        self.send_keys(self.loc_医院名称, name)
        return self

    def send_医院图片(self, png):
        self.send_keys(self.loc_医院图片, png)
        return self

    def send_医院头像(self, photo):
        self.send_keys(self.loc_医院头像, photo)
        return self

    def click_确定(self):
        self.mouse_over_click(self.loc_确定)
        return self

    def click_取消(self):
        self.click_element(self.loc_取消)
        return self

    def click_添加(self):
        self.mouse_over_click(self.loc_医院电话_添加)
        return self

    def click_裁切图片确定(self):
        self.click_element(self.loc_裁切图片确定)
        return self

    def click_裁切图片取消(self):
        self.click_element(self.loc_裁切图片取消)
        return self
