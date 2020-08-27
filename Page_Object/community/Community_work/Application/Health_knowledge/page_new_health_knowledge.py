#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/20 10:26
# @File     : page_new_health_knowledge.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_new_health_knowledge(SeleniumBase):
    """
    这是健康知识--新建健康知识页面
    """

    loc_标题 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[1]/div/div/input')
    loc_封面图片 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[2]/div/div/div[1]/div[1]/input')
    loc_发布者 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[3]/div/div/input')
    loc_发布者头像 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[4]/div/div/div[1]/div[1]/input')
    loc_富文本框输入 = (By.XPATH, '/html/body')
    loc_确定 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[6]/div/button[1]/span')
    loc_取消 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[6]/div/button[2]/span')
    loc_富文本框 = ('ueditor_0')

    def send_标题(self, title):
        self.send_keys(self.loc_标题, title)
        return self

    def send_封面(self, cover):
        self.send_png(self.loc_封面图片, cover)
        return self

    def send_发布者(self, promulgator):
        self.send_keys(self.loc_发布者, promulgator)
        return self

    def send_发布者头像(self, photo):
        self.send_png(self.loc_发布者头像, photo)
        return self

    def switch_富文本框(self):
        self.switch_to_frame(self.loc_富文本框)
        return self

    def send_富文本框输入(self, text):
        self.send_keys(self.loc_富文本框输入, text)
        return self

    def click_确定(self):
        self.click_element(self.loc_确定)
        return self

    def click_取消(self):
        self.click_element(self.loc_取消)
        return self
