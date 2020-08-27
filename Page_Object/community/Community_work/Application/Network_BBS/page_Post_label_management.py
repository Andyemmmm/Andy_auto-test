#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/25 11:02
# @File     : page_Post_label_management.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Post_label_management(SeleniumBase):
    '''
    这个是圈子论坛模块--帖子标签管理页面
    '''

    loc_新建帖子标签 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button/span')
    loc_新增标签_输入内容 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div//div/div[2]/div/input')
    loc_新建帖子标签_确定 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div//div/div[3]/span/button[2]')
    loc_新建帖子标签_取消 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div//div/div[3]/span/button[1]')
    loc_搜索框 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div/div/div/input')
    loc_列表第一条数据 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[2]/div')

    loc_返回结果 = (By.XPATH, "//p[contains(text(),'新增标签成功')]")

    # loc_帖子状态_审核通过 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[3]')
    # loc_帖子状态_审核不通过 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[4]')
    # loc_帖子状态_已删除 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[5]')
    #
    # loc_清空筛选条件 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/button/span')

    def click_新建帖子标签(self):
        self.mouse_over_click(self.loc_新建帖子标签)
        return self

    def send_新增标签_输入内容(self, content):
        self.send_keys(self.loc_新增标签_输入内容, content)
        return self

    def click_新建帖子标签_确定(self):
        self.mouse_over_click(self.loc_新建帖子标签_确定)
        return self

    def click_新建帖子标签_取消(self):
        self.mouse_over_click(self.loc_新建帖子标签_取消)
        return self

    def send_搜索框(self, value):
        self.send_element_key(self.loc_搜索框, value)
        return self

    def get_返回结果(self):
        return self.get_element_text(self.loc_返回结果)

    def get_列表第一条数据(self):
        return self.get_element_text(self.loc_列表第一条数据)
