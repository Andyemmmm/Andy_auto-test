#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/3/10 16:39
# @File     : audit_management.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Common.selenium_library import SeleniumBase


class Page_Community_qualification_audit(SeleniumBase):
    '''这个爱问大后台--审核管理--社区资质审核页面'''
    loc_社区资质审核 = (By.XPATH, '//div[1]/div/div/div/div[1]/ul/li[1]/span')
    loc_社区上线申请 = (By.XPATH, '//div[1]/div/div/div/div[1]/ul/li[2]/span')
    loc_社区名称 = (By.XPATH, '//input[@placeholder="请输入社区名称"]')
    loc_审核状态 = (By.XPATH, '//input[@placeholder="全部"]')
    loc_状态_全部 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span")
    loc_状态_审核未通过 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[2]/span")
    loc_状态_审核通过 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[3]/span")
    loc_状态_待审核 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[4]/span")
    loc_状态_未认证 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[5]/span")
    loc_搜索 = (By.XPATH, "//span[text()='搜索']")
    loc_清除 = (By.XPATH, "//span[text()='清除']")
    loc_第一行通过 = (By.XPATH, '//div[4]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button[2]/span')
    loc_通过 = (By.XPATH,
              '//*[@id="app"]/section/section/main/div/div/div[1]/div/div/div/div[2]/section/div/div[1]/div[4]/div[1]/div[4]/div[2]/table/tbody/tr/td[10]/div/button[2]/span')
    loc_认证通过_确定 = (By.XPATH, '//div[@role="dialog"]//button[2]')
    loc_查看 = (By.XPATH,
              '//*[@id="app"]/section/section/main/div/div/div[1]/div/div/div/div[2]/section/div/div[1]/div[4]/div[1]/div[4]/div[2]/table/tbody/tr/td[10]/div/button[1]/span')
    loc_不通过 = (By.XPATH,
               '//*[@id="app"]/section/section/main/div/div/div[1]/div/div/div/div[2]/section/div/div[1]/div[4]/div[1]/div[4]/div[2]/table/tbody/tr/td[10]/div/button[3]/span')
    loc_不通过原因 = (By.XPATH,
                 '//*[@id="app"]/section/section/main/div/div/div[1]/div/div/div/div[2]/section/div/div[2]/div/div[2]/div/form/div/div/div/div[1]/div/input')
    loc_不通过_确定 = (By.XPATH, '//div[2]/section/div/div[2]//div[@class="el-dialog__footer"]//span[text()="确认"]')
    loc_不通过_自定义原因 = (By.XPATH, '//span[@class="el-checkbox__inner"]')
    loc_不通过_自定义原因_输入框 = (By.XPATH, '//textarea[@placeholder="请输入理由，信息将反馈给社区管理员。"]')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def click_社区资质审核(self):
        self.mouse_over_click(self.loc_社区资质审核)
        return self

    def click_社区上线申请(self):
        self.mouse_over_click(self.loc_社区上线申请)
        return self

    def send_社区名称(self, name):
        self.send_keys(self.loc_社区名称, name)
        return self

    def click_审核状态(self):
        self.click_element(self.loc_审核状态)
        return self

    def click_状态全部(self):
        self.mouse_over_click(self.loc_状态_全部)
        return self

    def click_状态审核未通过(self):
        self.mouse_over_click(self.loc_状态_审核未通过)
        return self

    def click_状态审核通过(self):
        self.mouse_over_click(self.loc_状态_审核通过)
        return self

    def click_状态待审核(self):
        self.mouse_over_click(self.loc_状态_待审核)
        return self

    def click_状态未认证(self):
        self.mouse_over_click(self.loc_状态_未认证)
        return self

    def click_清除(self):
        self.click_element(self.loc_清除)
        return self

    def click_搜索(self):
        self.mouse_over_click(self.loc_搜索)
        return self

    def click_第一行通过(self):
        self.click_element(self.loc_第一行通过)
        return self

    def click_通过(self):
        self.click_element(self.loc_通过)
        return self

    def click_通过确定(self):
        self.click_element(self.loc_认证通过_确定)
        return self

    def click_不通过(self):
        self.click_element(self.loc_不通过)
        return self

    def click_不通过原因(self):
        self.click_element(self.loc_不通过原因)
        return self

    def select_不通过原因(self, cause):
        try:
            ele = self.driver.find_element_by_xpath(
                f'/html/body/script[4]/following-sibling::div[2]/div//ul/li/span[text()="{cause}"]')
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        except:
            print('没有此选项，系统默认选择')
            ele = self.driver.find_element_by_xpath('/html/body/script[4]/following-sibling::div[2]/div//ul/li[1]')
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()

    def click_自定义原因(self):
        self.click_element(self.loc_不通过_自定义原因)
        return self

    def send_自定义原因(self, reason):
        self.send_keys(self.loc_不通过_自定义原因_输入框, reason)
        return self

    def click_不通过确定(self):
        self.click_element(self.loc_不通过_确定)
        return self

    def click_查看(self):
        self.click_element(self.loc_查看)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)


