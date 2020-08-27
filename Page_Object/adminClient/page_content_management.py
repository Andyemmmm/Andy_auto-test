#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 15:59
# @File     : content_management.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Content_Management(SeleniumBase):
    '''这个爱问大后台--内容管理--文章管理--医生文章页面'''
    loc_标题 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[3]/div')
    loc_文章状态 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[8]/div')
    loc_文章类型 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[7]/div')
    loc_医生姓名 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[5]/div')
    loc_查看 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[14]/div/button[1]')
    loc_删除 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[14]/div/button[2]')

    # loc_系统设置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[6]/div[2]/p[3]')
    # loc_内容管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[7]/div[2]/p[3]')
    # loc_频道管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[8]/div[2]/p[3]')
    # loc_iask运营管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[9]/div[2]/p[3]')
    loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    def get_列表第一行_标题(self):
        return self.get_element_text(self.loc_标题)

    def get_列表第一行_文章状态(self):
        return self.get_element_text(self.loc_文章状态)

    def get_列表第一行_文章类型(self):
        return self.get_element_text(self.loc_文章类型)

    def get_列表第一行_医生姓名(self):
        return self.get_element_text(self.loc_医生姓名)

    def click_查看(self):
        self.mouse_over_click(self.loc_查看)
        return self

    def click_删除(self):
        self.click_element(self.loc_删除)
        return self

    def get_消息(self):
        return self.get_element_text(self.loc_消息)


class Page_Article_Detail(SeleniumBase):
    '''这个爱问大后台--内容管理--文章管理--医生文章详情页面'''
    loc_标题 = (By.XPATH, '//div[2]/section/div/div/div/div[2]/div[1]')
    loc_文章内容 = (By.XPATH, '//*[@id="tab-articleInfo"]')
    loc_删除按钮 = (By.XPATH, '//div[3]/div[1]/button')
    loc_确定删除 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]')
    loc_取消删除 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')

    # loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    def get_标题(self):
        return self.get_element_text(self.loc_标题)

    def get_文章内容(self):
        return self.get_element_text(self.loc_文章内容)

    def click_删除(self):
        self.click_element(self.loc_删除按钮)
        return self

    def click_确定删除(self):
        self.click_element(self.loc_确定删除)
        return self
