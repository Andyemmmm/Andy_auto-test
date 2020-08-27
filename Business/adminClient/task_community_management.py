#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/10 13:45
# @File     : task_community_management.py
# @Software : aiwen_ui

import time
from Page_Object.adminClient.page_community_management import Page_Community_message
from Page_Object.adminClient.page_home import Page_Home


def operation_online_community(driver, community_name=None, community_id=None, organization_name=None,
                               organization_id=None, arguments=None, reason=None):
    '''
    社区管理--社区信息---社区操作流程
    :param driver:            浏览器
    :param community_name:    社区名称
    :param community_id:      社区id
    :param organization_name: 机构名称
    :param organization_id:   机构id
    :param arguments:         操作栏选项（上线，详情，下架）
    :param reason:            上线或下架的原因
    :return:
    '''
    Page_Home(driver).click_社区管理()
    if community_id:
        Page_Community_message(driver).send_社区id(community_id).click_搜索()
    if organization_name:
        Page_Community_message(driver).send_机构名称(organization_name).click_搜索()
    if organization_id:
        Page_Community_message(driver).send_机构id(organization_id).click_搜索()
    if community_name:
        Page_Community_message(driver).send_社区名称(community_name).click_搜索()
    time.sleep(1.5)
    if arguments == '上线':
        try:
            Page_Community_message(driver).click_上线().send_上线缘由(reason).click_上线申请确定()
        except:
            print('没有上线按钮，此社区可能已经上线')
            pass

    elif arguments == '详情':
        try:
            Page_Community_message(driver).click_详情()
        except:
            print('没有详情按钮，此社区可能不存在')
            pass

    elif arguments == '下架':
        try:
            Page_Community_message(driver).click_下架().send_下架原因(reason).click_下架确定()
        except:
            print('没有上线按钮，此社区可能已经下架')
            pass
