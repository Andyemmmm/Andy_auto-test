#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/19 17:11
# @File     : task_咨询公告.py
# @Software : aiwen_ui
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Page_Object.community.Community_work.Application.page_myApplication import Page_MyApplication
from Page_Object.community.Community_work.Application.Info.page_info import Page_Info
from Page_Object.community.Community_work.Application.Info.page_information import Page_Information
import time


def New_Information(driver, title, cover, promulgator, photo, text):
    '''新建咨询公告流程'''

    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_咨询公告()
    time.sleep(2)
    Page_Info(driver).click_新建咨询公告()
    Page_Information(driver).send_标题(title).send_封面(cover).send_发布者(promulgator).send_发布者头像(
        photo).switch_富文本框().send_富文本框输入(text).switch_back_frame().click_确定()
