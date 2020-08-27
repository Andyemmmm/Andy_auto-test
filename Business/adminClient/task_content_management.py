#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/17 17:03
# @File     : task_content_management.py
# @Software : aiwen_ui

import time
from Page_Object.adminClient.page_content_management import Page_Content_Management, Page_Article_Detail
from Page_Object.adminClient.page_home import Page_Home


def article_view(driver):
    '''查看内容管理--医生文章列表的文章'''
    Page_Home(driver).click_内容管理()


def article_detail(driver):
    '''查看内容管理--医生文章列表详情的文章'''
    Page_Content_Management(driver).click_查看()


def del_article(driver):
    '''删除内容管理--医生文章详情页删除'''
    Page_Article_Detail(driver).click_删除()
    time.sleep(1)
    Page_Article_Detail(driver).click_确定删除()
