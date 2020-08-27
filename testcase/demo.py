#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/7/8 10:10
# @File     : test_login.py
# @Software : Test_dental
import requests
import json
import unittest
# from selenium import webdriver
# from common import loging
# import time
# import ddt
# from common.read_txt import read_txt
# from config.url import appointment
#
# logger = loging.Log(__name__)
# from config.url import url_内测
#
# logger.info('打开浏览器')
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get(appointment)
# time.sleep(5)
# # 点击位置按钮
# # for i in range(9):
# #     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/div/div[1]/div[1]').click()
# #     time.sleep(1)
# #     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[7]/div[2]/div/div[1]/span[1]').click()
# #     time.sleep(1)
# # 点击时间按钮
# for i in range(9):
#     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/div/div[2]/div[1]/b').click()
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[8]/div[1]').click()
#     time.sleep(1)
# # # 点击全部项目
# # for i in range(9):
# #     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/div/div[2]/div[2]/b').click()
# #     time.sleep(1)
# #     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[6]/div[2]/div/div[1]/span[1]').click()
# #     time.sleep(1)
# # # 点击立即预约,并按确定按钮.最后关闭
# # for i in range(9):
# #     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/ul/li[1]/div[2]').click()  # 点击立即预约
# #     time.sleep(1)
# #     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[8]/div[2]/div/div[3]/div').click()  # 点击确定按钮
# #     time.sleep(1)
# #     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[5]/div[2]/div/div[3]/div[2]').click()  # 点击立即预约
# #     time.sleep(2)
# #     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[5]/div[1]').click()  # 点击其它地方关闭弹窗
# #     time.sleep(1)
#
# driver.quit()
data={
    'pageNumber':1,
    'pageSize':20,
    'sid':'5db2550cbfe5230006ec6420',
    'versionNo':430
}
response=requests.get(url='http://appdr.wenwo.com/api/v4/videoLessons/getOnlineClassRoomList',data=data)
print(requests.status_codes)