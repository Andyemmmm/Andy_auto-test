#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/25 14:04
# @File     : page_home_management.py
# @Software : aiwen_ui


from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase


class Page_Home_management(SeleniumBase):
    '''
    这个是社区模块--首页管理页面
    '''

    loc_banner配置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/ul/li[1]')
    loc_功能推荐位配置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/ul/li[2]')
    loc_健康知识_咨询公告配置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/ul/li[3]')
    loc_医医课堂配置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/ul/li[4]')
    loc_医生推荐配置 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/ul/li[5]')
    loc_热门帖子 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/ul/li[6]')
    loc_热门专题 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/ul/li[7]')
    loc_精选科普 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/ul/li[8]')

    loc_banner1 = (By.XPATH,
                   '//*[@id="app"]/section/section/main/div/div/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/button/span')
    loc_banner2 = (By.XPATH,
                   '//*[@id="app"]/section/section/main/div/div/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[2]/td[6]/div/button/span')
    loc_banner3 = (By.XPATH,
                   '//*[@id="app"]/section/section/main/div/div/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[3]/td[6]/div/button/span')
    loc_banner4 = (By.XPATH,
                   '//*[@id="app"]/section/section/main/div/div/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[4]/td[6]/div/button/span')
    loc_banner5 = (By.XPATH,
                   '//*[@id="app"]/section/section/main/div/div/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[5]/td[6]/div/button/span')
    loc_banner弹窗_展示类型 = (By.XPATH,
                         '//*[@id="app"]/section/section/main/div/div/div/div/div[2]/div[2]/div/div[2]/form/div[2]/div/div/label[1]/span[2]')
    loc_banner弹窗_内容类型 = (By.XPATH,
                         '//*[@id="app"]/section/section/main/div/div/div/div/div[2]/div[2]/div/div[2]/form/div[3]/div/div/div/input')
    loc_banner弹窗_内容类型_选项 = (By.XPATH,
                            '/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
    loc_banner弹窗_内容类型2_选项 = (By.XPATH,
                             '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
    loc_banner弹窗_标题 = (By.XPATH,
                       '//*[@id="app"]/section/section/main/div/div/div/div/div[2]/div[2]/div/div[2]/form/div[4]/div/div/div/input')
    loc_banner弹窗_标题_选项 = (By.XPATH,
                          '/html/body/div[4]/div[1]/div[1]/ul/li/span')
    loc_banner弹窗_标题_选项2 = (By.XPATH,
                           '/html/body/div[5]/div[1]/div[1]/ul/li/span')
    loc_banner弹窗_图片 = (By.XPATH,
                       '//*[@id="app"]/section/section/main/div/div/div/div/div[2]/div[2]/div/div[2]/form/div[5]/div/div/div[1]/input')
    loc_banner弹窗_裁切确定 = (By.CSS_SELECTOR,
                         "body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small > span")
    loc_banner弹窗_确定 = (By.CSS_SELECTOR,
                       '#app > section > section > main > div > div > div > div > div:nth-child(3) > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small > span')

    loc_健康知识 = (By.ID, 'tab-first')
    loc_咨询公告 = (By.ID, 'tab-second')
    loc_编辑1 = (By.XPATH, '//*[@id="pane-first"]/div/div[3]/table/tbody/tr[1]/td[4]/div/button/span')
    loc_咨询公告_编辑1 = (By.XPATH, '//*[@id="pane-second"]/div/div[3]/table/tbody/tr[1]/td[4]/div/button/span')
    loc_编辑2 = (By.XPATH, '//*[@id="pane-first"]/div/div[3]/table/tbody/tr[2]/td[4]/div/button/span')
    loc_咨询公告_编辑2 = (By.XPATH, '//*[@id="pane-second"]/div/div[4]/table/tbody/tr[1]/td[4]/div/button/span')
    loc_标题输入 = (By.XPATH,
                '//*[@id="app"]/section/section/main/div/div/div/div/div[4]/div[2]/div/div[2]/form/div[2]/div/div/div[1]/input')
    loc_标题_选项 = (By.XPATH,
                 '/html/body/div[6]/div[1]/div[1]/ul/li/span')
    loc_标题输入确定 = (By.XPATH,
                  '//*[@id="app"]/section/section/main/div/div/div/div/div[4]/div[2]/div/div[3]/span/button[1]/span')
    loc_标题输入取消 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div[4]/div[2]/div/div[3]/span/button[2]/span')

    loc_医医课堂_编辑1 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[5]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/button/span')
    loc_医医课堂_编辑2 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[5]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[4]/div/button/span')
    loc_医医课堂_编辑3 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[5]/div[1]/div[2]/div[3]/table/tbody/tr[3]/td[4]/div/button/span')
    loc_医医课堂_编辑4 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[5]/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[4]/div/button/span')
    loc_医医课堂_标题输入 = (By.XPATH,
                     '//*[@id="app"]/section/section/main/div/div/div/div/div[5]/div[2]/div/div[2]/form/div[2]/div/div/div/input')
    loc_医医课堂_标题选项 = (By.XPATH,
                     '/html/body/div[8]/div[1]/div[1]/ul/li[1]/span')
    loc_医医课堂_标题确定 = (By.XPATH,
                     '//*[@id="app"]/section/section/main/div/div/div/div/div[5]/div[2]/div/div[3]/span/button[1]/span')

    loc_医生推荐_推荐位1 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div[6]/div/form/div[1]/div/div/div[1]/input')
    loc_医生推荐_推荐位_选项 = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li/span')
    loc_医生推荐_推荐位_选项1 = (By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul/li/span')
    loc_医生推荐_推荐位_选项2 = (By.XPATH, '/html/body/div[9]/div[1]/div[1]/ul/li/span')
    loc_医生推荐_推荐位2 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div[6]/div/form/div[2]/div/div/div/input')

    loc_医生推荐_推荐位3 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div[6]/div/form/div[3]/div/div/div[1]/input')

    loc_医生推荐_确定 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div[6]/div/span/button/span')

    loc_热门帖子_编辑1 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[7]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/button/span')
    loc_热门帖子_标题输入 = (By.XPATH,
                     '//*[@id="app"]/section/section/main/div/div/div/div/div[7]/div[2]/div/div[2]/form/div[2]/div/div/div[1]/input')
    loc_热门帖子_标题_选项 = (By.XPATH,
                      '/html/body/div[8]/div[1]/div[1]/ul/li/span')
    loc_热门帖子_编辑2 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[7]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[5]/div/button/span')
    loc_热门帖子_编辑3 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[7]/div[1]/div[2]/div[3]/table/tbody/tr[3]/td[5]/div/button/span')
    loc_热门帖子_编辑4 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[7]/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[5]/div/button/span')
    loc_热门帖子_编辑5 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[7]/div[1]/div[2]/div[3]/table/tbody/tr[5]/td[5]/div/button/span')
    loc_热门帖子_确定 = (By.XPATH,
                   '//*[@id="app"]/section/section/main/div/div/div/div/div[7]/div[2]/div/div[3]/span/button[1]/span')

    loc_专题配置_编辑1 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[8]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/button/span')
    loc_专题配置_编辑2 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[8]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[4]/div/button/span')
    loc_专题配置_删除1 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[8]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/button[3]/span')
    loc_专题配置_删除2 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[8]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[4]/div/button[3]/span')
    loc_专题配置_标题输入 = (By.XPATH,
                     '//*[@id="app"]/section/section/main/div/div/div/div/div[8]/div[2]/div/div[2]/form/div[2]/div/div/div[1]/input')
    loc_专题配置_标题输入1 = (By.XPATH,
                      '//*[@id="app"]/section/section/main/div/div/div/div/div[8]/div[2]/div/div[2]/form/div[2]/div/div/div/input')
    loc_专题配置_标题选项 = (By.XPATH,
                     '/html/body/div[9]/div[1]/div[1]/ul/li/span')
    loc_专题配置_标题确定 = (By.XPATH,
                     '//*[@id="app"]/section/section/main/div/div/div/div/div[8]/div[2]/div/div[3]/span/button[1]/span')

    loc_精选科普_编辑1 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[9]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/button/span')
    loc_精选科普_编辑2 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[9]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[4]/div/button/span')
    loc_精选科普_编辑3 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[9]/div[1]/div[2]/div[3]/table/tbody/tr[3]/td[4]/div/button/span')
    loc_精选科普_编辑4 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[9]/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[4]/div/button/span')
    loc_精选科普_编辑5 = (By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/div[9]/div[1]/div[2]/div[3]/table/tbody/tr[5]/td[4]/div/button/span')
    loc_精选科普_标题输入 = (By.XPATH,
                     '//*[@id="app"]/section/section/main/div/div/div/div/div[9]/div[2]/div/div[2]/form/div[2]/div/div/div[1]/input')
    loc_精选科普_标题选项 = (By.XPATH,
                     '/html/body/div[11]/div[1]/div[1]/ul/li/span')
    loc_精选科普_标题确定 = (By.XPATH,
                     '//*[@id="app"]/section/section/main/div/div/div/div/div[9]/div[2]/div/div[3]/span/button[1]/span')

    def click_banner_配置(self):
        self.mouse_over_click(self.loc_banner配置)
        return self

    def click_功能推荐位_配置(self):
        self.mouse_over_click(self.loc_功能推荐位配置)
        return self

    def click_健康知识_咨询公告_配置(self):
        self.mouse_over_click(self.loc_健康知识_咨询公告配置)
        return self

    def click_医医课堂_配置(self):
        self.mouse_over_click(self.loc_医医课堂配置)
        return self

    def click_医生推荐配置(self):
        self.mouse_over_click(self.loc_医生推荐配置)
        return self

    def click_热门帖子_配置(self):
        self.mouse_over_click(self.loc_热门帖子)
        return self

    def click_热门专题_配置(self):
        self.mouse_over_click(self.loc_热门专题)
        return self

    def click_精选科普_配置(self):
        self.mouse_over_click(self.loc_精选科普)
        return self

    def click_banner1_编辑(self):
        self.mouse_over_click(self.loc_banner1)
        return self

    def click_banner2_编辑(self):
        self.click_element(self.loc_banner2)
        return self

    def click_banner弹窗_内容类型(self):
        self.mouse_over_click(self.loc_banner弹窗_内容类型)
        return self

    def click_banner弹窗_内容类型_选项(self):
        self.mouse_over_click(self.loc_banner弹窗_内容类型_选项)
        return self

    def click_banner弹窗_内容类型2_选项(self):
        self.mouse_over_click(self.loc_banner弹窗_内容类型2_选项)
        return self

    def send_banner弹窗_标题(self, title):
        self.send_keys(self.loc_banner弹窗_标题, title)
        return self

    def click_banner弹窗_标题(self):
        self.mouse_over_click(self.loc_banner弹窗_标题)
        return self

    def click_banner弹窗_标题_选项(self):
        self.mouse_over_click(self.loc_banner弹窗_标题_选项)
        return self

    def click_banner弹窗_标题_选项2(self):
        self.mouse_over_click(self.loc_banner弹窗_标题_选项2)
        return self

    def send_banner弹窗_图片(self, png):
        self.send_png(self.loc_banner弹窗_图片, png)
        return self

    def click_banner弹窗_裁切确定(self):
        self.click_element(self.loc_banner弹窗_裁切确定)
        return self

    def click_banner弹窗_确定(self):
        self.click_element(self.loc_banner弹窗_确定)
        return self

    def click_健康知识(self):
        self.click_element(self.loc_健康知识)
        return self

    def click_咨询公告(self):
        self.mouse_over_click(self.loc_咨询公告)
        return self

    def click_健康知识_编辑1(self):
        self.click_element(self.loc_编辑1)
        return self

    def click_咨询公告_编辑1(self):
        self.click_element(self.loc_咨询公告_编辑1)
        return self

    def click_健康知识_编辑2(self):
        self.click_element(self.loc_编辑2)
        return self

    def click_咨询公告_编辑2(self):
        self.click_element(self.loc_编辑2)
        return self

    def click_健康咨询_标题输入(self):
        self.click_element(self.loc_标题输入)
        return self

    def send_健康咨询_标题输入(self, title):
        self.send_keys(self.loc_标题输入, title)
        return self

    def click_健康咨询_标题_选项(self):
        self.click_element(self.loc_标题_选项)
        return self

    def click_健康咨询_标题输入确定(self):
        self.click_element(self.loc_标题输入确定)
        return self

    def click_医医课堂_编辑1(self):
        self.click_element(self.loc_医医课堂_编辑1)
        return self

    def send_医医课堂_标题输入(self, classname):
        self.send_keys(self.loc_医医课堂_标题输入, classname)
        return self

    def click_医医课堂_标题输入(self):
        self.click_element(self.loc_医医课堂_标题输入)
        return self

    def click_医医课堂_标题选项(self):
        self.mouse_over_click(self.loc_医医课堂_标题选项)
        return self

    def click_医医课堂_编辑2(self):
        self.click_element(self.loc_医医课堂_编辑2)
        return self

    def click_医医课堂_编辑3(self):
        self.click_element(self.loc_医医课堂_编辑3)
        return self

    def click_医医课堂_编辑4(self):
        self.click_element(self.loc_医医课堂_编辑4)
        return self

    def click_医医课堂_标题确定(self):
        self.click_element(self.loc_医医课堂_标题确定)
        return self

    def scroll_医生推荐_配置(self):
        self.ex_script(self.loc_医生推荐配置)
        return self

    def click_医生推荐_推荐位1(self):
        self.click_element(self.loc_医生推荐_推荐位1)
        return self

    def send_医生推荐_推荐位1(self, name):
        self.send_keys(self.loc_医生推荐_推荐位1, name)
        return self

    def click_医生推荐_推荐位2(self):
        self.click_element(self.loc_医生推荐_推荐位2)
        return self

    def send_医生推荐_推荐位2(self, name):
        self.send_keys(self.loc_医生推荐_推荐位2, name)
        return self

    def click_医生推荐_推荐位3(self):
        self.click_element(self.loc_医生推荐_推荐位3)
        return self

    def send_医生推荐_推荐位3(self, name):
        self.send_keys(self.loc_医生推荐_推荐位3, name)
        return self

    def click_医生推荐_推荐位_选项(self):
        self.mouse_over_click(self.loc_医生推荐_推荐位_选项)
        return self

    def click_医生推荐_推荐位_选项1(self):
        self.mouse_over_click(self.loc_医生推荐_推荐位_选项1)
        return self

    def click_医生推荐_推荐位_选项2(self):
        self.mouse_over_click(self.loc_医生推荐_推荐位_选项2)
        return self

    def click_医生推荐_确定(self):
        self.click_element(self.loc_医生推荐_确定)
        return self

    def click_热门帖子_编辑1(self):
        self.click_element(self.loc_热门帖子_编辑1)
        return self

    def click_热门帖子_编辑2(self):
        self.click_element(self.loc_热门帖子_编辑2)
        return self

    def click_热门帖子_编辑3(self):
        self.click_element(self.loc_热门帖子_编辑3)
        return self

    def click_热门帖子_标题输入(self):
        self.click_element(self.loc_热门帖子_标题输入)
        return self

    def send__热门帖子_标题输入(self, title):
        self.send_keys(self.loc_热门帖子_标题输入, title)
        return self

    def click_热门帖子_标题_选项(self):
        self.click_element(self.loc_热门帖子_标题_选项)
        return self

    def click_热门帖子_确定(self):
        self.click_element(self.loc_热门帖子_确定)
        return self

    def click_专题配置_编辑1(self):
        self.mouse_over_click(self.loc_专题配置_编辑1)
        return self

    def click_专题配置_编辑2(self):
        self.mouse_over_click(self.loc_专题配置_编辑2)
        return self

    def click_专题配置_删除1(self):
        self.mouse_over_click(self.loc_专题配置_删除1)
        return self

    def click_专题配置_删除2(self):
        self.mouse_over_click(self.loc_专题配置_删除2)
        return self

    def click_专题配置_标题输入(self):
        self.click_element(self.loc_专题配置_标题输入)
        return self

    def send__专题配置_标题输入(self, title):
        self.send_keys(self.loc_专题配置_标题输入, title)
        return self

    def click_专题配置_标题选项(self):
        self.mouse_over_click(self.loc_专题配置_标题选项)
        return self

    def click_专题配置_标题确定(self):
        self.click_element(self.loc_专题配置_标题确定)
        return self

    def click_精选科普_编辑1(self):
        self.mouse_over_click(self.loc_精选科普_编辑1)
        return self

    def click_精选科普_编辑2(self):
        self.mouse_over_click(self.loc_精选科普_编辑2)
        return self

    def click_精选科普_编辑3(self):
        self.mouse_over_click(self.loc_精选科普_编辑3)
        return self

    def click_精选科普_标题输入(self):
        self.click_element(self.loc_精选科普_标题输入)
        return self

    def send__精选科普_标题输入(self, title):
        self.send_keys(self.loc_精选科普_标题输入, title)
        return self

    def click_精选科普_标题选项(self):
        self.mouse_over_click(self.loc_精选科普_标题选项)
        return self

    def click_精选科普_标题确定(self):
        self.click_element(self.loc_精选科普_标题确定)
        return self
