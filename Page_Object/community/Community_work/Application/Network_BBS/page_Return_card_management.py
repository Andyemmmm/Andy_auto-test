#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/25 10:43
# @File     : page_Return_card_management.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Return_card_management(SeleniumBase):
    '''
    这个是圈子论坛模块--回帖管理页面
    '''

    loc_删除按钮 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div[1]/button/span')
    loc_搜索框 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div[2]/div/div/input')

    loc_返回结果 = (By.XPATH, '/html/body/div[3]/p')

    loc_帖子状态_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[1]')
    loc_帖子状态_待审核 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[2]')
    loc_帖子状态_审核通过 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[3]')
    loc_帖子状态_审核不通过 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[4]')
    loc_帖子状态_已删除 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[5]')

    loc_清空筛选条件 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/button/span')

    def click_删除按钮(self):
        self.mouse_over_click(self.loc_删除按钮)
        return self

    def click_帖子状态_全部(self):
        self.click_element(self.loc_帖子状态_全部)
        return self

    def click_帖子状态_待审核(self):
        self.click_element(self.loc_帖子状态_待审核)
        return self

    def click_帖子状态_审核通过(self):
        self.click_element(self.loc_帖子状态_审核通过)
        return self

    def get_返回结果(self):
        return self.get_element_text(self.loc_返回结果)

    def send_搜索框(self, content):
        self.send_element_key(self.loc_搜索框, content)

    def click_帖子状态_审核不通过(self):
        self.click_element(self.loc_帖子状态_审核不通过)
        return self

    def click_帖子状态_已删除(self):
        self.click_element(self.loc_帖子状态_已删除)
        return self
