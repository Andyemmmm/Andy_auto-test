#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/5/14 19:26
# @File     : iw_data_collect.py
# @Software : aiwen_ui


from Common.selenium_library import SeleniumBase
import time


class Iw_data_collect(SeleniumBase):
    """数据打点测试类"""

    def click_event_back(self, button, num=1):
        """
        点击事件的测试方法（点击按钮跳转的）
        :param button:  埋点元素
        :param num:     点击策略
        :return:
        """
        if num > 1:
            for i in range(num):
                self.click_element(button)
                time.sleep(1)
                self.driver.back()
                time.sleep(0.5)
                # self.driver.implicitly_wait(6)
        else:
            self.click_element(button)
            self.driver.back()
        return self

    def click_event(self, button, num=1):
        """
        点击事件的测试方法（点击按钮不跳转的）
        :param button:   埋点元素
        :param num:      点击策略
        :return:
        """
        if num > 1:
            for i in range(num):
                self.click_element(button)
                time.sleep(0.5)
        else:
            self.click_element(button)
        return self

    def click_event_double(self, button, num=1, setp1=None, setp2=None, setp3=None):
        """
        点击事件的测试方法（点击按钮两次，针对下拉筛选的按钮）
        :param button:   埋点元素
        :param num:      点击策略
        :param setp1:    步骤1
        :param setp2:    步骤2
        :param setp3:    步骤3
        :return:
        """
        if num > 1:
            for i in range(num):
                self.click_element(button)
                time.sleep(0.5)
                if setp1:
                    time.sleep(0.5)
                    self.click_element(setp1)
                    if setp2:
                        time.sleep(0.5)
                        self.click_element(setp2)
                    if setp3:
                        time.sleep(0.5)
                        self.click_element(setp3)
                else:
                    self.click_element(button)
        else:
            self.click_element(button)
            time.sleep(0.5)
            if setp1:
                time.sleep(0.5)
                self.click_element(setp1)
                if setp2:
                    time.sleep(0.5)
                    self.click_element(setp2)
                if setp3:
                    time.sleep(0.5)
                    self.click_element(setp3)
            else:
                self.click_element(button)
        return self

    def click_search_event(self, content, button, num=None):
        """
        搜索框点击事件的测试方法
        :param content:  用户输入内容
        :param button:   埋点元素
        :param num:     点击策略
        :return:
        """
        if num:
            for i in range(num):
                self.send_keys(content)
                self.click_element(button)
                self.driver.back()
        else:
            self.click_element(button)
        return self

    def remain_event(self, url, num, stay=None):
        """
        停留事件的测试方法
        :param url:     页面url
        :param num:     停留策略
        :param stay:       停留时间
        :return:
        """
        if num:
            for i in range(num):
                self.get(url)
                if stay:
                    time.sleep(stay)
        else:
            self.get(url)
            if stay:
                time.sleep(stay)
        return self

    def feed_event(self, url, num=None):
        """
        feed流展现量的测试方法
        :param url:     页面url
        :param num:     策略
        :return:
        """
        if num:
            for i in range(num):
                self.get(url)
        else:
            self.get(url)
        return self
