#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/10 13:45
# @File     : task_audit_management.py
# @Software : aiwen_ui

import time
from Page_Object.adminClient.page_audit_management import Page_Community_qualification_audit, \
    Page_Community_online_application
from Page_Object.adminClient.page_home import Page_Home


def Review_community(driver, name=None, cause=None, reason=None):
    '''
    审核管理--社区资质审核（社区认证审核）---社区认证审核
    :param driver: 浏览器
    :param name:   社区名称
    :param args:   判断是否通过审核
    :param cause:  不通过的原因
    :param reason: 自定义原因
    :return:
    '''
    Page_Home(driver).click_审核管理()
    if name:
        Page_Community_qualification_audit(driver).send_社区名称(name).click_搜索()
        time.sleep(1)
        if cause:
            Page_Community_qualification_audit(driver).click_不通过()
            time.sleep(0.5)
            Page_Community_qualification_audit(driver).click_不通过原因().select_不通过原因(cause)
            if reason:
                Page_Community_qualification_audit(driver).click_自定义原因().send_自定义原因(reason)
            Page_Community_qualification_audit(driver).click_不通过确定()
        else:
            try:
                Page_Community_qualification_audit(driver).click_通过().click_通过确定()
            except:
                print('没有通过按钮，此社区可能已经审核')
                pass
    else:
        try:
            Page_Community_qualification_audit(driver).click_第一行通过().click_通过确定()
        except:
            print('没有通过按钮，此社区可能已经审核')
            pass


def Online_application(driver, name=None, reason=None):
    '''
    审核管理--社区上线申请--社区上线审核
    :param driver:   浏览器
    :param name:     社区名称
    :param reason:   不通过原因
    :return:
    '''
    Page_Home(driver).click_审核管理()
    time.sleep(1)
    Page_Community_qualification_audit(driver).click_社区上线申请()
    time.sleep(1)
    if name:
        Page_Community_online_application(driver).send_社区名称(name).click_搜索()
        time.sleep(1)
        if reason:
            Page_Community_online_application(driver).click_不通过()
            time.sleep(0.5)
            Page_Community_online_application(driver).send_不通过原因(reason).click_不通过确定()
        else:
            try:
                Page_Community_online_application(driver).click_通过().click_通过确定()
            except:
                print('没有通过按钮，此社区可能已经上线')
                pass
    else:
        try:
            Page_Community_online_application(driver).click_第一行通过().click_通过确定()
        except:
            print('没有通过按钮，此社区可能已经上线')
            pass
