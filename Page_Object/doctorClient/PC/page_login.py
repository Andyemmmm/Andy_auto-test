#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/3 9:49
# @File     : page_login.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Login(SeleniumBase):
    '''这是医端的登陆页'''
    loc_phone = (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[1]/div/div[1]/input')
    loc_password = (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[1]/input')
    loc_loginSubmit = (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/button')
    loc_msg_error = (By.XPATH, '/html/body/div[3]/p')

    def send_用户名(self, username):
        self.send_keys(self.loc_phone, username)
        return self

    def send_密码(self, password):
        self.send_keys(self.loc_password, password)
        return self

    def click_登录按钮(self):
        self.click_element(self.loc_loginSubmit)
        return self

    def get_登录错误提示(self):
        return self.get_element_text(self.loc_msg_error)
