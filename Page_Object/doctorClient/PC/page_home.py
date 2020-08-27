#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/3 9:55
# @File     : page_home.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Home(SeleniumBase):
    '''这个医端首页'''
    loc_首页 = (By.XPATH, '//*[@id="sideMenu"]/dl[1]/dt/a')
    loc_我的视频 = (By.XPATH, '//*[@id="sideMenu"]/dl[2]/dd/ul/li[1]/a')
    loc_文章发布 = (By.XPATH, '//*[@id="sideMenu"]/dl[2]/dd/ul/li[2]/a')
    loc_品牌推广 = (By.XPATH, '//*[@id="sideMenu"]/dl[2]/dd/ul/li[3]/a')
    loc_专题活动 = (By.XPATH, '//*[@id="sideMenu"]/dl[2]/dd/ul/li[4]/a')
    loc_流量市场 = (By.XPATH, '//*[@id="sideMenu"]/dl[2]/dd/ul/li[5]/a')
    loc_公益咨询 = (By.XPATH, '//*[@id="sideMenu"]/dl[2]/dd/ul/li[6]/a')
    loc_访谈节目 = (By.XPATH, '//*[@id="sideMenu"]/dl[2]/dd/ul/li[7]/a')
    loc_好友互推 = (By.XPATH, '//*[@id="sideMenu"]/dl[2]/dd/ul/li[8]/a')
    loc_品牌学院 = (By.XPATH, '//*[@id="sideMenu"]/dl[2]/dd/ul/li[9]/a')

    loc_图文咨询 = (By.XPATH, '//*[@id="sideMenu"]/dl[3]/dd/ul/li[1]/a')
    loc_门诊预约 = (By.XPATH, '//*[@id="sideMenu"]/dl[3]/dd/ul/li[2]/a')
    loc_商业活动 = (By.XPATH, '//*[@id="sideMenu"]/dl[3]/dd/ul/li[3]/a')
    loc_服务评价 = (By.XPATH, '//*[@id="sideMenu"]/dl[3]/dd/ul/li[4]/a')

    loc_我的患者 = (By.XPATH, '//*[@id="sideMenu"]/dl[4]/dd/ul/li[1]/a')
    loc_我的社区 = (By.XPATH, '//*[@id="sideMenu"]/dl[4]/dd/ul/li[2]/a')

    loc_用户分析 = (By.XPATH, '//*[@id="sideMenu"]/dl[5]/dd/ul/li[1]/a')
    loc_文章分析 = (By.XPATH, '//*[@id="sideMenu"]/dl[5]/dd/ul/li[2]/a')
    loc_收入分析 = (By.XPATH, '//*[@id="sideMenu"]/dl[5]/dd/ul/li[3]/a')

    loc_广告投放 = (By.XPATH, '//*[@id="sideMenu"]/dl[6]/dd/ul/li/a')

    loc_专题活动_第一行数据 = (By.XPATH, '//*[@id="bns_list"]/ul/li[1]/div/a')
    loc_专题详情_去写文章 = (By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div[4]/a')
    loc_发布健康科普 = (By.XPATH, '//*[@id="use_layer2"]/div[2]/a[1]')
    loc_发布诊间日记 = (By.XPATH, '//*[@id="use_layer2"]/div[2]/a[2]')
    loc_发布病例分析 = (By.XPATH, '//*[@id="use_layer2"]/div[2]/a[3]')

    loc_品牌推广_社区活动 = (By.XPATH, '//*[@id="communityTask"]')
    loc_去完成 = (By.XPATH, '//*[@id="community_list"]/ul/li[1]/a[2]')
    loc_立即投稿 = (By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/c/a')

    def click_专题活动(self):
        self.click_element(self.loc_专题活动)
        return self

    def click_品牌推广(self):
        self.click_element(self.loc_品牌推广)
        return self

    def click_文章发布(self):
        self.click_element(self.loc_文章发布)
        return self

    def click_去完成(self):
        self.click_element(self.loc_去完成)
        return self

    def click_立即投稿(self):
        self.click_element(self.loc_立即投稿)
        return self

    def click_专题活动_第一行数据(self):
        self.click_element(self.loc_专题活动_第一行数据)
        return self

    def click_专题详情_写文章(self):
        self.click_element(self.loc_专题详情_去写文章)
        return self

    def click_发布健康科普(self):
        self.mouse_over_click(self.loc_发布健康科普)

    def click_发布诊间日记(self):
        self.mouse_over_click(self.loc_发布诊间日记)

    def click_发布病例分析(self):
        self.mouse_over_click(self.loc_发布病例分析)

    def click_品牌推广_社区活动(self):
        self.click_element(self.loc_品牌推广_社区活动)
        return self

    #
    # def click_设置(self):
    #     self.click_element(self.loc_设置)
    #
    # def get_获取社区名(self):
    #     return self.get_element_text(self.loc_社区名)

    def get_信息(self):
        return self.get_element_text(self.loc_首页)
