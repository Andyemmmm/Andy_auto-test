#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/19 09:11
# @File     : task_科普专题.py
# @Software : aiwen_ui
from Page_Object.community.Community_work.Application.Science_project.page_Management_of_special_articles import \
    Page_Management_of_special_articles
from Page_Object.community.Community_work.Application.Science_project.page_Special_invitation_management import \
    Page_Special_invitation_management, Page_Filter_paper
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Page_Object.community.Community_work.Application.page_myApplication import Page_MyApplication
from Page_Object.community.Community_work.Application.Science_project.page_invitation_topic import Page_Invitation_topic
from Page_Object.community.Community_work.Application.Science_project.page_science_management import \
    Page_Science_mangement
from Page_Object.community.Community_work.Application.Science_project.page_Subject_classification_management import \
    Page_Subject_classification_management
import time


def New_project(driver, name, about, start_date, start_time, end_date, end_time, nickname, niabout, png,
                value, value1, num, number):
    '''专题管理--新建专题--邀约医生写专题流程'''

    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_科普专题()
    time.sleep(1)
    Page_Science_mangement(driver).click_新建专题().click_邀约医生写专题()
    Page_Invitation_topic(driver).send_邀约名称(name).send_邀约简介(
        about).click_有效时间().send_开始日期(start_date).send_开始时间(start_time).click_开始时间确定().send_结束日期(end_date).send_结束时间(
        end_time).click_结束时间确定().click_有效时间确定().send_专题名称(nickname).send_专题介绍(
        niabout).send_专题封面(png).click_一级科室().mouse_一级科室_科室(value).click_二级科室().click_二级科室_科室(
        value1).click_专题分类().click_专题分类_选项().click_全选科室().send_每篇奖励(num).send_要求数量(number).click_提交()


def Publish_project(driver):
    '''专题管理---发布文章流程'''
    Page_Science_mangement(driver).click_专题管理().click_专题状态待发布()
    time.sleep(0.5)
    text = Page_Science_mangement(driver).get_获取列表第一行()
    time.sleep(0.5)
    Page_Science_mangement(driver).click_第一行发布().click_发布确定()
    return text


def New_topic_category(driver, name):
    '''专题分类管理--新建专题分类流程'''
    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_科普专题()
    time.sleep(1)
    Page_Science_mangement(driver).click_专题分类管理()
    Page_Subject_classification_management(driver).click_新建专题分类().send_输入名称(name).click_输入名称_确定()


def Filter_paper(driver):
    '''专题邀约管理--筛选文章流程'''
    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_科普专题()
    time.sleep(1)
    Page_Science_mangement(driver).click_专题邀约管理()
    time.sleep(3)
    Page_Special_invitation_management(driver).click_列表第一行_筛选()
    time.sleep(3)
    text = Page_Filter_paper(driver).get_第一行内容()
    Page_Filter_paper(driver).click_加入文章库()
    return text


def Filter_paper_next(driver):
    '''专题邀约管理---筛选文章确定流程'''
    Page_Filter_paper(driver).click_文章筛选图标()
    time.sleep(0.5)
    text = Page_Filter_paper(driver).get_文章选择区内容()
    Page_Filter_paper(driver).click_确定文章选择()
    return text


def Management_of_special_articles(driver):
    '''专题文章管理--移出专题流程'''
    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_科普专题()
    time.sleep(1)
    Page_Science_mangement(driver).click_专题文章管理()
    time.sleep(1.5)
    Page_Management_of_special_articles(driver).click_移出专题().click_确定移出()
