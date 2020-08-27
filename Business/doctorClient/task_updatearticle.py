#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/3 15:31
# @File     : task_updatearticle.py
# @Software : aiwen_ui
import time
from Page_Object.doctorClient.PC.page_home import Page_Home
from Page_Object.doctorClient.PC.page_updatearticle import Page_UpdateArticle, Page_UpdateArticle_nextstep, \
    Page_UpdateArticle_ditchstep, Page_UpdateArticle_timestep
from Page_Object.doctorClient.PC.page_articles_published import Page_Articles_published
from Page_Object.doctorClient.PC.page_updatearticle_Clinic_and_diary import Page_UpdateArticle_Clinic_and_diary, \
    Page_UpdateArticle_ditchstep_Clinic_and_diary, Page_UpdateArticle_nextstep_Clinic_and_diary, \
    Page_UpdateArticle_timestep_Clinic_and_diary
from Page_Object.doctorClient.PC.page_updatearticle_case_analysis import Page_UpdateArticle_Case_analysis, \
    Page_UpdateArticle_ditchstep_case_analysis, Page_UpdateArticle_nextstep_case_analysis, \
    Page_UpdateArticle_timestep_case_analysis


def Updatearticle(driver, content, title, png):
    '''写 社区邀约活动 的 专题活动 和 科普文章活动 的文章（只有即时发布，没有定时发布的功能）'''
    Page_Home(driver).click_品牌推广().click_品牌推广_社区活动()
    time.sleep(30)
    Page_Home(driver).click_去完成().click_立即投稿()
    Page_UpdateArticle(driver).switch_iframe().send_输入框(content).switch_back_frame().click_下一步()
    Page_UpdateArticle_nextstep(driver).send_文章标题(
        title).click_文章标签().click_文章标签_选项1().click_文章标签_选项2().click_空白().send_图片(png).offset_裁切(
        ).click_裁切确定()
    time.sleep(2)
    Page_UpdateArticle_nextstep(driver).click_下一步()
    time.sleep(1)
    Page_UpdateArticle_ditchstep(driver).click_同步到微博().see_发布().ckick_发布()


def Updatearticle_health(driver, content, title, png, date, H, M):
    '''写 健康科普 的文章（只有即时发布，没有定时发布的功能）'''
    Page_Home(driver).click_文章发布()
    Page_Articles_published(driver).click_健康科普()
    Page_UpdateArticle(driver).switch_iframe().send_输入框(content).switch_back_frame().click_下一步()
    Page_UpdateArticle_nextstep(driver).send_文章标题(
        title).click_文章标签().click_文章标签_选项1().click_文章标签_选项2().click_空白().send_图片(png).offset_裁切(
        driver).click_裁切确定()
    time.sleep(2)
    Page_UpdateArticle_nextstep(driver).click_下一步()
    time.sleep(1)
    Page_UpdateArticle_timestep(driver).click_日期框().scr_date(date, H, M).click_下一步()
    Page_UpdateArticle_ditchstep(driver).click_同步到微博().see_发布().ckick_发布()


def Updatearticle_Clinic_and_diary(driver, content, png, date, H, M):
    '''写 诊间日记 的文章（有定时发布的功能）'''
    Page_Home(driver).click_文章发布()
    Page_Articles_published(driver).click_诊间日记()
    Page_UpdateArticle_Clinic_and_diary(driver).send_输入框(content).click_下一步()
    Page_UpdateArticle_nextstep_Clinic_and_diary(
        driver).click_文章标签().click_文章标签_选项1().click_文章标签_选项2().click_空白().send_图片(png).offset_裁切(driver).click_裁切确定()
    time.sleep(2)
    Page_UpdateArticle_nextstep_Clinic_and_diary(driver).click_下一步()
    time.sleep(1)
    Page_UpdateArticle_timestep_Clinic_and_diary(driver).click_日期框().scr_date(date, H, M).click_下一步()
    Page_UpdateArticle_ditchstep_Clinic_and_diary(driver).click_同步到微博().see_发布().ckick_发布()


def Updatearticle_case_analysis(driver, content, notes, title, png, date, H, M, select=None):
    '''写 病例分析 的文章 （有定时发布的功能）'''
    Page_Home(driver).click_文章发布()
    Page_Articles_published(driver).click_病例分析()
    if select:
        Page_UpdateArticle_Case_analysis(driver).click_选择病例().click_病例记录()
        Page_UpdateArticle_Case_analysis(driver).switch_frame0().send_医生心得(notes).switch_back_frame().click_下一步()
        time.sleep(0.5)
    else:
        Page_UpdateArticle_Case_analysis(driver).click_撰写病例()
        time.sleep(0.5)
        Page_UpdateArticle_Case_analysis(driver).switch_frame1().send_输入框(
            content).switch_back_frame().switch_frame2().send_医生心得(notes).switch_back_frame().click_下一步()
    Page_UpdateArticle_nextstep_case_analysis(driver).send_文章标题(
        title).click_文章标签().click_文章标签_选项1().click_文章标签_选项2().click_空白().send_图片(png).offset_裁切(
        driver).click_裁切确定()
    time.sleep(1)
    Page_UpdateArticle_nextstep_case_analysis(driver).click_下一步()
    time.sleep(1)
    Page_UpdateArticle_timestep_case_analysis(driver).click_日期框().scr_date(date, H, M).click_下一步()
    time.sleep(1)
    Page_UpdateArticle_ditchstep_case_analysis(driver).click_同步到微博().see_发布().ckick_发布()
