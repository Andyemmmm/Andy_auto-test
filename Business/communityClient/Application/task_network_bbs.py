#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/27 16:06
# @File     : task_network_bbs.py
# @Software : aiwen_ui

from Page_Object.community.Community_work.Application.Network_BBS.page_Network_management import Page_Network_management
from Page_Object.community.Community_work.Application.Network_BBS.page_Circle_the_main import Page_Circle_the_main
from Page_Object.community.Community_work.Application.Network_BBS.page_Post_label_management import \
    Page_Post_label_management
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Page_Object.community.Community_work.Application.page_myApplication import Page_MyApplication
from Page_Object.community.Community_work.Application.Network_BBS.page_Return_card_management import \
    Page_Return_card_management
from Page_Object.community.Community_work.Application.questionnaire.page_Labeling_management import \
    Page_Labeling_management
import time

'''这是圈子管理的业务流程'''


def screen_开始(driver):
    '''开始筛选流程'''

    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_圈子论坛()


def screen_普通贴(driver):
    '''筛选普通帖流程'''
    Page_Network_management(driver).click_帖子类型_普通贴()


def screen_精华帖(driver):
    '''筛选精华帖'''
    Page_Network_management(driver).click_帖子类型_精华帖()


def screen_否置顶(driver):
    '''筛选否置顶选项'''
    Page_Network_management(driver).click_是否置顶_否()


def screen_是置顶(driver):
    '''筛选是置顶选项'''
    Page_Network_management(driver).click_是否置顶_是()


def screen_是推荐(driver):
    '''筛选是推荐选项'''
    Page_Network_management(driver).click_是否推荐_是()


def screen_否推荐(driver):
    '''筛选否推荐选项'''
    Page_Network_management(driver).click_是否推荐_否()


def screen_创建时间_全部(driver):
    '''筛选全部-创建日期'''
    Page_Network_management(driver).click_创建日期_全部()


def screen_今日(driver):
    '''筛选今日-创建日期'''
    Page_Network_management(driver).click_创建日期_今日()


def screen_昨日(driver):
    '''筛选昨日-创建日期'''
    Page_Network_management(driver).click_创建日期_昨日()


def screen_本周(driver):
    '''筛选本周-创建日期'''
    Page_Network_management(driver).click_创建日期_本周()


def screen_本月(driver):
    '''筛选本月-创建日期'''
    Page_Network_management(driver).click_创建日期_本月()


'''这是回帖管理的业务流程'''


def screen_帖子状态_待审核(driver, communityID):
    '''筛选帖子状态_待审核'''
    Page_CommunityList(driver).mouse_click_社区(communityID)
    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_圈子论坛()
    Page_Network_management(driver).click_回帖管理()
    Page_Return_card_management(driver).click_帖子状态_待审核()


def screen_帖子状态_审核通过(driver):
    '''筛选帖子状态_审核通过'''
    Page_Return_card_management(driver).click_帖子状态_审核通过()


def screen_帖子状态_审核不通过(driver):
    '''筛选帖子状态_审核不通过'''
    Page_Return_card_management(driver).click_帖子状态_审核不通过()


def screen_帖子状态_已删除(driver):
    '''筛选帖子状态_已删除'''
    Page_Return_card_management(driver).click_帖子状态_已删除()


'''这是圈主/医生设置的业务流程'''


def screen_吧主管理_新增(driver, communityID):
    '''点击吧主管理_新增---未完待续'''
    Page_CommunityList(driver).mouse_click_社区(communityID)
    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_圈子论坛()
    Page_Network_management(driver).click_圈主_医生设置()
    Page_Circle_the_main(driver).click_吧主管理_新增()


def screen_医生管理_新增(driver):
    '''点击医生管理_新增---未完待续'''
    Page_Circle_the_main(driver).click_医生管理_新增()


'''这个是帖子标签管理业务流程'''


def new_新建帖子标签(driver, content):
    '''新建帖子标签'''
    Page_Home(driver).click_应用()
    Page_MyApplication(driver).click_圈子论坛()
    Page_Network_management(driver).click_帖子标签管理()
    Page_Post_label_management(driver).click_新建帖子标签().send_新增标签_输入内容(content).click_新建帖子标签_确定()


def screen_搜索框(driver, value):
    '''搜索框搜索'''
    Page_Post_label_management(driver).send_搜索框(value)
