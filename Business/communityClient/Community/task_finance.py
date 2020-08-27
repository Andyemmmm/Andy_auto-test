#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/17 14:15
# @File     : task_finance.py
# @Software : aiwen_ui

import time

from Page_Object.community.Community_work.finance.page_finance_management import Page_Finance_Management
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home


def Gold_Deposits(driver, num):
    '''财务模块---金币充值流程'''
    Page_Home(driver).click_财务()
    time.sleep(1)
    Page_Finance_Management(driver).click_立即充值().send_输入金币数(num).click_提交申请()
