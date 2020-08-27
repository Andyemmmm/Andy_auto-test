#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/23 11:18
# @File     : page_hospital_recommend.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Hospital_recommend(SeleniumBase):
    '''
    这个是医院推荐模块--列表页面
    '''

    loc_新建 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div[1]/button/span')
    loc_按地区_全部省份 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/input')
    loc_按地区_选择城市 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/input')
    loc_按地区_选择地区 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[1]/input')
    loc_搜索框 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div[2]/div/input')
    loc_新建成功 = (By.XPATH, '/html/body/div[4]/p')
    loc_错误提示 = (By.XPATH, '/html/body/div[5]/p')

    def click_新建(self):
        self.click_element(self.loc_新建)

    def click_课程状态_全部(self):
        self.click_element(self.loc_按地区_全部省份)

    def click_课程状态_转码中(self):
        self.click_element(self.loc_按地区_选择城市)

    def click_课程状态_已上线(self):
        self.click_element(self.loc_按地区_选择地区)

    def click_搜索框(self):
        self.send_element_key(self.loc_搜索框)

    def get_新建成功(self):
        return self.get_element_text(self.loc_新建成功)

    def get_错误提示(self):
        return self.get_element_text(self.loc_错误提示)
