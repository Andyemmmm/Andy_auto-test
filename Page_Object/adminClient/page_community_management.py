#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/11 10:01
# @File     : community_management.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Community_message(SeleniumBase):
    '''这个爱问大后台--社区管理--社区信息页面'''
    loc_社区名称 = (By.XPATH, '//input[@placeholder="请输入社区名称"]')
    loc_社区id = (By.XPATH, '//input[@placeholder="请输入社区ID"]')
    loc_机构名称 = (By.XPATH, '//input[@placeholder="请输入机构名称"]')
    loc_机构id = (By.XPATH, '//input[@placeholder="请输入机构ID"]')
    loc_状态 = (By.XPATH, '//input[@placeholder="全部"]')
    loc_状态_全部 = (By.XPATH, "//body/script[4]/following-sibling::div[1]//ul/li/span[text()='全部']")
    loc_状态_已下架 = (By.XPATH, "//body/script[4]/following-sibling::div[1]//ul/li/span[text()='已下架']")
    loc_状态_上线中 = (By.XPATH, "//body/script[4]/following-sibling::div[1]//ul/li/span[text()='上线中']")
    loc_状态_已注销 = (By.XPATH, "//body/script[4]/following-sibling::div[1]//ul/li/span[text()='已注销']")
    loc_状态_未上线 = (By.XPATH, "//body/script[4]/following-sibling::div[1]//ul/li/span[text()='未上线']")
    loc_状态_上线审核中 = (By.XPATH, "//body/script[4]/following-sibling::div[1]//ul/li/span[text()='上线审核中']")
    loc_状态_上线审核未通过 = (By.XPATH, "//body/script[4]/following-sibling::div[1]//ul/li/span[text()='上线审核未通过']")
    loc_搜索 = (By.XPATH, "//span[text()='搜索']")
    loc_清除 = (By.XPATH, "//span[text()='清除']")

    loc_上线 = (By.XPATH, '//div[4]/div[1]/div[5]/div[2]/table/tbody/tr/td[12]/div/button[2]/span')
    loc_详情 = (By.XPATH, '//div[4]/div[1]/div[5]/div[2]/table/tbody/tr/td[12]/div/button[1]/span')
    loc_上线缘由 = (By.XPATH, '//textarea[@placeholder="请输入上线申请缘由。"]')
    loc_上线申请确定 = (By.XPATH, '//div[5]/div/div[3]/div/button[1]/span')
    loc_下架 = (By.XPATH, '//div[4]/div[1]/div[5]/div[2]/table/tbody/tr/td[12]/div/button[2]/span')
    loc_下架原因 = (By.XPATH, '//textarea[@placeholder="请输入下架原因"]')
    loc_下架确定 = (By.XPATH, '//div[3]/button[2]/span')
    loc_详情 = (By.XPATH, '//div[4]/div[1]/div[5]/div[2]/table/tbody/tr/td[12]/div/button[2]/span')
    # loc_频道管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[8]/div[2]/p[3]')
    # # loc_iask运营管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[9]/div[2]/p[3]')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def send_社区名称(self, name):
        self.send_keys(self.loc_社区名称, name)
        return self

    def send_社区id(self, ID):
        self.send_keys(self.loc_社区id, ID)
        return self

    def send_机构名称(self, name):
        return self.send_keys(self.loc_机构名称, name)

    def send_机构id(self, ID):
        self.send_keys(self.loc_机构id, ID)
        return self

    def click_状态(self):
        self.click_element(self.loc_状态)
        return self

    def click_状态_全部(self):
        self.mouse_over_click(self.loc_状态_全部)
        return self

    def click_状态_已下架(self):
        self.mouse_over_click(self.loc_状态_已下架)
        return self

    def click_状态_上线中(self):
        self.mouse_over_click(self.loc_状态_上线中)
        return self

    def click_状态_已注销(self):
        self.mouse_over_click(self.loc_状态_已注销)
        return self

    def click_状态_未上线(self):
        self.mouse_over_click(self.loc_状态_未上线)
        return self

    def click_状态_上线审核中(self):
        self.mouse_over_click(self.loc_状态_上线审核中)
        return self

    def click_状态_上线审核未通过(self):
        self.mouse_over_click(self.loc_状态_上线审核未通过)
        return self

    def click_清除(self):
        self.click_element(self.loc_清除)
        return self

    def click_搜索(self):
        self.mouse_over_click(self.loc_搜索)
        return self

    def click_上线(self):
        self.click_element(self.loc_上线)
        return self

    def click_详情(self):
        self.click_element(self.loc_详情)
        return self

    def send_上线缘由(self, reason):
        self.send_keys(self.loc_上线缘由, reason)
        return self

    def click_上线申请确定(self):
        self.click_element(self.loc_上线申请确定)
        return self

    def click_下架(self):
        self.click_element(self.loc_下架)
        return self

    def send_下架原因(self, reason):
        self.send_keys(self.loc_下架原因, reason)
        return self

    def click_下架确定(self):
        self.click_element(self.loc_下架确定)
        return self

    def click_详情(self):
        self.click_element(self.loc_详情)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)


