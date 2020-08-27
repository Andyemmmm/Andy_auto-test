#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/4 11:59
# @File     : page_bseting.py
# @Software : aiwen_ui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Common.selenium_library import SeleniumBase


class Page_Bseting(SeleniumBase):
    '''这是社区B端社区列表页面'''
    loc_机构信息 = (By.XPATH, "//div[@class='info_word']")
    loc_用户信息 = (By.XPATH, "//div[@class='user-info-wrapper']")
    loc_机构设置 = (By.XPATH, "//ul[@class='dropdown']/li[1]/div")
    loc_添加机构成员 = (By.XPATH, "//ul[@class='dropdown']/li[2]/div")
    loc_个人资料 = (By.XPATH, "//ul[@class='dropdown dropdown_right']/li[1]/div")
    loc_安全设置 = (By.XPATH, "//ul[@class='dropdown dropdown_right']/li[2]/div")
    loc_社区列表 = (By.XPATH, "//ul[@class='dropdown dropdown_right']/li[3]/div")
    loc_退出登录 = (By.XPATH, "//ul[@class='dropdown dropdown_right']/li[4]/div")

    def mouse_over_机构信息(self):
        self.mouse_over(self.loc_机构信息)
        return self

    def mouse_over_用户信息(self):
        self.mouse_over(self.loc_用户信息)
        return self

    def mouse_click_机构设置(self):
        self.mouse_over_click(self.loc_机构设置)
        return self

    def mouse_click_添加机构成员(self):
        self.mouse_over_click(self.loc_添加机构成员)
        return self

    def mouse_click_个人资料(self):
        self.mouse_over_click(self.loc_个人资料)
        return self

    def mouse_click_安全设置(self):
        self.mouse_over_click(self.loc_安全设置)
        return self

    def mouse_click_社区列表(self):
        self.mouse_over_click(self.loc_社区列表)
        return self

    def mouse_click_退出登录(self):
        self.mouse_over_click(self.loc_退出登录)
        return self


class Page_Organization(SeleniumBase):
    '''这是机构设置的页面'''
    loc_机构设置 = (By.XPATH, "//ul[@class='tabs']/li[1]")
    loc_员工管理 = (By.XPATH, "//ul[@class='tabs']/li[2]")
    loc_机构名称 = (By.XPATH, '//*[@id="app"]/div/div[2]/section/main/form/div[1]/div/div/input')
    loc_更新 = (By.XPATH, "//span[text()='更新']")
    loc_err_msg = (By.XPATH, '//div[@class="el-form-item__error"]')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def click_机构设置(self):
        self.mouse_over_click(self.loc_机构设置)
        return self

    def click_员工管理(self):
        self.mouse_over_click(self.loc_员工管理)
        return self

    def send_机构名称(self, name):
        self.send_keys(self.loc_机构名称, name)
        return self

    def click_更新(self):
        self.click_element(self.loc_更新)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)

    def get_err_msg(self):
        return self.get_element_text(self.loc_err_msg)


