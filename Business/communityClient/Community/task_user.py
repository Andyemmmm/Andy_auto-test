#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/17 14:15
# @File     : task_finance.py
# @Software : aiwen_uip

import time

from Page_Object.community.Community_work.finance.page_finance_management import Page_Finance_Management
from Page_Object.community.Community_work.user.page_user import Page_User_management, Page_label_management
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home


def New_label(driver, content):
    '''用户模块---标签管理---新建标签流程'''
    Page_Home(driver).click_用户()
    time.sleep(1)
    Page_User_management(driver).click_标签管理()
    time.sleep(1)
    Page_label_management(driver).click_新建标签().send_新建标签输入框(content).click_新建标签确定()