class Page_Community_online_application(SeleniumBase):
    '''这个爱问大后台--审核管理--社区上线申请页面'''
    loc_社区名称 = (By.XPATH, '//input[@placeholder="请输入社区名称"]')
    loc_审核状态 = (By.XPATH, '//input[@placeholder="全部"]')
    loc_状态_全部 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span")
    loc_状态_审核不通过 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[2]/span")
    loc_状态_审核通过 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[3]/span")
    loc_状态_待审核 = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[4]/span")
    loc_搜索 = (By.XPATH, "//span[text()='搜索']")
    loc_清除 = (By.XPATH, "//span[text()='清除']")
    loc_查看 = (By.XPATH, '//div[4]/div[1]/div[4]/div[2]/table/tbody/tr/td[11]/div/button[1]/span')
    loc_通过 = (By.XPATH, '//div[4]/div[1]/div[4]/div[2]/table/tbody/tr/td[11]/div/button[2]/span')
    loc_第一行通过 = (By.XPATH, '//div[4]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[11]/div/button[2]/span')
    loc_上线通过_确定 = (By.XPATH, '//div[@role="dialog"]//button[2]')
    loc_不通过 = (By.XPATH, '//div[4]/div[1]/div[4]/div[2]/table/tbody/tr/td[11]/div/button[3]/span')
    loc_不通过原因_输入框 = (By.XPATH, '//textarea[@placeholder="请输入拒绝理由，信息将反馈给社区管理员。"]')
    loc_不通过确定 = (By.XPATH, '//div[2]/section/div/div[2]//div[@class="el-dialog__footer"]//span[text()="确认"]')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def send_社区名称(self, name):
        self.send_keys(self.loc_社区名称, name)
        return self

    def click_审核状态(self):
        self.click_element(self.loc_审核状态)
        return self

    def click_状态全部(self):
        self.mouse_over_click(self.loc_状态_全部)
        return self

    def click_状态审核未通过(self):
        self.mouse_over_click(self.loc_状态_审核不通过)
        return self

    def click_状态审核通过(self):
        self.mouse_over_click(self.loc_状态_审核通过)
        return self

    def click_状态待审核(self):
        self.mouse_over_click(self.loc_状态_待审核)
        return self

    def click_清除(self):
        self.click_element(self.loc_清除)
        return self

    def click_搜索(self):
        self.mouse_over_click(self.loc_搜索)
        return self

    def click_查看(self):
        self.click_element(self.loc_查看)
        return self

    def click_通过(self):
        self.click_element(self.loc_通过)
        return self

    def click_第一行通过(self):
        self.click_element(self.loc_第一行通过)
        return self

    def click_通过确定(self):
        self.click_element(self.loc_上线通过_确定)
        return self

    def click_不通过(self):
        self.click_element(self.loc_不通过)
        return self

    def send_不通过原因(self, reason):
        self.send_keys(self.loc_不通过原因_输入框, reason)
        return self

    def click_不通过确定(self):
        self.click_element(self.loc_不通过确定)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)
