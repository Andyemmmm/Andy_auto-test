import time

from Business.communityClient.用户中心 import task_登录业务
from Page_Object.community.page_bseting import Page_Bseting, Page_Organization, Page_Staff_Management, \
    Page_personal_data, Page_security_settings


def organization_update_name(driver, name):
    """机构设置---更新机构名称业务流程"""
    Page_Bseting(driver).mouse_over_机构信息()
    time.sleep(0.5)
    Page_Bseting(driver).mouse_click_机构设置()
    time.sleep(0.5)
    Page_Organization(driver).send_机构名称(name).click_更新()


def Add_members(driver, phone, phone1=None, phone2=None):
    '''员工管理--添加员工业务流程'''
    Page_Bseting(driver).mouse_over_机构信息()
    time.sleep(0.5)
    Page_Bseting(driver).mouse_click_添加机构成员()
    time.sleep(0.5)
    Page_Staff_Management(driver).click_添加员工()
    time.sleep(0.5)
    Page_Staff_Management(driver).send_phone1(phone)
    if phone1:
        Page_Staff_Management(driver).click_添加更多()
        Page_Staff_Management(driver).send_phone2(phone1)
    if phone2:
        Page_Staff_Management(driver).click_添加更多()
        Page_Staff_Management(driver).send_phone3(phone2)
    Page_Staff_Management(driver).click_发起邀请()


def remove_members(driver, phone):
    '''员工管理---移除员工业务流程'''
    Page_Bseting(driver).mouse_over_机构信息()
    time.sleep(0.5)
    Page_Bseting(driver).mouse_click_添加机构成员()
    time.sleep(0.5)
    Page_Staff_Management(driver).click_待加入()
    time.sleep(0.5)
    Page_Staff_Management(driver).remove_members(phone)
    time.sleep(0.5)
    Page_Staff_Management(driver).click_移除确定()


def update_personal(driver, name=None, head=None):
    '''用户信息---个人资料---更新信息'''
    Page_Bseting(driver).mouse_over_用户信息()
    time.sleep(0.5)
    Page_Bseting(driver).mouse_click_个人资料()
    time.sleep(0.5)
    if name:
        Page_personal_data(driver).send_name(name)
    if head:
        Page_personal_data(driver).send_头像(head)
        Page_personal_data(driver).click_裁切确定()
        time.sleep(0.5)
    Page_personal_data(driver).click_更新信息()


def change_password(driver, password, newpassword, pwd):
    '''用户信息---安全设置---修改密码'''
    Page_Bseting(driver).mouse_over_用户信息()
    time.sleep(0.5)
    Page_Bseting(driver).mouse_click_安全设置()
    time.sleep(0.5)
    Page_security_settings(driver).click_修改()
    time.sleep(0.5)
    Page_security_settings(driver).send_当前密码(password).send_新密码(newpassword).send_重复密码(pwd).click_更新密码()
