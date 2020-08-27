#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/24 10:13
# @File     : task_questionnaire.py
# @Software : aiwen_ui

from Page_Object.community.Community_work.Application.questionnaire.page_questionnaire_add import Page_Questionnaire_add
from Page_Object.community.Community_work.Application.page_applicationMarket import Page_ApplicationMarket
from Page_Object.community.Community_work.Application.page_questionnaire_download import Page_Questionnaire_download
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Page_Object.community.Community_work.Application.page_myApplication import Page_MyApplication
from Page_Object.community.Community_work.Application.questionnaire.page_questionnaire import Page_Questionnaire
from Page_Object.community.Community_work.Application.questionnaire.page_Labeling_management import \
    Page_Labeling_management
import time


def New_Questionnaire(driver, title, describe, png, cover, remark, option1, option2, png1, option3, png2,
                      hint, body, content, name, nickname, hospital, major, url):
    '''新建调查问卷流程'''

    Page_Home(driver).click_应用()
    try:
        Page_MyApplication(driver).click_调查问卷()
    except:
        Download_application_questionnaire(driver)
        Page_MyApplication(driver).click_调查问卷()
    time.sleep(1)
    Page_Questionnaire(driver).click_新建问卷()
    Page_Questionnaire_add(driver).send_问卷标题(title).send_问卷描述(describe).send_问卷图片(png).send_问卷card封面(
        cover).click_问卷card封面_裁切确定().send_问卷备注(remark).click_组件_单选题().send_单选题_标题(title).send_单选题_内容1(
        option1).send_单选题_图片1(png).send_单选题_内容2(option2).send_单选题_图片2(png1).send_单选题_内容3(option3).send_单选题_图片3(
        png2)
    time.sleep(1)
    Page_Questionnaire_add(driver).click_组件_多选题().send_多选题_标题(title).send_多选题_内容1(option1).send_多选题_图片1(
        png).send_多选题_内容2(
        option2).send_多选题_图片2(png1).send_多选题_内容3(option3).send_多选题_图片3(png2)
    time.sleep(1)
    Page_Questionnaire_add(driver).click_组件_图片().send_图片上传(png).send_图片_描述(
        describe).click_组件_单行文本题().send_单行文本题_标题(title).send_单行文本题_描述(describe).send_单行文本题_图片(png).send_单行文本题_提示文字(
        hint).click_组件_多行文本题().send_多行文本题_标题(title).send_多行文本题_描述(describe).send_多行文本题_图片(png).send_多行文本题_提示文字(
        hint).click_组件_富文本().switch_富文本框().send_富文本内容(body).switch_back_frame().click_组件_提交().send_提交_文案(
        content).click_组件_图片_Card().send_图片_Card_文案(content).send_图片_Card_复制内容(
        content).click_组件_医生_Card().send_医生_Card_医生姓名(name).send_医生_Card_职称(nickname).send_医生_Card_医院(
        hospital).send_医生_Card_擅长(major).send_医生_Card_头像(cover).click_医生_Card_头像_裁切确定().send_医生_Card_URL(
        url).click_投放().click_投放确定()


def New_Labeling_management(driver, content):
    """新建标注的流程"""

    Page_Home(driver).click_应用()
    try:
        Page_MyApplication(driver).click_调查问卷()
    except:
        Download_application_questionnaire(driver)
        Page_MyApplication(driver).click_调查问卷()
    time.sleep(1)
    Page_Questionnaire(driver).click_标注管理()
    time.sleep(1)
    Page_Labeling_management(driver).click_新建问卷().send_弹框_输入标注(content).click_弹框_确定()


def Download_application_questionnaire(driver):
    """
    这个是下载应用的流程
    """
    Page_MyApplication(driver).click_应用市场()
    Page_ApplicationMarket(driver).click_调查问卷()
    Page_Questionnaire_download(driver).click_开通().click_确定开通()
    Page_MyApplication(driver).click_我的应用()
