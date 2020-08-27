#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/8 9:39
# @File     : page_articles_published.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Articles_published(SeleniumBase):
    '''这个文章发表的页面'''
    loc_诊间日记 = (By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[1]/a[1]')
    loc_健康科普 = (By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[1]/a[2]')
    loc_患者自述点评 = (By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[1]/a[3]')
    loc_病例分析 = (By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[1]/a[4]')

    def click_诊间日记(self):
        self.click_element(self.loc_诊间日记)
        return self

    def click_健康科普(self):
        self.click_element(self.loc_健康科普)
        return self

    def click_患者自述点评(self):
        self.click_element(self.loc_患者自述点评)
        return self

    def click_病例分析(self):
        self.click_element(self.loc_病例分析)
        return self
