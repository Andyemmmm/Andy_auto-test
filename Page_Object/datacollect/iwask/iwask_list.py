#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/5/15 11:17
# @File     : iwask_list.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.datacollect.iw_data_collect import Iw_data_collect
import time


class Page_Iwask_List(Iw_data_collect):
    """聚合医疗平台医生列表页"""
    url = "https://health.sina.cn/c/iwask/list?"
    loc_顶部搜索框 = (By.XPATH, '//input[@placeholder="搜索疾病、医生、科室"]')
    loc_顶部搜索框按钮 = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[2]/div/i')
    loc_综合排序 = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[3]/div/div/div/div[1]/div[1]/span/div')
    loc_综合排序_综合排序 = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[3]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/span')
    loc_综合排序_价格从低到高 = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/span')
    loc_综合排序_价格从高到低 = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[3]/div/div/div/div[2]/div/div[2]/div[3]/div/span')
    loc_科室 = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[3]/div/div/div/div[1]/div[2]/span/div')
    loc_科室_中医科 = (By.XPATH, '//div[3]/div/div[2]/div/div[1]/a[2]/div[text()="中医学"]')
    loc_科室_中医科_中医科 = (By.XPATH, '//div[@class="van-tree-select__content"]/div[text()="中医科"]')
    loc_城市 = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[3]/div/div/div/div[1]/div[3]/span/div')
    loc_城市_北京 = (By.XPATH, '//div[4]/div/div[2]/div/div[1]/a[2]/div[text()="北京"]')
    loc_城市_北京_北京市 = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[3]/div/div/div/div[4]/div/div[2]/div/div[2]/div[2]')
    loc_更多 = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[3]/div/div/div/div[1]/div[4]/span/div')
    loc_更多_职称_主任医师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[1]/button[text()="主任医师"]')
    loc_更多_职称_副主任医师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[1]/button[text()="副主任医师"]')
    loc_更多_职称_主治医师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[1]/button[text()="主治医师"]')
    loc_更多_职称_医师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[1]/button[text()="医师"]')
    loc_更多_职称_主任药师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[2]/button[text()="主任药师 "]')
    loc_更多_职称_副主任药师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[2]/button[text()="副主任药师"]')
    loc_更多_职称_主管药师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[2]/button[text()="主管药师"]')
    loc_更多_职称_初级药师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[2]/button[text()="初级药师"]')
    loc_更多_职称_执业护师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[3]/button[text()="执业护师"]')
    loc_更多_职称_心理咨询师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[3]/button[text()="心理咨询师"]')
    loc_更多_职称_公共营养师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[3]/button[text()="公共营养师"]')
    loc_更多_职称_健康管理师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[3]/button[text()="健康管理师"]')
    loc_更多_职称_医学检验技师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[3]/button[text()="医学检验技师"]')
    loc_更多_职称_康复治疗技师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[3]/button[text()="康复治疗技师"]')
    loc_更多_职称_药剂师 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[1]/div[3]/button[text()="药剂师"]')
    loc_更多_平台_爱问医生 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[2]/div/button[text()="爱问医生"]')
    loc_更多_平台_丁香医生 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[2]/div/button[text()="丁香医生"]')
    loc_更多_平台_好大夫在线 = (By.XPATH, '//div[5]/div/div[2]/div[1]/div[2]/div/button[text()="好大夫在线"]')
    loc_更多_确定按钮 = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[3]/div/div/div/div[5]/div/div[2]/div[2]/button[2]')
    loc_第一个医生 = (By.XPATH, '//div[@class="doctor_list"]/div[1]/a[1]/div[1]')
    loc_第一个医生图文咨询 = (By.XPATH, '//div[@class="doctor_list"]/div[1]/div')
    loc_share = (By.XPATH, '//*[@id="scroll_div_wrapper"]/div[1]/div[3]/a')
    loc_share_q = (By.XPATH, '//span[text()="确定"]')
