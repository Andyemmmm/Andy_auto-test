#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/23 13:47
# @File     : task_hospital.py
# @Software : aiwen_ui

from Page_Object.community.Community_work.Application.Hospital.page_hospital_add import Page_New_hospital
from Page_Object.community.Community_work.Application.page_applicationMarket import Page_ApplicationMarket
from Page_Object.community.Community_work.Application.page_hospital_download import Page_Hospital_download
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Page_Object.community.Community_work.Application.page_myApplication import Page_MyApplication
from Page_Object.community.Community_work.Application.Hospital.page_hospital_recommend import Page_Hospital_recommend
import time


def New_Hospital(driver, photo, name, about, mark, addre, introduce, remark, phone, png):
    '''新建医生课堂流程'''

    Page_Home(driver).click_应用()
    try:
        Page_MyApplication(driver).click_医院推荐()
    except:
        Download_application_hospital(driver)
        Page_MyApplication(driver).click_医院推荐()
    time.sleep(1)
    Page_Hospital_recommend(driver).click_新建()
    Page_New_hospital(driver).send_医院头像(photo).click_裁切头像确定().send_医院名称(name).send_医院简介(about).send_医院擅长(
        mark).click_医院地址().send_医院地址输入(addre)
    time.sleep(3)
    Page_New_hospital(driver).click_医院地址点击().click_医院地址确定().send_医院介绍(introduce).send_点评(remark).send_医院电话(
        phone).click_添加().send_医院图片(png).click_裁切图片确定().click_确定()


def Download_application_hospital(driver):
    """
    这个是下载应用的流程
    """
    Page_MyApplication(driver).click_应用市场()
    Page_ApplicationMarket(driver).click_医院推荐()
    Page_Hospital_download(driver).click_开通().click_确定开通()
    Page_MyApplication(driver).click_我的应用()
