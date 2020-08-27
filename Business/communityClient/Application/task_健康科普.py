#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/17 17:11
# @File     : task_健康科普.py
# @Software : aiwen_ui
from Page_Object.community.Community_work.Application.Health_science.page_Management_of_popularization_invitation import \
    Page_Management_of_popularization_invitation
from Page_Object.community.Community_work.Application.Health_science.page_science_classification_management import \
    Page_science_classification_management
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Page_Object.community.Community_work.Application.page_myApplication import Page_MyApplication
from Page_Object.community.Community_work.Application.Health_science.page_health_science import Page_Health_science
from Page_Object.community.Community_work.Application.Health_science.page_filter_paper import Page_Filter_paper
from Page_Object.community.Community_work.Application.Health_science.page_new_health_science import \
    Page_new_Health_science
import time


def New_article_invitation(driver, name, about, start_date, start_time, end_date, end_time, value, value1,
                           num, number):
    '''科普管理--新建文章邀约流程'''

    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_健康科普()
    Page_Health_science(driver).click_新建文章邀约()
    Page_new_Health_science(driver).send_邀约名称(name).send_邀约简介(about).click_有效时间().send_开始日期(start_date).send_开始时间(
        start_time).click_开始时间确定().send_结束日期(end_date).send_结束时间(
        end_time).click_结束时间确定().click_有效时间确定().click_一级科室().mouse_一级科室_科室(value).click_二级科室().click_二级科室_科室(
        value1).click_选择标签().click_标签名称选项().click_全选科室().send_输入每篇奖励的金币数(
        num).send_输入需要手机的文章数(number).click_提交()


def New_article_TAB(driver, name):
    '''科普分类管理--新建文章标签'''
    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_健康科普()
    Page_Health_science(driver).click_科普分类管理()
    Page_science_classification_management(driver).click_新建专题标签().send_输入名称(name).click_输入名称_确定()


def Filter_paper(driver):
    '''专题邀约管理--筛选文章流程'''
    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_健康科普()
    time.sleep(1)
    Page_Health_science(driver).click_科普邀约管理()
    time.sleep(3)
    Page_Management_of_popularization_invitation(driver).click_第一行筛选()
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
