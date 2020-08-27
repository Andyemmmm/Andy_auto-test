#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/20 16:24
# @File     : page_doctor_class_download.py
# @Software : aiwen_ui


from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Doctor_class_download(SeleniumBase):
    '''
    这个是应用市场里面的医生模块开通页面
    '''

    loc_医生课堂 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div[1]/div[2]/p[1]')
    loc_开通 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div[1]/div[3]/button/span')
    lco_确定开通 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')

    def get_获取医生课堂文本(self):
        return self.get_element_text(self.loc_医生课堂)

    def click_开通(self):
        self.click_element(self.loc_开通)
        return self

    def click_确定开通(self):
        self.ex_script_click(self.lco_确定开通)
        return self
