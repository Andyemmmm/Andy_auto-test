#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/4/14 17:00
# @File     : task_注册业务.py
# @Software : auto_web_ui_test
from Page_Object.page_register import Page_Register


def register(driver,username,password,pwdRepeat,mobile_phone):
    '''注册业务流程'''
    rp=Page_Register(driver)
    rp.send_用户名(username).send_密码(password).send_确认密码(pwdRepeat).send_手机号码(mobile_phone).click_注册按钮()

