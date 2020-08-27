#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/3 17:21
# @File     : task_login.py
# @Software : aiwen_ui

from Business.base_url import doctor_Client
from Page_Object.doctorClient.PC.page_index import Page_Index
from Page_Object.doctorClient.PC.page_login import Page_Login


def login_doctor(driver, username, password):
    """登录业务流程"""
    driver.get(doctor_Client)
    # Page_Index(driver).click_登陆()
    Page_Login(driver).send_用户名(username).send_密码(password).click_登录按钮()
