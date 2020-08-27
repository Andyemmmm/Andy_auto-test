#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/3 10:44
# @File     : page_updatearticle.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
import time
from Common.selenium_library import SeleniumBase


class Page_UpdateArticle(SeleniumBase):
    '''这个是健康科普写文章的页面'''
    loc_iframe = ('ueditor_1')
    loc_输入框 = (By.XPATH, '/html/body')
    loc_下一步 = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/a[1]')

    def switch_iframe(self):
        self.switch_to_frame(self.loc_iframe)
        return self

    def send_输入框(self, content):
        self.send_keys(self.loc_输入框, content)
        return self

    def click_下一步(self):
        self.mouse_over_click(self.loc_下一步)


class Page_UpdateArticle_nextstep(SeleniumBase):
    '''这个是健康科普--写文章下一步的页面'''
    loc_文章标题 = (By.XPATH, '//*[@id="diaryTitle"]')
    loc_文章类别 = (By.XPATH, '//*[@id="deptName"]')
    loc_文章标签 = (By.XPATH, '/html/body/div[3]/div[2]/dl/dd[3]/div[2]')
    loc_文章标签_选项1 = (By.XPATH, '/html/body/div[3]/div[2]/dl/dd[3]/div[3]/div[2]/div/a[1]')
    loc_文章标签_选项2 = (By.XPATH, '/html/body/div[3]/div[2]/dl/dd[3]/div[3]/div[2]/div/a[2]')
    loc_空白 = (By.XPATH, '/html/body/div[3]/div[2]/dl/dd[3]/div[3]')
    lco_上传图片 = (By.XPATH, '//*[@id="xxupimg"]')
    loc_裁切框 = (By.XPATH, '//*[@id="preview"]/div/div[1]/div[1]/div[5]')
    loc_裁切确定 = (By.XPATH, '/html/body/div[15]/div[3]/a[1]')
    loc_下一步 = (By.ID, 'next')

    def send_文章标题(self, title):
        self.send_keys(self.loc_文章标题, title)
        return self

    def click_文章标签(self):
        self.mouse_over_click(self.loc_文章标签)
        return self

    def click_文章标签_选项1(self):
        self.mouse_over_click(self.loc_文章标签_选项1)
        return self

    def click_文章标签_选项2(self):
        self.mouse_over_click(self.loc_文章标签_选项2)
        return self

    def click_空白(self):
        self.click_element(self.loc_空白)
        return self

    def send_图片(self, png):
        self.send_png(self.lco_上传图片, png)
        return self

    def offset_裁切(self):
        self.by_offset(self.loc_裁切框)
        return self

    def click_裁切确定(self):
        self.click_element(self.loc_裁切确定)
        return self

    def click_下一步(self):
        self.click_element(self.loc_下一步)
        return self


class Page_UpdateArticle_timestep(SeleniumBase):
    '''这个是写文章发布时间设置的页面'''
    loc_日期框 = (By.XPATH, '//*[@id="date"]')
    loc_下一步 = (By.ID, 'next')
    loc_今日 = (By.XPATH, '/html/body/div[11]/div[3]/table/tfoot/tr/th')
    loc_今天 = (By.XPATH, "//td[contains(@class,'day today')]")
    loc_当前时间 = (By.XPATH, "//div[@class='datetimepicker-hours']//span[contains(@class,'hour active')]")
    lco_当前分钟 = (By.XPATH, "//div[@class='datetimepicker-minutes']//span[contains(@class,'minute active')]")
    th_prev = (By.XPATH, '/html/body/div/div[1]/table/thead/tr/th[1]')
    th_next = (By.XPATH, '/html/body/div/div[1]/table/thead/tr/th[3]')
    loc_翻页第一个 = (By.XPATH, '/html/body/div/div[1]/table/tbody/tr/td/span[1]')

    def click_日期框(self):
        self.click_element(self.loc_日期框)
        return self

    def click_下一步(self):
        self.mouse_over_click(self.loc_下一步)
        return self

    def click_今日(self):
        self.mouse_over_click(self.loc_今日)
        return self

    def scr_date(self, date, H, M):
        '''
        选择定时发布文章时间的方法
        :param date: 日期   格式：1-9，10-31
        :param H: 小时      格式：0:00
        :param M: 分        格式：H:00-H:55
        :return: None
        '''
        da = self.get_element_text(self.loc_今天)
        if date == da:
            self.driver.find_element_by_xpath(f"//td[text()={date} and contains(@class,'day today')]").click()
            time.sleep(0.5)
            try:
                self.driver.find_element_by_xpath(f"//div[@class='datetimepicker-hours']//span[text()='{H}']").click()
                time.sleep(0.5)
            except:
                self.click_element(self.loc_当前时间)

            try:
                self.driver.find_element_by_xpath(f"//div[@class='datetimepicker-minutes']//span[text()='{M}']").click()
                time.sleep(1)
            except:
                self.click_element(self.lco_当前分钟)

        else:
            self.driver.find_element_by_xpath("//td[contains(@class,'day today')]/following-sibling::td[1]").click()
            time.sleep(0.5)
            try:
                self.driver.find_element_by_xpath(f"//div[@class='datetimepicker-hours']//span[text()='{H}']").click()
                time.sleep(0.5)
            except:
                self.click_element(self.loc_当前时间)

            try:
                self.driver.find_element_by_xpath(f"//div[@class='datetimepicker-minutes']//span[text()='{M}']").click()
                time.sleep(1)
            except:
                self.click_element(self.lco_当前分钟)

        return self


class Page_UpdateArticle_ditchstep(SeleniumBase):
    '''这个是写文章设置渠道授权的页面'''

    loc_发布 = (By.XPATH, '//*[@id="next"]')
    loc_同步到微博 = (By.XPATH, '/html/body/div[3]/div[1]/div/div[3]/div[3]/div[2]/input')

    def see_发布(self):
        self.ex_script(self.loc_发布)
        return self

    def ckick_发布(self):
        self.click_element(self.loc_发布)
        return self

    def click_同步到微博(self):
        self.click_element(self.loc_同步到微博)
        return self


class Page_UpdateArticle_success(SeleniumBase):
    '''这个是写文章发布成功的页面'''

    loc_再写一篇 = (By.ID, 'next')
    loc_消息 = (By.XPATH, '/html/body/div[3]/div/div[3]/div[1]')
    loc_文章名称 = (By.XPATH, '/html/body/div[3]/div/div[3]/div[3]/a')

    def see_下一步(self):
        self.click_element(self.loc_再写一篇)

    def get_消息(self):
        return self.get_element_text(self.loc_消息)

    def get_文章名称(self):
        return self.get_element_text(self.loc_文章名称)