class Page_Community_roles(SeleniumBase):
    '''这个爱问大后台--社区管理--社区角色页面'''
    # loc_标题 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[3]/div')
    # loc_文章状态 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[8]/div')
    # loc_文章类型 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[7]/div')
    # loc_医生姓名 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[5]/div')
    # loc_查看 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[14]/div/button[1]')
    # loc_删除 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[14]/div/button[2]')
    #
    # # loc_系统设置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[6]/div[2]/p[3]')
    # # loc_内容管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[7]/div[2]/p[3]')
    # # loc_频道管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[8]/div[2]/p[3]')
    # # loc_iask运营管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[9]/div[2]/p[3]')
    # loc_消息 = (By.XPATH, '/html/body/div[3]/p')
    #
    # def get_列表第一行_标题(self):
    #     return self.get_element_text(self.loc_标题)
    #
    # def get_列表第一行_文章状态(self):
    #     return self.get_element_text(self.loc_文章状态)
    #
    # def get_列表第一行_文章类型(self):
    #     return self.get_element_text(self.loc_文章类型)
    #
    # def get_列表第一行_医生姓名(self):
    #     return self.get_element_text(self.loc_医生姓名)
    #
    # def click_查看(self):
    #     self.mouse_over_click(self.loc_查看)
    #     return self
    #
    # def click_删除(self):
    #     self.click_element(self.loc_删除)
    #     return self
    #
    # def get_消息(self):
    #     return self.get_element_text(self.loc_消息)


class Page_Application_Overview(SeleniumBase):
    '''这个爱问大后台--应用管理--应用总览页面'''
    loc_应用总览 = (By.XPATH, '//div[1]/div/div/div/div[1]/ul/li[1]')
    loc_专题 = (By.XPATH, '//div[1]/div/div/div/div[1]/ul/li[2]')
    loc_科普文章 = (By.XPATH, '//div[1]/div/div/div/div[1]/ul/li[3]')
    loc_贴吧 = (By.XPATH, '//div[1]/div/div/div/div[1]/ul/li[4]')
    loc_新闻广告 = (By.XPATH, '//div[1]/div/div/div/div[1]/ul/li[5]')
    loc_社区分享 = (By.XPATH, '//div[1]/div/div/div/div[1]/ul/li[6]')
    loc_活动推广 = (By.XPATH, '//div[1]/div/div/div/div[1]/ul/li[7]')

    # loc_系统设置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[6]/div[2]/p[3]')
    # loc_内容管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[7]/div[2]/p[3]')
    # loc_频道管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[8]/div[2]/p[3]')
    # loc_iask运营管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[9]/div[2]/p[3]')
    # loc_消息 = (By.XPATH, '/html/body/div[3]/p')
    #
    # def get_列表第一行_标题(self):
    #     return self.get_element_text(self.loc_标题)
    #
    # def get_列表第一行_文章状态(self):
    #     return self.get_element_text(self.loc_文章状态)
    #
    # def get_列表第一行_文章类型(self):
    #     return self.get_element_text(self.loc_文章类型)
    #
    # def get_列表第一行_医生姓名(self):
    #     return self.get_element_text(self.loc_医生姓名)
    #
    # def click_查看(self):
    #     self.mouse_over_click(self.loc_查看)
    #     return self
    #
    # def click_删除(self):
    #     self.click_element(self.loc_删除)
    #     return self
    #
    # def get_消息(self):
    #     return self.get_element_text(self.loc_消息)


class Page_Project(SeleniumBase):
    '''这个爱问大后台--应用管理--专题页面'''
    loc_功能介绍 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[1]')
    loc_修改 = (By.XPATH, '//div[2]/div/div/div/div[1]/div/button')
    loc_专题列表 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[2]')
    # loc_医生姓名 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[5]/div')
    # loc_查看 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[14]/div/button[1]')
    # loc_删除 = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[14]/div/button[2]')

    # loc_系统设置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[6]/div[2]/p[3]')
    # loc_内容管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[7]/div[2]/p[3]')
    # loc_频道管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[8]/div[2]/p[3]')
    # loc_iask运营管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/section/div[9]/div[2]/p[3]')
    # loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    # def get_列表第一行_标题(self):
    #     return self.get_element_text(self.loc_标题)
    #
    # def get_列表第一行_文章状态(self):
    #     return self.get_element_text(self.loc_文章状态)
    #
    # def get_列表第一行_文章类型(self):
    #     return self.get_element_text(self.loc_文章类型)
    #
    # def get_列表第一行_医生姓名(self):
    #     return self.get_element_text(self.loc_医生姓名)
    #
    # def click_查看(self):
    #     self.mouse_over_click(self.loc_查看)
    #     return self
    #
    # def click_删除(self):
    #     self.click_element(self.loc_删除)
    #     return self
    #
    # def get_消息(self):
    #     return self.get_element_text(self.loc_消息)


