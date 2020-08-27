#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 15:43
# @File     : task_login.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Business.base_url import admin_client
from Common.tools.rw_ini import read_config
from Page_Object.adminClient.page_login import Page_Login


def login_admin(driver, username, password):
    """登录业务流程"""
    driver.get(admin_client)
    Page_Login(driver).send_用户名(username).send_密码(password).click_登录按钮()


def start_test(driver):
    '''测试用例执行前登录的流程'''
    rc = read_config("Config/env.ini")
    username = rc.get("admin", "username")
    password = rc.get("admin", "password")
    login_admin(driver, username, password)
