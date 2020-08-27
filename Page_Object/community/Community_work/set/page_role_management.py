# !/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/20 10:00
# @File     : page_message_notification.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_role_management(SeleniumBase):
    '''
    这个是设置模块---角色管理页面
    '''

    loc_新建角色 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/button[1]/span')
    loc_角色名称 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[1]/div/div/input')
    loc_角色描述 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[2]/div/div/textarea')
    loc_权限_首页 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[3]/div/div/div[1]/div/div[1]/div/span[2]')
    loc_权限_社区 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[3]/div/div/div[1]/div/div[2]/div/span[2]')
    loc_权限_医生 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[3]/div/div/div[1]/div/div[3]/div/span[2]')
    loc_权限_用户 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[3]/div/div/div[1]/div/div[4]/div/span[2]')
    loc_权限_财务 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[3]/div/div/div[1]/div/div[5]/div/span[2]')
    loc_权限_应用 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[3]/div/div/div[1]/div/div[6]/div/span[2]')
    loc_权限_设置 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[3]/div/div/div[1]/div/div[7]/div/span[2]')

    loc_删除 = (By.XPATH, '//div[2]/div/div[3]/table/tbody/tr[6]/td[5]/div/button[2]')
    loc_确定删除 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')

    loc_提交 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[4]/div/button[1]/span')
    loc_取消 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/form/div[4]/div/button[2]/span')
    loc_消息 = (By.XPATH, "//p[@class='el-message__content']")

    def click_新建角色(self):
        self.click_element(self.loc_新建角色)
        return self

    def send_角色名称(self, name):
        self.send_keys(self.loc_角色名称, name)
        return self

    def send_角色描述(self, describe):
        self.send_keys(self.loc_角色描述, describe)
        return self

    def click_权限首页(self):
        self.click_element(self.loc_权限_首页)
        return self

    def click_权限社区(self):
        self.click_element(self.loc_权限_社区)
        return self

    def click_权限医生(self):
        self.click_element(self.loc_权限_医生)
        return self

    def click_权限用户(self):
        self.click_element(self.loc_权限_用户)
        return self

    def click_权限财务(self):
        self.click_element(self.loc_权限_财务)
        return self

    def click_权限应用(self):
        self.click_element(self.loc_权限_应用)
        return self

    def click_权限设置(self):
        self.click_element(self.loc_权限_设置)
        return self

    def click_提交(self):
        self.click_element(self.loc_提交)
        return self

    def click_取消(self):
        self.click_element(self.loc_取消)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_消息)

    def click_删除(self):
        self.click_element(self.loc_删除)
        return self

    def click_确定删除(self):
        self.click_element(self.loc_确定删除)
        return self
