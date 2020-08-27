#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/20 11:25
# @File     : task_health_knowledge.py
# @Software : aiwen_ui

from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Page_Object.community.Community_work.Application.page_doctor_class_download import Page_Doctor_class_download
from Page_Object.community.Community_work.Application.page_applicationMarket import Page_ApplicationMarket
from Page_Object.community.Community_work.Application.page_myApplication import Page_MyApplication
from Page_Object.community.Community_work.Application.Health_knowledge.page_health_knowledge import \
    Page_health_knowledge
from Page_Object.community.Community_work.Application.Health_knowledge.page_new_health_knowledge import \
    Page_new_health_knowledge
import time


def New_Health_knowledge(driver, title, cover, promulgator, photo, text):
    '''新建健康知识流程'''

    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_健康知识()
    time.sleep(1)
    Page_health_knowledge(driver).click_新建健康知识()
    Page_new_health_knowledge(driver).send_标题(title).send_封面(cover).send_发布者(promulgator).send_发布者头像(
        photo).switch_富文本框().send_富文本框输入(text).switch_back_frame().click_确定()


def Download_application(driver):
    """
    这个是下载应用的流程
    """
    Page_MyApplication(driver).click_应用市场()
    Page_ApplicationMarket(driver).click_医生课堂()
    Page_Doctor_class_download(driver).click_开通()
    time.sleep(2)
    Page_Doctor_class_download(driver).click_确定开通()
    Page_MyApplication(driver).click_我的应用()
