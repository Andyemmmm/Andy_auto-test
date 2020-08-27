#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/20 14:07
# @File     : task_setting.py
# @Software : aiwen_ui
import time

from Page_Object.community.Community_work.set.page_member_management import Page_Memberm_management, \
    Page_Memberm_management
from Page_Object.community.Community_work.set.page_message_notification import Page_Message_notification
from Page_Object.community.Community_work.set.page_role_management import Page_role_management
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home

'''成员管理---业务流程'''


def Add_members(driver, name, option):
    '''成员管理---添加成员流程'''
    Page_Home(driver).click_设置()
    Page_Message_notification(driver).click_成员管理()
    time.sleep(1)
    Page_Memberm_management(driver).click_添加成员()
    time.sleep(0.5)
    Page_Memberm_management(driver).send_添加成员搜索框(name).click_搜索框选项().click_角色分配()
    time.sleep(0.5)
    Page_Memberm_management(driver).click_角色分配选项(option).click_添加成员确定()


def Remove_members(driver):
    '''成员管理---移除成员流程'''
    Page_Home(driver).click_设置()
    Page_Message_notification(driver).click_成员管理()
    time.sleep(1)
    Page_Memberm_management(driver).click_移除()
    time.sleep(0.5)
    Page_Memberm_management(driver).click_移除确定()


'''角色管理---业务流程'''


def New_role(driver, role, describe):
    '''角色管理---新建角色流程'''
    Page_Home(driver).click_设置()
    Page_Message_notification(driver).click_角色管理()
    time.sleep(1)
    Page_role_management(driver).click_新建角色()
    time.sleep(1)
    Page_role_management(driver).send_角色名称(role).send_角色描述(describe).click_提交()


def del_role(driver):
    '''角色管路---删除角色流程'''
    Page_Home(driver).click_设置()
    Page_Message_notification(driver).click_角色管理()
    time.sleep(1.5)
    Page_role_management(driver).click_删除()
    time.sleep(0.5)
    Page_role_management(driver).click_确定删除()
