#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/25 8:40
# @File     : page_Labeling_management.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Labeling_management(SeleniumBase):
    '''
    这个是调查问卷模块--标注管理页面
    '''

    loc_新建标注 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/button/span')
    loc_弹框_输入标注 = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/input')
    loc_弹框_确定 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')
    loc_弹框_取消 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[1]/span')
    loc_返回结果 = (By.XPATH, '/html/body/div[3]/p')

    # loc_创建日期_本周 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]')
    # loc_创建日期_本月 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[5]')
    # loc_错误提示 = (By.XPATH, '/html/body/div[5]/p')

    def click_新建问卷(self):
        self.mouse_over_click(self.loc_新建标注)
        return self

    def send_弹框_输入标注(self, content):
        self.send_keys(self.loc_弹框_输入标注, content)
        return self

    def click_弹框_确定(self):
        self.click_element(self.loc_弹框_确定)
        return self

    def click_弹框_取消(self):
        self.click_element(self.loc_弹框_取消)
        return self

    def get_返回结果(self):
        return self.get_element_text(self.loc_返回结果)
