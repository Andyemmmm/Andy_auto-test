#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/20 18:10
# @File     : task_doctor_class.py
# @Software : aiwen_ui

from Business.communityClient.Application.task_health_knowledge import Download_application
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Page_Object.community.Community_work.Application.page_myApplication import Page_MyApplication
from Page_Object.community.Community_work.Application.doctor_class.page_doctor_class import Page_Doctor_class
from Page_Object.community.Community_work.Application.doctor_class.page_new_doctor_class import Page_New_doctor_class
import time


def New_Doctorclass(driver, title, about, video, cover, introduce, outline, name, header, photo, survey,
                    newname, phone):
    '''新建医生课堂流程'''

    Page_Home(driver).click_应用()
    try:
        Page_MyApplication(driver).click_医生课堂()
    except:
        Download_application(driver)
        Page_MyApplication(driver).click_医生课堂()
    time.sleep(1)
    Page_Doctor_class(driver).click_新建()
    try:
        Page_New_doctor_class(driver).send_课程标题(title).send_课程简介(about).send_课程视频(video).send_课程封面(
            cover).click_课程封面裁切图片确定().switch_富文本框_介绍().send_课程介绍(
            introduce).switch_back_frame().switch_富文本框_大纲().send_课程大纲(
            outline).switch_back_frame().send_医生姓名(name).send_医生头衔(header).send_医生头像(
            photo).click_医生头像裁切图片确定().send_调查问卷(
            survey).click_新增().send_新增医生_姓名(newname).send_新增医生_手机号码(phone).click_新增医生_确定().click_确定()
    except:
        print('视频未加载完成，无法新增医生')
