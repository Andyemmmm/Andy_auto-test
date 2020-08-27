#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/5/15 11:17
# @File     : iwask_home.py
# @Software : aiwen_ui

from selenium.webdriver.common.by import By
from Common.datacollect.iw_data_collect import Iw_data_collect
import time


class Page_Iwask_Home(Iw_data_collect):
    """聚合医疗平台首页"""
    url = "https://health.sina.cn/c/iwask?"
    loc_顶部搜索框 = (By.XPATH, '//input[@placeholder="搜索疾病、医生、科室"]')
    loc_顶部搜索框按钮 = (By.XPATH, '//*[@id="__layout"]/div/section/div[2]/div/i')
    loc_热门科室全部 = (By.XPATH, '//*[@id="__layout"]/div/section/div[3]/a')
    lco_热门科室_儿科 = (By.XPATH, '//*[@id="__layout"]/div/section/div[4]/ul/li[1]/a/p')
    loc_热门科室_妇产科 = (By.XPATH, '//*[@id="__layout"]/div/section/div[4]/ul/li[2]/a/p')
    loc_热门科室_皮肤科 = (By.XPATH, '//*[@id="__layout"]/div/section/div[4]/ul/li[3]/a/p')
    loc_热门科室_消化内科 = (By.XPATH, '//*[@id="__layout"]/div/section/div[4]/ul/li[4]/a/p')
    loc_热门科室_口腔科 = (By.XPATH, '//*[@id="__layout"]/div/section/div[4]/ul/li[5]/a/p')
    loc_热门科室_泌尿外科 = (By.XPATH, '//*[@id="__layout"]/div/section/div[4]/ul/li[6]/a/p')
    loc_热门科室_骨科 = (By.XPATH, '//*[@id="__layout"]/div/section/div[4]/ul/li[7]/a/p')
    loc_热门科室_耳鼻咽喉科 = (By.XPATH, '//*[@id="__layout"]/div/section/div[4]/ul/li[8]/a/p')
    loc_banner = (By.XPATH, '//*[@id="__layout"]/div/section/div[5]/div/div[1]/div[1]/a')
    loc_医生推荐全部 = (By.XPATH, '//*[@id="__layout"]/div/section/div[6]/a')
    loc_第一个医生卡片 = (By.XPATH, '//*[@id="__layout"]/div/section/div[7]/div/div[1]/div[1]/div/a[1]/div')
    loc_第一个医生图文咨询按钮 = (By.XPATH, '//*[@id="__layout"]/div/section/div[7]/div/div[1]/div[1]/div/a[2]')
    loc_栏目一 = (By.XPATH, '//*[@id="__layout"]/div/section/div[8]/div[1]/a')
    loc_栏目二 = (By.XPATH, '//*[@id="__layout"]/div/section/div[8]/div[2]/a')
    loc_栏目三 = (By.XPATH, '//*[@id="__layout"]/div/section/div[8]/div[3]/a')
    loc_文章一 = (By.XPATH, '//*[@id="__layout"]/div/section/div[9]/div/a[1]/div[1]')
    loc_文章二 = (By.XPATH, '//*[@id="__layout"]/div/section/div[9]/div/a[2]/div[1]')
    loc_文章三 = (By.XPATH, '//*[@id="__layout"]/div/section/div[9]/div/a[3]/div[1]')
    loc_文章四 = (By.XPATH, '//*[@id="__layout"]/div/section/div[9]/div/a[4]/div[1]')
    loc_文章五 = (By.XPATH, '//*[@id="__layout"]/div/section/div[9]/div/a[5]/div[1]')
    loc_文章六 = (By.XPATH, '//*[@id="__layout"]/div/section/div[9]/div/a[6]/div[1]')
    loc_share = (By.XPATH, '//*[@id="__layout"]/div/section/div[1]/div[3]/a')
    loc_share_q = (By.XPATH, '//*[@id="__layout"]/div/section/div[11]/div[2]/div[1]/span[3]')
