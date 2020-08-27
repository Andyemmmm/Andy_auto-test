#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/20 10:00
# @File     : page_message_notification.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Memberm_management(SeleniumBase):
    '''
    这个是设置模块--成员管理页面
    '''

    loc_添加成员 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/button/span')
    loc_请选择 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div[1]/ul/li[1]')
    loc_社区管理员 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div[1]/ul/li[2]')
    loc_电话运营 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div[1]/ul/li[3]')
    loc_运营组 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div[1]/ul/li[4]')
    loc_管理员权限 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div[1]/ul/li[5]')
    loc_超级管理员 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div[1]/ul/li[6]')
    loc_编辑 = (By.XPATH, '//div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/div/button[1]')
    loc_移除 = (By.XPATH, '//div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/div/button[2]')
    loc_移除确定 = (By.XPATH, '//*/div[3]/div/div[3]/div/button[1]')
    loc_移除取消 = (By.XPATH, '//*/div[3]/div/div[3]/div/button[2]')

    loc_添加成员_搜索框 = (By.XPATH, "//div[5]/div/div[2]/div/div[3]/div/div/input")
    loc_搜索框_选项 = (By.XPATH, "//div[@role='region']//li[1]")
    loc_角色分配 = (By.XPATH, '//div[5]/div/div[2]/div/div[5]/div/div[1]/span/span/i')
    loc_添加成员确定 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[5]/div/div[3]/div/button[2]')
    loc_消息 = (By.XPATH, "//p[@class='el-message__content']")

    def click_添加成员(self):
        self.click_element(self.loc_添加成员)
        return self

    def click_请选择(self):
        self.click_element(self.loc_请选择)
        return self

    def click_社区管理员(self):
        self.click_element(self.loc_社区管理员)
        return self

    def click_电话运营(self):
        self.click_element(self.loc_电话运营)
        return self

    def click_运营组(self):
        self.click_element(self.loc_运营组)
        return self

    def click_管理员权限(self):
        self.click_element(self.loc_管理员权限)
        return self

    def click_超级管理员(self):
        self.click_element(self.loc_超级管理员)
        return self

    def click_编辑(self):
        self.click_element(self.loc_编辑)
        return self

    def click_移除(self):
        self.click_element(self.loc_移除)
        return self

    def send_添加成员搜索框(self, name):
        self.send_keys(self.loc_添加成员_搜索框, name)
        return self

    def click_搜索框选项(self):
        try:
            self.mouse_over_click(self.loc_搜索框_选项)
        except:
            pass
        return self

    def click_角色分配(self):
        self.click_element(self.loc_角色分配)
        return self

    def click_角色分配选项(self, option):
        try:
            self.driver.find_element_by_xpath(f"//div[@x-placement='bottom-start']//li/span[text()='{option}']").click()
        except:
            self.driver.find_element_by_xpath("//div[@x-placement='bottom-start']//li/span[text()='请选择']").click()
        return self

    def click_添加成员确定(self):
        self.click_element(self.loc_添加成员确定)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_消息)

    def click_移除确定(self):
        self.click_element(self.loc_移除确定)
        return self
