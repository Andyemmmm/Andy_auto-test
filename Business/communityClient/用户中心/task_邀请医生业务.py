import time

from Page_Object.community.Community_work.doctor.page_doctor import Page_Doctor, Page_Label_Management
from Page_Object.community.Community_work.doctor.page_doctor_invite import Page_Doctor_Invite
from Page_Object.community.Community_work.home_page.page_home import Page_Home


def Doctor_invite(driver, name, phone):
    """邀请医生加入社区业务流程"""
    Page_Home(driver).click_医生()
    Page_Doctor(driver).mouse_click_邀请医生()
    Page_Doctor_Invite(driver).send_输入邀请医生名称(name).send_输入邀请医生手机号(phone).click_添加().click_确认()


def Lable_management(driver, name):
    '''新建医生模块--新建标签管理'''
    Page_Home(driver).click_医生()
    Page_Doctor(driver).click_标签管理()
    time.sleep(1)
    Page_Label_Management(driver).click_新建标签().send_标签(name).click_确定()
