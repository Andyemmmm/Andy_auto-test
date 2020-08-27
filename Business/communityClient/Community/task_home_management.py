from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.Community_work.home_page.page_home import Page_Home
from Page_Object.community.Community_work.community.page_community_management import Page_Community_management
from Page_Object.community.Community_work.community.page_home_management import Page_Home_management

import time


def Home_management(driver, title, title1, png, png1, title2, title3, classname, classname1, doctor,
                    doctor1, doctor2, title4, title5, title6, title7):
    '''首页管理的流程'''

    Page_Home(driver).click_社区()
    Page_Community_management(driver).click_首页管理()
    Page_Home_management(
        driver).click_banner1_编辑().click_banner弹窗_内容类型().click_banner弹窗_内容类型_选项().click_banner弹窗_标题().send_banner弹窗_标题(
        title).click_banner弹窗_标题_选项().send_banner弹窗_图片(
        png)
    Page_Home_management(driver).click_banner弹窗_裁切确定()
    time.sleep(3)
    Page_Home_management(driver).click_banner弹窗_确定()
    time.sleep(1)
    Page_Home_management(
        driver).click_banner2_编辑().click_banner弹窗_内容类型().click_banner弹窗_内容类型2_选项().click_banner弹窗_标题().send_banner弹窗_标题(
        title1).click_banner弹窗_标题_选项2().send_banner弹窗_图片(png1)
    Page_Home_management(driver).click_banner弹窗_裁切确定()
    time.sleep(3)
    Page_Home_management(driver).click_banner弹窗_确定()

    Page_Home_management(driver).click_功能推荐位_配置()

    Page_Home_management(driver).click_健康知识_咨询公告_配置().click_健康知识_编辑1()
    Page_Home_management(driver).click_健康咨询_标题输入().send_健康咨询_标题输入(title2).click_健康咨询_标题_选项(
    ).click_健康咨询_标题输入确定().click_咨询公告().click_咨询公告_编辑1().click_健康咨询_标题输入().send_健康咨询_标题输入(
        title3).click_健康咨询_标题_选项().click_健康咨询_标题输入确定()

    Page_Home_management(driver).click_医医课堂_配置().click_医医课堂_编辑1().click_医医课堂_标题输入().send_医医课堂_标题输入(
        classname).click_医医课堂_标题选项().click_医医课堂_标题确定()
    time.sleep(1)
    Page_Home_management(driver).click_医医课堂_编辑2().click_医医课堂_标题输入().send_医医课堂_标题输入(
        classname1).click_医医课堂_标题选项().click_医医课堂_标题确定()

    Page_Home_management(driver).scroll_医生推荐_配置().click_医生推荐配置().click_医生推荐_推荐位1().send_医生推荐_推荐位1(
        doctor).click_医生推荐_推荐位_选项()
    time.sleep(0.5)
    Page_Home_management(driver).click_医生推荐_推荐位2().send_医生推荐_推荐位2(
        doctor1).click_医生推荐_推荐位_选项1()
    time.sleep(0.5)
    Page_Home_management(driver).click_医生推荐_推荐位3().send_医生推荐_推荐位3(doctor2).click_医生推荐_推荐位_选项2().click_医生推荐_确定()
    time.sleep(1)

    Page_Home_management(driver).click_热门帖子_配置().click_热门帖子_编辑1().click_热门帖子_标题输入().send__热门帖子_标题输入(
        title4).click_热门帖子_标题_选项().click_热门帖子_确定()
    time.sleep(1)
    Page_Home_management(driver).click_热门帖子_编辑2().click_热门帖子_标题输入().send__热门帖子_标题输入(
        title5).click_热门帖子_标题_选项().click_热门帖子_确定()

    Page_Home_management(driver).click_热门专题_配置().click_专题配置_编辑1().click_专题配置_标题输入().send__专题配置_标题输入(
        title6).click_专题配置_标题选项().click_专题配置_标题确定().click_专题配置_编辑2().click_专题配置_标题输入().send__专题配置_标题输入(
        title7).click_专题配置_标题选项().click_专题配置_标题确定()

    Page_Home_management(driver).click_精选科普_配置().click_精选科普_编辑1().click_精选科普_标题输入().send__精选科普_标题输入(
        title).click_精选科普_标题选项().click_精选科普_标题确定().click_精选科普_编辑2().click_精选科普_标题输入().send__精选科普_标题输入(
        title1).click_精选科普_标题选项().click_精选科普_标题确定()

    Page_Community_management(driver).click_社区管理()
