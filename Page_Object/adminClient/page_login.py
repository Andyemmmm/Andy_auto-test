#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 15:39
# @File     : page_login.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Login(SeleniumBase):
    '''这是爱问大后台的登陆页'''
    loc_user = (By.XPATH, '//*[@id="app"]/section/main/div/div/div/form/div[2]/div/div[1]/input')
    loc_password = (By.XPATH, '//*[@id="app"]/section/main/div/div/div/form/div[3]/div/div/input')
    loc_loginSubmit = (By.XPATH, '//*[@id="app"]/section/main/div/div/div/form/button')
    loc_msg_error = (By.XPATH, '/html/body/div[2]/p')

    def send_用户名(self, username):
        self.send_keys(self.loc_user, username)
        return self

    def send_密码(self, password):
        self.send_keys(self.loc_password, password)
        return self

    def click_登录按钮(self):
        self.mouse_over_click(self.loc_loginSubmit)
        return self

    def get_登录错误提示(self):
        return self.get_element_text(self.loc_msg_error)