class Page_Science_Article(SeleniumBase):
    '''这个爱问大后台--应用管理--科普文章页面'''
    loc_功能介绍 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[1]')
    loc_修改 = (By.XPATH, '//div[2]/div/div/div/div[1]/div/button')
    loc_文章列表 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[2]')

    # loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    # def get_标题(self):
    #     return self.get_element_text(self.loc_标题)
    #
    # def get_文章内容(self):
    #     return self.get_element_text(self.loc_文章内容)
    #
    # def click_删除(self):
    #     self.click_element(self.loc_删除按钮)
    #     return self
    #
    # def click_确定删除(self):
    #     self.click_element(self.loc_确定删除)
    #     return self


class Page_Postbar(SeleniumBase):
    '''这个爱问大后台--应用管理--贴吧页面'''
    loc_功能介绍 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[1]')
    loc_修改 = (By.XPATH, '//div[2]/div/div/div/div[1]/div/button')
    loc_贴吧列表 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[2]')

    # loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    # def get_标题(self):
    #     return self.get_element_text(self.loc_标题)
    #
    # def get_文章内容(self):
    #     return self.get_element_text(self.loc_文章内容)
    #
    # def click_删除(self):
    #     self.click_element(self.loc_删除按钮)
    #     return self
    #
    # def click_确定删除(self):
    #     self.click_element(self.loc_确定删除)
    #     return self


class Page_Press_release(SeleniumBase):
    '''这个爱问大后台--应用管理--新闻公告页面'''
    loc_功能介绍 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[1]')
    loc_修改 = (By.XPATH, '//div[2]/div/div/div/div[1]/div/button')

    # loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    # def get_标题(self):
    #     return self.get_element_text(self.loc_标题)
    #
    # def get_文章内容(self):
    #     return self.get_element_text(self.loc_文章内容)
    #
    # def click_删除(self):
    #     self.click_element(self.loc_删除按钮)
    #     return self
    #
    # def click_确定删除(self):
    #     self.click_element(self.loc_确定删除)
    #     return self


class Page_Community_Share(SeleniumBase):
    '''这个爱问大后台--应用管理--社区分享页面'''
    loc_功能介绍 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[1]')
    loc_修改 = (By.XPATH, '//div[2]/div/div/div/div[1]/div/button')

    # loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    # def get_标题(self):
    #     return self.get_element_text(self.loc_标题)
    #
    # def get_文章内容(self):
    #     return self.get_element_text(self.loc_文章内容)
    #
    # def click_删除(self):
    #     self.click_element(self.loc_删除按钮)
    #     return self
    #
    # def click_确定删除(self):
    #     self.click_element(self.loc_确定删除)
    #     return self


class Page_Event_Promotion(SeleniumBase):
    '''这个爱问大后台--应用管理--活动推广页面'''
    loc_功能介绍 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[1]')
    loc_修改 = (By.XPATH, '//div[2]/div/div/div/div[1]/div/button')
    loc_活动推广列表 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[2]')

    # loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    # def get_标题(self):
    #     return self.get_element_text(self.loc_标题)
    #
    # def get_文章内容(self):
    #     return self.get_element_text(self.loc_文章内容)
    #
    # def click_删除(self):
    #     self.click_element(self.loc_删除按钮)
    #     return self
    #
    # def click_确定删除(self):
    #     self.click_element(self.loc_确定删除)
    #     return self


class Page_System_update(SeleniumBase):
    '''这个爱问大后台--消息管理--系统更新消息页面'''
    loc_新建消息 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[1]')
    # loc_修改 = (By.XPATH, '//div[2]/div/div/div/div[1]/div/button')
    # loc_活动推广列表 = (By.XPATH, '//div[2]/div/div/div/div[1]/ul/li[2]')

    # loc_消息 = (By.XPATH, '/html/body/div[3]/p')

    # def get_标题(self):
    #     return self.get_element_text(self.loc_标题)
    #
    # def get_文章内容(self):
    #     return self.get_element_text(self.loc_文章内容)
    #
    # def click_删除(self):
    #     self.click_element(self.loc_删除按钮)
    #     return self
    #
    # def click_确定删除(self):
    #     self.click_element(self.loc_确定删除)
    #     return self
