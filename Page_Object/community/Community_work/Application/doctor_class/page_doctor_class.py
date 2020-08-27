#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/20 16:47
# @File     : page_doctor_class_download.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Doctor_class(SeleniumBase):
    '''
    这个是医生课堂--列表页面
    '''

    loc_新建 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button')
    loc_课程状态_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div/ul/li[1]')
    loc_课程状态_转码中 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div/ul/li[2]')
    loc_课程状态_已上线 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div/ul/li[3]')
    loc_课程状态_已下线 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div/ul/li[4]')
    loc_搜索框 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div/div/div/input')
    loc_新建成功 = (By.XPATH, '/html/body/div[3]/p')

    def click_新建(self):
        self.click_element(self.loc_新建)

    def click_课程状态_全部(self):
        self.click_element(self.loc_课程状态_全部)

    def click_课程状态_转码中(self):
        self.click_element(self.loc_课程状态_转码中)

    def click_课程状态_已上线(self):
        self.click_element(self.loc_课程状态_已上线)

    def click_课程状态_已下线(self):
        self.click_element(self.loc_课程状态_已下线)

    def click_搜索框(self):
        self.send_element_key(self.loc_搜索框)

    def get_新建成功(self):
        return self.get_element_text(self.loc_新建成功)
