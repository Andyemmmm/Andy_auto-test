#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/20 17:17
# @File     : page_new_doctor_class.py
# @Software : aiwen_ui


from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_New_doctor_class(SeleniumBase):
    '''
    这个是医生课堂--新建课程页面
    '''

    loc_课程标题 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/form/div[1]/div/div/input')
    loc_课程简介 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/form/div[2]/div/div/textarea')
    loc_课程视频 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/form/div[3]/div/div/div[1]/div/input')
    loc_课程封面 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/form/div[4]/div/div/div[1]/input')
    loc_课程介绍 = (By.XPATH, '/html/body')
    loc_课程大纲 = (By.XPATH, '/html/body')
    loc_医生姓名 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[1]/div/div/input')
    loc_医生头衔 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[2]/div/div/input')
    loc_医生头像 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/form/div[3]/div/div/div[1]/input')
    loc_调查问卷 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/form/div/div/div/input')
    loc_确定 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[5]/button[1]/span')
    loc_取消 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[5]/button[2]/span')
    loc_富文本框_介绍 = ('ueditor_0')
    loc_富文本框_大纲 = ('ueditor_1')
    loc_新增 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[4]/div[2]/div[1]/button[1]/span')
    loc_上传名单 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[4]/div[2]/div[1]/button[2]/span')
    loc_新增医生_姓名 = (By.XPATH,
                   '//*[@id="app"]/section/section/main/div/div[2]/div/div[4]/div[2]/div[2]/div/div[2]/form/div[1]/div/div[1]/input')
    loc_新增医生_手机号码 = (By.XPATH,
                     '//*[@id="app"]/section/section/main/div/div[2]/div/div[4]/div[2]/div[2]/div/div[2]/form/div[2]/div/div[1]/input')
    loc_新增医生_确定 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[4]/div[2]/div[2]/div/div[3]/span/button[2]/span')
    loc_新增医生_取消 = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div/div[2]/div/div[4]/div[2]/div[2]/div/div[3]/span/button[1]/span')
    loc_课程封面裁切图片确定 = (By.XPATH, '/html/body/div[3]/div/div[3]/span/button[2]/span')
    loc_医生头像裁切图片确定 = (By.XPATH, '/html/body/div[4]/div/div[3]/span/button[2]/span')

    def send_课程标题(self, title):
        self.send_keys(self.loc_课程标题, title)
        return self

    def send_课程简介(self, about):
        self.send_keys(self.loc_课程简介, about)
        return self

    def send_课程视频(self, video):
        self.send_keys(self.loc_课程视频, video)
        return self

    def send_课程封面(self, cover):
        self.send_keys(self.loc_课程封面, cover)
        return self

    def send_课程介绍(self, introduce):
        self.send_keys(self.loc_课程介绍, introduce)
        return self

    def send_课程大纲(self, outline):
        self.send_keys(self.loc_课程大纲, outline)
        return self

    def send_医生姓名(self, name):
        self.send_keys(self.loc_医生姓名, name)
        return self

    def send_医生头衔(self, header):
        self.send_keys(self.loc_医生头衔, header)
        return self

    def send_医生头像(self, photo):
        self.send_keys(self.loc_医生头像, photo)
        return self

    def send_调查问卷(self, survey):
        self.send_keys(self.loc_调查问卷, survey)
        return self

    def click_确定(self):
        self.mouse_over_click(self.loc_确定)
        return self

    def click_取消(self):
        self.click_element(self.loc_取消)
        return self

    def switch_富文本框_介绍(self):
        self.switch_to_frame(self.loc_富文本框_介绍)
        return self

    def switch_富文本框_大纲(self):
        self.switch_to_frame(self.loc_富文本框_大纲)
        return self

    def send_新增医生_姓名(self, newname):
        self.send_keys(self.loc_新增医生_姓名, newname)
        return self

    def send_新增医生_手机号码(self, phone):
        self.send_keys(self.loc_新增医生_手机号码, phone)
        return self

    def click_新增(self):
        self.click_element(self.loc_新增)
        return self

    def click_上传名单(self):
        self.click_element(self.loc_上传名单)
        return self

    def click_新增医生_确定(self):
        self.click_element(self.loc_新增医生_确定)
        return self

    def click_新增医生_取消(self):
        self.click_element(self.loc_新增医生_取消)
        return self

    def click_课程封面裁切图片确定(self):
        self.mouse_over_click(self.loc_课程封面裁切图片确定)
        return self

    def click_医生头像裁切图片确定(self):
        self.mouse_over_click(self.loc_医生头像裁切图片确定)
        return self
