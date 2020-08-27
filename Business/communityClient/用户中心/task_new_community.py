#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/28 10:34
# @File     : task_new_community.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
import time
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Page_Object.community.page_new_community import Page_New_community, Page_community_info, Page_Hospital, \
    Page_organization, Page_Doctor_team, Page_certificated_information_hospital, \
    Page_certificated_information_organization, Page_certificated_information_doctor, Page_Project_community

'''新建社区---填写社区信息公共流程'''


def new_community_info(driver, community_name, slogan, abbreviation, brief, png, option, disease):
    '''新建社区---填写社区信息的流程'''
    Page_community_info(driver).send_名称(community_name).send_Slogan(slogan).send_简称(abbreviation).send_简介(
        brief).send_logo(png).click_logo_确定()
    time.sleep(1)
    Page_community_info(driver).click_特色科室(option).click_擅长疾病(disease)


'''社区B端--新建医院社区流程'''


def New_community_hospital(driver, community_name, slogan, abbreviation, brief, png, option, disease, name, addr,
                           option1, option2, name1, png2, png3, name2, phone, confirm):
    '''社区B端--新建医院社区流程'''
    # Page_CommunityList(driver).click_新建社区()
    # Page_New_community(driver).click_社区(type).click_next()
    new_community_info(driver, community_name, slogan, abbreviation, brief, png, option, disease)
    Page_Hospital(driver).send_hoapital_name(name).send_hospital_addr(addr)
    time.sleep(2)
    Page_Hospital(driver).click_经营性质(option1)
    time.sleep(1)
    Page_Hospital(driver).click_医院类型(option2)
    Page_New_community(driver).click_next()
    # time.sleep(1)
    try:
        text = Page_New_community(driver).get_msg()
        if text == "社区名称已存在,请重新编辑" or text == '社区简称已被使用':
            return text
    except:
        if confirm:
            Page_certificated_information_hospital(driver).click_沿用上一个社区资料()
        else:
            Page_certificated_information_hospital(driver).send_企业名称(name1).send_营业执照(png2).send_执业许可证(png3).send_其他证件(
                png3).send_联系人(name2).send_联系方式(phone)
        time.sleep(2)
        Page_New_community(driver).click_next()


'''社区B端--新建机构集团类型社区流程'''


def New_community_organization(driver, community_name, slogan, abbreviation, brief, png, option, disease, name,
                               addr, name1, png2, png3, name2, phone):
    # Page_CommunityList(driver).click_新建社区()
    # Page_New_community(driver).click_社区(type).click_next()
    new_community_info(driver, community_name, slogan, abbreviation, brief, png, option, disease)
    Page_organization(driver).send_集团机构名称(name).send_集团机构地址(addr)
    Page_New_community(driver).click_next()
    # time.sleep(1)
    try:
        text = Page_New_community(driver).get_msg()
        if text == "社区名称已存在,请重新编辑" or text == '社区简称已被使用':
            return text
    except:
        Page_certificated_information_organization(driver).send_企业名称(name1).send_营业执照(png2).send_其他证件(png3).send_联系人(
            name2).send_联系方式(phone)
        time.sleep(2)
        Page_New_community(driver).click_next()


'''社区B端--新建医生团队类型社区流程'''


