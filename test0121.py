# coding:utf8

from selenium import webdriver

import time
dr=webdriver.Chrome()
url="http://www.baidu.com"
dr.get(url)
name=["天行九歌","韩非","张良"]
l=len(name)
for i in range(0,l):
    dr.find_element_by_id("kw").send_keys(name[i])
    dr.find_element_by_id("su").click()
    dr.find_element_by_id("kw").clear()
dr.get("http://www.taobao.com")
dr.quit()