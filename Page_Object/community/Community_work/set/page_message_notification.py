#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/20 10:00
# @File     : page_message_notification.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Message_notification(SeleniumBase):
    '''
    这个是设置模块--消息通知页面
    '''

    loc_消息通知 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[1]/li/span')
    loc_成员管理 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[2]/li/span')
    loc_角色管理 = (By.XPATH, '//*[@id="app"]/section/aside/div[2]/ul/div[3]/li/span')

    def click_消息通知(self):
        self.mouse_over_click(self.loc_消息通知)
        return self

    def click_成员管理(self):
        self.mouse_over_click(self.loc_成员管理)
        return self

    def click_角色管理(self):
        self.mouse_over_click(self.loc_角色管理)
        return self
