#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/25 10:20
# @File     : page_Network_management.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Network_management(SeleniumBase):
    '''
    这个是圈子论坛模块--圈子管理页面
    '''

    loc_圈子管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[1]')
    loc_回帖管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[2]')
    loc_圈主_医生设置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[3]')
    loc_帖子标签管理 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/ul/li[4]')
    loc_搜索框 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[1]/div/div/div/input')
    loc_返回结果 = (By.XPATH, '/html/body/div[3]/p')

    loc_帖子类型_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[1]')
    loc_帖子类型_普通贴 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[2]')
    loc_帖子类型_精华帖 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[1]/ul/li[3]')

    loc_是否推荐_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[1]')
    loc_是否推荐_是 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[2]')
    loc_是否推荐_否 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[2]/ul/li[3]')

    loc_是否置顶_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[3]/ul/li[1]')
    loc_是否置顶_是 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[3]/ul/li[2]')
    loc_是否置顶_否 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[3]/ul/li[3]')

    loc_创建日期_全部 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/ul/li[1]')
    loc_创建日期_今日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/ul/li[2]')
    loc_创建日期_昨日 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/ul/li[3]')
    loc_创建日期_本周 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/ul/li[4]')
    loc_创建日期_本月 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/div[4]/ul/li[5]')

    loc_清空筛选条件 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[2]/button/span')

    loc_帖子类型_值 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr/td[4]/div')

    loc_帖子类型的值 = '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr/td[4]/div'
    loc_是否推荐的值 = '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr/td[5]/div'
    lco_是否置顶的值 = '//*[@id="app"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr/td[6]/div'

    def click__圈子管理(self):
        self.mouse_over_click(self.loc_圈子管理)
        return self

    def click_回帖管理(self):
        self.click_element(self.loc_回帖管理)
        return self

    def click_圈主_医生设置(self):
        self.click_element(self.loc_圈主_医生设置)
        return self

    def click_帖子标签管理(self):
        self.click_element(self.loc_帖子标签管理)
        return self

    def get_返回结果(self):
        return self.get_element_text(self.loc_返回结果)

    def send_搜索框(self, content):
        self.send_element_key(self.loc_搜索框, content)

    def click_帖子类型_全部(self):
        self.click_element(self.loc_帖子类型_全部)
        return self

    def click_帖子类型_普通贴(self):
        self.click_element(self.loc_帖子类型_普通贴)
        return self

    def click_帖子类型_精华帖(self):
        self.click_element(self.loc_帖子类型_精华帖)
        return self

    def click_是否推荐_全部(self):
        self.click_element(self.loc_是否推荐_全部)
        return self

    def click_是否推荐_是(self):
        self.click_element(self.loc_是否推荐_是)
        return self

    def click_是否推荐_否(self):
        self.click_element(self.loc_是否推荐_否)
        return self

    def click_是否置顶_全部(self):
        self.click_element(self.loc_是否置顶_全部)
        return self

    def click_是否置顶_是(self):
        self.click_element(self.loc_是否置顶_是)
        return self

    def click_是否置顶_否(self):
        self.click_element(self.loc_是否置顶_否)
        return self

    def click_创建日期_全部(self):
        self.click_element(self.loc_创建日期_全部)
        return self

    def click_创建日期_今日(self):
        self.click_element(self.loc_创建日期_今日)
        return self

    def click_创建日期_昨日(self):
        self.click_element(self.loc_创建日期_昨日)
        return self

    def click_创建日期_本周(self):
        self.click_element(self.loc_创建日期_本周)
        return self

    def click_创建日期_本月(self):
        self.click_element(self.loc_创建日期_本月)
        return self

    def click_清空筛选条件(self):
        self.click_element(self.loc_清空筛选条件)
        return self

    def find_number(self, locator):
        L = []
        if locator == '帖子类型':
            eles = self.driver.find_elements_by_xpath(self.loc_帖子类型的值)
        if locator == '是否推荐':
            eles = self.driver.find_elements_by_xpath(self.loc_是否推荐的值)
        if locator == '是否置顶':
            eles = self.driver.find_elements_by_xpath(self.lco_是否置顶的值)
        for ele in eles:
            L.append(ele.text)
        return L
