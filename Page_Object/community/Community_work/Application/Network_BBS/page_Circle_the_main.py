#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/25 10:55
# @File     : page_Circle_the_main.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Circle_the_main(SeleniumBase):
    '''
    这个是圈子论坛模块--圈主/医生设置页面
    '''

    loc_吧主管理_新增 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div[1]/div[1]/button[2]/span')
    loc_吧主管理_删除 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div[1]/div[1]/button[1]/span')
    loc_吧主管理_输入用户名id = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/div[2]/div/div[1]/input')

    loc_返回结果 = (By.XPATH, '/html/body/div[3]/p')

    loc_医生管理_新增 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[1]')
    loc_医生管理_删除 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[2]')

    # loc_帖子状态_审核通过 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[3]')
    # loc_帖子状态_审核不通过 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[4]')
    # loc_帖子状态_已删除 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div/ul/li[5]')
    #
    # loc_清空筛选条件 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/button/span')

    def click_吧主管理_新增(self):
        self.mouse_over_click(self.loc_吧主管理_新增)
        return self

    def click_吧主管理_删除(self):
        self.click_element(self.loc_吧主管理_删除)
        return self

    def send_吧主新增_输入用户名id(self):
        self.send_keys(self.loc_吧主管理_输入用户名id)
        return self

    def click_医生管理_新增(self):
        self.click_element(self.loc_医生管理_新增)
        return self

    def click_医生管理_删除(self):
        self.click_element(self.loc_医生管理_删除)
        return self