class Page_Staff_Management(SeleniumBase):
    '''这是员工管理的页面'''
    loc_添加员工 = (By.XPATH, "//button/span[text()='添加员工']")
    loc_状态_使用中 = (By.XPATH, "//ul[@class='tag-list']/li[1]")
    loc_状态_已停用 = (By.XPATH, "//ul[@class='tag-list']/li[2]")
    loc_状态_待加入 = (By.XPATH, "//ul[@class='tag-list']/li[3]")
    loc_添加更多 = (By.XPATH, "//span[normalize-space(text())='添加更多']")
    loc_手机号1 = (By.XPATH, "//label[text()='手机号1']/following-sibling::div//input")
    loc_手机号2 = (By.XPATH, "//label[text()='手机号2']/following-sibling::div//input")
    loc_手机号3 = (By.XPATH, "//label[text()='手机号3']/following-sibling::div//input")
    loc_发起邀请 = (By.XPATH, "//span[normalize-space(text())='发起邀请']")
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")
    loc_err_msg = (By.XPATH, '//div[@class="el-form-item__error"]')
    loc_第一行手机号码 = (By.XPATH, "//table/tbody/tr[1]/td[3]/div")
    loc_移除成员确定 = (By.XPATH, '//div[@aria-label="移除员工"]//button[1]/span')
    loc_总记录数 = (By.XPATH, '//span[@class="el-pagination__total"]')
    next_page = (By.XPATH, '//button[@class="btn-next"]')

    def click_添加员工(self):
        self.mouse_over_click(self.loc_添加员工)
        return self

    def click_使用中(self):
        self.click_element(self.loc_状态_使用中)
        return self

    def click_已停用(self):
        self.click_element(self.loc_状态_已停用)
        return self

    def click_待加入(self):
        self.click_element(self.loc_状态_待加入)
        return self

    def click_添加更多(self):
        self.click_element(self.loc_添加更多)
        return self

    def send_phone1(self, phone):
        self.send_keys(self.loc_手机号1, phone)
        return self

    def send_phone2(self, phone):
        self.send_keys(self.loc_手机号2, phone)
        return self

    def send_phone3(self, phone):
        self.send_keys(self.loc_手机号3, phone)
        return self

    def click_发起邀请(self):
        self.click_element(self.loc_发起邀请)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)

    def get_err_msg(self):
        text = self.get_element_text(self.loc_err_msg)
        if text == '':
            while text == '':
                text = self.get_element_text(self.loc_err_msg)
        return text

    def get_第一行手机号码(self):
        return self.get_element_text(self.loc_第一行手机号码)

    def remove_members(self, phone):
        try:
            ele = self.driver.find_element_by_xpath(
                f"//table/tbody//div[text()='{phone}']/parent::td/following-sibling::td//span[text()='移除员工']")
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        except:
            total = self.get_page_size(self.loc_总记录数)
            for i in range(total):
                self.click_element(self.next_page)
                try:
                    ele = self.driver.find_element_by_xpath(
                        f"//table/tbody//div[text()='{phone}']/parent::td/following-sibling::td//span[text()='移除员工']")
                    if ele.is_displayed():
                        break
                except:
                    pass
            try:
                ele = self.driver.find_element_by_xpath(
                    f"//table/tbody//div[text()='{phone}']/parent::td/following-sibling::td//span[text()='移除员工']")
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            except:
                print('输入的手机号码不存在，请确定输入的手机号码是否正确')
        return self

    def click_移除确定(self):
        self.click_element(self.loc_移除成员确定)
        return self


class Page_personal_data(SeleniumBase):
    '''用户信息---个人资料页面'''
    loc_个人资料 = (By.XPATH, "//ul[@class='tabs']/li[1]")
    loc_安全设置 = (By.XPATH, "//ul[@class='tabs']/li[2]")
    loc_头像 = (By.XPATH, '//*[@id="app"]/div/div[2]/section/main/div/div[2]/form/div[1]/div/div/div[1]/input')
    loc_裁切确定 = (By.XPATH, '//div[@aria-label="裁剪图片"]//span[text()="确 定"]')
    loc_name = (By.XPATH, '//*[@id="app"]/div/div[2]/section/main/div/div[2]/form/div[2]/div/div/input')
    loc_更新信息 = (By.XPATH, "//span[text()='更新信息']")
    loc_err_msg = (By.XPATH, '//div[@class="el-form-item__error"]')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def click_个人资料(self):
        self.mouse_over_click(self.loc_个人资料)
        return self

    def click_安全设置(self):
        self.mouse_over_click(self.loc_安全设置)
        return self

    def send_头像(self, png):
        self.send_png(self.loc_头像, png)
        return self

    def send_name(self, name):
        self.send_keys(self.loc_name, name)
        return self

    def click_更新信息(self):
        self.click_element(self.loc_更新信息)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)

    def get_err_msg(self):
        return self.get_element_text(self.loc_err_msg)

    def click_裁切确定(self):
        self.click_element(self.loc_裁切确定)
        return self


class Page_security_settings(SeleniumBase):
    '''用户信息---安全设置'''
    loc_修改 = (By.XPATH, "//span[text()='修改']")
    loc_当前密码 = (By.XPATH, '//input[@placeholder="请输入当前密码"]')
    loc_新密码 = (By.XPATH, '//input[@placeholder="请输入新密码"]')
    loc_重复密码 = (By.XPATH, '//input[@placeholder="请再次输入新密码"]')
    loc_更新密码 = (By.XPATH, "//span[text()='更新密码']")
    loc_err_msg = (By.XPATH, '//div[@class="el-form-item__error"]')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def click_修改(self):
        self.click_element(self.loc_修改)
        return self

    def send_当前密码(self, password):
        self.send_keys(self.loc_当前密码, password)
        return self

    def send_新密码(self, password):
        self.send_keys(self.loc_新密码, password)
        return self

    def send_重复密码(self, password):
        self.send_keys(self.loc_重复密码, password)
        return self

    def click_更新密码(self):
        self.click_element(self.loc_更新密码)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)

    def get_err_msg(self):
        return self.get_element_text(self.loc_err_msg)
