#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/19 15:28
# @File     : page_user.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_User_management(SeleniumBase):
    '''
    这个是用户模块--用户管理页面
    '''

    loc_用户管理 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[1]/li/span')
    loc_标签管理 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[2]/li/span')
    loc_全部类型 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div/div/div/div[1]/div/div/input')
    loc_用户名称手机号输入框 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[2]/li/ul/div[1]/li/span')
    loc_搜索按键 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[2]/li/ul/div[2]/li/span')

    # loc_返回结果 = (By.XPATH, '/html/body/div[3]/p')
    #
    # loc_微博 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[3]/li/ul/div[1]/li/span')
    # loc_微信公众号 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[3]/li/ul/div[2]/li/span')
    # loc_广告配置 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[4]/li/span')
    #
    # loc_社区介绍 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[5]/li/span')
    # loc_社区信息_ID = (By.XPATH, "//span[text()='ID：']/following-sibling::span")
    # loc_社区上线信息 = (By.XPATH, '//div[1]/div[1]/div[1]/h1/div/span[1]')
    #
    # loc_修改 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div[1]/div[2]/button/span/span')

    def click_用户管理(self):
        self.mouse_over_click(self.loc_用户管理)
        return self

    def click_标签管理(self):
        self.mouse_over_click(self.loc_标签管理)
        return self

    def click_全部类型(self):
        self.mouse_over_click(self.loc_全部类型)
        return self

    def click_用户名称手机号输入框(self, phone):
        self.send_keys(self.loc_用户名称手机号输入框, phone)
        return self

    def click_搜索按键(self):
        self.mouse_over_click(self.loc_搜索按键)
        return self

    # def click_微博(self):
    #     self.mouse_over_click(self.loc_微博)
    #     return self
    #
    # def click_微信公众号(self):
    #     self.mouse_over_click(self.loc_微信公众号)
    #     return self
    #
    # def click_广告配置(self):
    #     self.mouse_over_click(self.loc_广告配置)
    #     return self
    #
    # def click_社区介绍(self):
    #     self.mouse_over_click(self.loc_社区介绍)
    #     return self
    #
    # def click_修改(self):
    #     self.click_element(self.loc_修改)
    #     return self
    #
    # def get_社区ID(self):
    #     return self.get_element_text(self.loc_社区信息_ID)
    #
    # def get_社区上线信息(self):
    #     return self.get_element_text(self.loc_社区上线信息)


class Page_label_management(SeleniumBase):
    '''用户模块---标签管理页面'''
    loc_新建标签 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/button/span')
    loc_搜索框 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div/div/div/input')
    loc_搜索按键 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div/div/div/div/button')
    loc_新建标签输入框 = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/input')
    loc_新建标签确定 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')
    loc_msg = (By.XPATH, 'html/body/div[3]/p')

    def click_新建标签(self):
        self.click_element(self.loc_新建标签)
        return self

    def click_搜索按键(self):
        self.click_element(self.loc_搜索按键)
        return self

    def send_搜索框(self, content):
        self.send_keys(self.loc_搜索框, content)
        return self

    def send_新建标签输入框(self, content):
        self.send_keys(self.loc_新建标签输入框, content)
        return self

    def click_新建标签确定(self):
        self.click_element(self.loc_新建标签确定)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)

