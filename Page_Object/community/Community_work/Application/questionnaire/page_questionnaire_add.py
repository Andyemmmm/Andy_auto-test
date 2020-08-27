#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/23 16:57
# @File     : page_questionnaire_add.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Questionnaire_add(SeleniumBase):
    '''
    这个是调查问卷模块--新建调查问卷页面
    '''

    loc_问卷标题 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/input')
    loc_问卷描述 = (
        By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[3]/div/textarea')
    loc问卷图片 = (
        By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[5]/div/div[1]/input')
    loc_问卷card封面 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[7]/div/div[1]/input')
    loc_问卷card封面_裁切确定 = (By.XPATH, '/html/body/div[2]/div/div[3]/span/button[2]/span')
    loc_问卷备注 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[8]/div/textarea')

    loc_组件_单选题 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/ul/div/li[1]/span')
    loc_组件_多选题 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/ul/div/li[2]/span')
    loc_组件_图片 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/ul/div/li[3]/span')
    loc_单行文本题 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/ul/div/li[4]/span')
    loc_多行文本题 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/ul/div/li[5]/span')
    loc_富文本 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/ul/div/li[6]/span')
    loc_提交 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/ul/div/li[7]/span')
    loc_图片_Card = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/ul/div/li[8]/span')
    loc_医生_Card = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/ul/div/li[9]/span')

    loc_单选题_标题 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/input')
    loc_单选题_内容1 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/ul/li[1]/div[1]/input')
    loc_单选题_图片1 = (By.NAME, '0')
    loc_单选题_内容2 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/ul/li[2]/div[1]/input')
    loc_单选题_图片2 = (By.NAME, '1')
    loc_单选题_内容3 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/ul/li[3]/div[1]/input')
    loc_单选题_图片3 = (By.NAME, '2')

    loc_多选题_标题 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/input')
    loc_多选题_内容1 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/ul/li[1]/div[1]/input')
    loc_多选题_图片1 = (By.NAME, '0')
    loc_多选题_内容2 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/ul/li[2]/div[1]/input')
    loc_多选题_图片2 = (By.NAME, '1')
    loc_多选题_内容3 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/ul/li[3]/div[1]/input')
    loc_多选题_图片3 = (By.NAME, '2')

    loc_图片_上传 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/input')
    loc_图片_描述 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/textarea')

    loc_单行文本题_标题 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/input')
    loc_单行文本题_描述 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/textarea')
    loc_单行文本题_图片 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[3]/div/div[1]/input')
    loc_单行文本题_提示文字 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[4]/div/textarea')

    loc_多行文本题_标题 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/input')
    loc_多行文本题_描述 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/textarea')
    loc_多行文本题_图片 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[3]/div/div[1]/input')
    loc_多行文本题_提示文字 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[4]/div/textarea')

    loc_富文本_frame = ('ueditor_0')
    loc_富文本框内容 = (By.XPATH, '/html/body')

    loc_提交_文案 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/input')
    loc_提交_是吸底 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/label[1]/span[1]/span')
    loc_提交_否吸底 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/label[2]/span[1]/input')

    loc_图片_Card_文案 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/input')
    loc_图片_Card_复制内容 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[3]/div/input')

    loc_医生_Card_医生姓名 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/input')
    loc_医生_Card_职称 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/input')
    loc_医生_Card_医院 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[3]/div/input')
    loc_医生_Card_擅长 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[4]/div/input')
    loc_医生_Card_按钮文字 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[5]/div/input')
    loc_医生_Card_头像 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[6]/div/div[1]/input')
    loc_医生_Card_头像_裁切确定 = (By.XPATH, '/html/body/div[4]/div/div[3]/span/button[2]/span')
    loc_医生_Card_按钮点击效果_链接 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[7]/div/label[1]/span[1]/span')
    loc_医生_Card_按钮点击效果_弹层提问 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[7]/div/label[2]/span[1]/span')
    loc_医生_Card_URL = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[8]/div/input')
    loc_错误提示 = (By.XPATH, '/html/body/div[7]/p')
    loc_投放成功 = (By.XPATH, '/html/body/div[6]/div/div[1]/div')

    loc_保存 = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/button[3]/span')
    lco_确定投放 = (By.XPATH, '/html/body/div[5]/div/div[3]/button[2]/span')
    loc_投放 = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/button[4]/span')
    lco_取消 = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/button[1]/span')
    loc_预览 = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/button[2]/span')

    def send_问卷标题(self, title):
        self.send_keys(self.loc_问卷标题, title)
        return self

    def send_问卷描述(self, describe):
        self.send_keys(self.loc_问卷描述, describe)
        return self

    def send_问卷图片(self, png):
        self.send_keys(self.loc问卷图片, png)
        return self

    def send_问卷card封面(self, cover):
        self.send_keys(self.loc_问卷card封面, cover)
        return self

    def click_问卷card封面_裁切确定(self):
        self.click_element(self.loc_问卷card封面_裁切确定)
        return self

    def send_问卷备注(self, remark):
        self.send_keys(self.loc_问卷备注, remark)
        return self

    def click_组件_单选题(self):
        self.mouse_over_click(self.loc_组件_单选题)
        return self

    def click_组件_多选题(self):
        self.mouse_over_click(self.loc_组件_多选题)
        return self

    def click_组件_图片(self):
        self.mouse_over_click(self.loc_组件_图片)
        return self

    def click_组件_单行文本题(self):
        self.mouse_over_click(self.loc_单行文本题)
        return self

    def click_组件_多行文本题(self):
        self.mouse_over_click(self.loc_多行文本题)
        return self

    def click_组件_富文本(self):
        self.mouse_over_click(self.loc_富文本)
        return self

    def click_组件_提交(self):
        self.mouse_over_click(self.loc_提交)
        return self

    def click_组件_图片_Card(self):
        self.mouse_over_click(self.loc_图片_Card)
        return self

    def click_组件_医生_Card(self):
        self.mouse_over_click(self.loc_医生_Card)
        return self

    def send_单选题_标题(self, title):
        self.send_keys(self.loc_单选题_标题, title)
        return self

    def send_单选题_内容1(self, option):
        self.send_keys(self.loc_单选题_内容1, option)
        return self

    def send_单选题_内容2(self, option):
        self.send_keys(self.loc_单选题_内容2, option)
        return self

    def send_单选题_内容3(self, option):
        self.send_keys(self.loc_单选题_内容3, option)
        return self

    def send_多选题_标题(self, title):
        self.send_keys(self.loc_多选题_标题, title)
        return self

    def send_多选题_内容1(self, option):
        self.send_keys(self.loc_多选题_内容1, option)
        return self

    def send_多选题_内容2(self, option):
        self.send_keys(self.loc_多选题_内容2, option)
        return self

    def send_多选题_内容3(self, option):
        self.send_keys(self.loc_多选题_内容3, option)
        return self

    def send_图片上传(self, png):
        self.send_png(self.loc_图片_上传, png)
        return self

    def send_图片_描述(self, describe):
        self.send_keys(self.loc_图片_描述, describe)
        return self

    def send_单行文本题_标题(self, title):
        self.send_keys(self.loc_单行文本题_标题, title)
        return self

    def send_单行文本题_描述(self, describe):
        self.send_keys(self.loc_单行文本题_描述, describe)
        return self

    def send_单行文本题_图片(self, png):
        self.send_png(self.loc_单行文本题_图片, png)
        return self

    def send_单行文本题_提示文字(self, hint):
        self.send_keys(self.loc_单行文本题_提示文字, hint)
        return self

    def send_多行文本题_标题(self, title):
        self.send_keys(self.loc_多行文本题_标题, title)
        return self

    def send_多行文本题_描述(self, describe):
        self.send_keys(self.loc_多行文本题_描述, describe)
        return self

    def send_多行文本题_图片(self, png):
        self.send_keys(self.loc_多行文本题_图片, png)
        return self

    def send_多行文本题_提示文字(self, hint):
        self.send_keys(self.loc_多行文本题_提示文字, hint)
        return self

    def send_富文本内容(self, body):
        self.send_png(self.loc_富文本框内容, body)
        return self

    def switch_富文本框(self):
        self.switch_to_frame(self.loc_富文本_frame)
        return self

    def send_提交_文案(self, content):
        self.send_keys(self.loc_提交_文案, content)
        return self

    def click_提交_是吸底(self):
        self.click_element(self.loc_提交_是吸底)
        return self

    def click_提交_否吸底(self):
        self.click_element(self.loc_提交_否吸底)
        return self

    def send_图片_Card_文案(self, content):
        self.send_keys(self.loc_图片_Card_文案, content)
        return self

    def send_图片_Card_复制内容(self, content):
        self.send_keys(self.loc_图片_Card_复制内容, content)
        return self

    def send_医生_Card_医生姓名(self, name):
        self.send_keys(self.loc_医生_Card_医生姓名, name)
        return self

    def send_医生_Card_职称(self, nickname):
        self.send_keys(self.loc_医生_Card_职称, nickname)
        return self

    def send_医生_Card_医院(self, hospital):
        self.send_keys(self.loc_医生_Card_医院, hospital)
        return self

    def send_医生_Card_擅长(self, major):
        self.send_keys(self.loc_医生_Card_擅长, major)
        return self

    def send_医生_Card_按钮文字(self, button):
        self.send_keys(self.loc_医生_Card_按钮文字, button)
        return self

    def send_医生_Card_头像(self, photo):
        self.send_png(self.loc_医生_Card_头像, photo)
        return self

    def click_医生_Card_头像_裁切确定(self):
        self.click_element(self.loc_医生_Card_头像_裁切确定)
        return self

    def send_医生_Card_按钮点击效果_链接(self):
        self.click_element(self.loc_医生_Card_按钮点击效果_链接)
        return self

    def send_医生_Card_按钮点击效果_弹层提问(self):
        self.click_element(self.loc_医生_Card_按钮点击效果_弹层提问)
        return self

    def send_医生_Card_URL(self, url):
        self.send_keys(self.loc_医生_Card_URL, url)
        return self

    def click_保存(self):
        self.click_element(self.loc_保存)
        return self

    def click_投放(self):
        self.click_element(self.loc_投放)
        return self

    def click_取消(self):
        self.click_element(self.lco_取消)
        return self

    def click_预览(self):
        self.click_element(self.loc_预览)
        return self

    def send_单选题_图片1(self, png):
        self.send_png(self.loc_单选题_图片1, png)
        return self

    def send_单选题_图片2(self, png):
        self.send_png(self.loc_单选题_图片2, png)
        return self

    def send_单选题_图片3(self, png):
        self.send_png(self.loc_单选题_图片3, png)
        return self

    def send_多选题_图片1(self, png):
        self.send_png(self.loc_多选题_图片1, png)
        return self

    def send_多选题_图片2(self, png):
        self.send_png(self.loc_多选题_图片2, png)
        return self

    def send_多选题_图片3(self, png):
        self.send_png(self.loc_多选题_图片3, png)
        return self

    def get_错误提示(self):
        return self.get_element_text(self.loc_错误提示)

    def get_投放成功(self):
        return self.get_element_text(self.loc_投放成功)

    def click_投放确定(self):
        self.click_element(self.lco_确定投放)
        return self