def New_community_doctorteam(driver, community_name, slogan, abbreviation, brief, png, option, disease, name,
                             name2, name3, png2, job, hospital, job2, job3, png3, aiwen):
    # Page_CommunityList(driver).click_新建社区()
    # Page_New_community(driver).click_社区(type).click_next()
    new_community_info(driver, community_name, slogan, abbreviation, brief, png, option, disease)
    if aiwen:
        Page_Doctor_team(driver).click_爱问平台医生().click_add()
        time.sleep(0.5)
        Page_Doctor_team(driver).send_doctor_mz(name).click_确定()
        time.sleep(0.5)
        Page_Doctor_team(driver).click_add()
        time.sleep(0.5)
        Page_Doctor_team(driver).send_doctor_mz(name2).click_确定()
        time.sleep(0.5)
        Page_Doctor_team(driver).click_add()
        time.sleep(0.5)
        Page_Doctor_team(driver).send_doctor_mz(name3).click_确定()
        time.sleep(0.5)
    else:
        Page_Doctor_team(driver).click_非爱问平台医生().click_add()
        time.sleep(1)
        Page_Doctor_team(driver).send_doctor_name(name).send_doctor_head(png2).click_裁切().click_职称(job).send_执业医院(
            hospital).click_添加医生确定()
        time.sleep(0.5)
        Page_Doctor_team(driver).click_add()
        time.sleep(0.5)
        Page_Doctor_team(driver).send_doctor_name(name2).send_doctor_head(png2).click_裁切1().click_职称(job2).send_执业医院(
            hospital).click_添加医生确定()
        time.sleep(0.5)
        Page_Doctor_team(driver).click_add()
        time.sleep(0.5)
        Page_Doctor_team(driver).send_doctor_name(name3).send_doctor_head(png2).click_裁切1().click_职称(job3).send_执业医院(
            hospital).click_添加医生确定()
        time.sleep(0.5)
    Page_New_community(driver).click_next()
    # time.sleep(1)
    try:
        text = Page_New_community(driver).get_msg()
        if text == "社区名称已存在,请重新编辑" or text == '社区简称已被使用':
            return text
    except:
        Page_certificated_information_doctor(driver).send_承诺函(png3)
        time.sleep(2)
        Page_certificated_information_doctor(driver).click_上传资质1().send_资质(png, png2, png3)
        time.sleep(1)
        Page_certificated_information_doctor(driver).click_上传资质2().send_资质(png, png2, png3)
        time.sleep(1)
        Page_certificated_information_doctor(driver).click_上传资质3().send_资质(png, png2, png3)
        time.sleep(1)
        Page_New_community(driver).click_next()


'''社区B端--新建项目类型社区流程'''


def New_community_project(driver, community_name, slogan, abbreviation, brief, png, option, disease, name, introduce):
    # Page_CommunityList(driver).click_新建社区()
    # Page_New_community(driver).click_社区(type).click_next()
    new_community_info(driver, community_name, slogan, abbreviation, brief, png, option, disease)
    Page_Project_community(driver).send_项目名称(name).send_项目介绍(introduce)
    Page_New_community(driver).click_next()


'''**************************以下是新建测试类型的社区流程********************************以下是新建测试类型的社区流程******************************以下是新建测试类型的社区流程***************************'''

'''社区B端---新建测试社区的医院类型的社区'''


def New_Test_community_hospital(driver, community_name, slogan, abbreviation, brief, png, option, disease, name,
                                addr, option1, option2, name1, png2, png3, name2, phone, confirm):
    Page_New_community(driver).click_测试社区(type='医院').click_next()
    text = New_community_hospital(driver, community_name, slogan, abbreviation, brief, png, option, disease, name, addr,
                                  option1, option2, name1, png2, png3, name2, phone, confirm)
    return text


'''社区B端---新建测试社区的机构类型的社区'''


def New_Test_community_organization(driver, community_name, slogan, abbreviation, brief, png, option, disease, name,
                                    addr, name1, png2, png3, name2, phone):
    Page_New_community(driver).click_测试社区(type='机构').click_next()
    text = New_community_organization(driver, community_name, slogan, abbreviation, brief, png, option, disease, name,
                                      addr, name1, png2, png3, name2, phone)
    return text


'''社区B端---新建测试社区的医生团队类型的社区'''


def New_Test_community_doctorteam(driver, community_name, slogan, abbreviation, brief, png, option, disease, name,
                                  name2, name3, png2, job, hospital, job2, job3, png3, aiwen):
    Page_New_community(driver).click_测试社区(type='医生团队').click_next()
    text = New_community_doctorteam(driver, community_name, slogan, abbreviation, brief, png, option, disease, name,
                                    name2, name3, png2, job, hospital, job2, job3, png3, aiwen)
    return text


'''社区B端---新建测试社区的项目类型的社区'''


def New_Test_community_project(driver, community_name, slogan, abbreviation, brief, png, option, disease, name,
                               introduce):
    Page_New_community(driver).click_测试社区(type='项目型社区').click_next()
    New_community_project(driver, community_name, slogan, abbreviation, brief, png, option, disease, name, introduce)


'''社区B端---社区上线'''


def up_online(driver):
    Page_CommunityList(driver).click_第一个社区()
    Page_Home(driver).click_首页()
    time.sleep(1)
    Page_Home(driver).click_online().click_online_confirm()
