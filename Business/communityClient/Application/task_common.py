#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/1/4 14:48
# @File     : task_common.py
# @Software : aiwen_ui

from Page_Object.community.Community_work.community.page_community_management import Page_Community_management
from Business.base_url import C_client, business_url
from Page_Object.community.Community_work.home_page.page_home import Page_Home
import time


def switch_H5(driver, se):
    '''跳转到  H5  页面'''
    Page_Home(driver).click_社区()
    communityID = Page_Community_management(driver).get_社区ID()
    se.get(f'{C_client}{communityID}')
    se.switch_to_window_url(communityID)


def switch_webpage(se):
    '''跳转到新的网址---商业'''
    se.get(business_url)
    se.driver.find_element_by_id('loginName').send_keys('super')
    se.driver.find_element_by_id('password').send_keys('123456')
    se.driver.find_element_by_xpath('//*[@id="ajaxFrm"]/div/a').click()
    se.driver.switch_to.frame('topFrame')
    se.driver.find_element_by_xpath('/html/body/div/ul/li[2]/a').click()
    se.driver.switch_to.frame('leftFrame')
    se.driver.find_element_by_xpath('//*[@id="a28"]/dd[3]/a').click()
    se.driver.switch_to.default_content()
    se.driver.switch_to.frame('main')
    se.driver.find_element_by_xpath(
        '//*[@id="tab"]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/input').click()
    se.driver.find_element_by_xpath('//*[@id="tool"]/div[1]/div/a[1]').click()
    se.driver.find_element_by_xpath('//*[@id="tab"]/div[3]/div/div[4]/input[1]').click()
    text = se.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]').text
    return text


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

        ele = self.driver.find_element_by_xpath(
            f"//div[@class='datetimepicker-hours']//span[text()='{H}']").is_enabled()
        if ele is False:
            self.click_element(self.loc_当前时间)
        else:
            self.driver.find_element_by_xpath(f"//div[@class='datetimepicker-hours']//span[text()='{H}']").click()
        time.sleep(0.5)

        try:
            ele = self.driver.find_element_by_xpath(
                f"//div[@class='datetimepicker-minutes']//span[text()='{M}']").is_enabled()
            if ele is False:
                self.click_element(self.lco_当前分钟)
            else:
                self.driver.find_element_by_xpath(
                    f"//div[@class='datetimepicker-minutes']//span[text()='{M}']").click()
        except:
            self.click_element(self.lco_当前分钟)
        time.sleep(1)

    else:
        self.driver.find_element_by_xpath("//td[contains(@class,'day today')]/following-sibling::td[1]").click()
        time.sleep(0.5)

        ele = self.driver.find_element_by_xpath(
            f"//div[@class='datetimepicker-hours']//span[text()='{H}']").is_enabled()
        if ele is False:
            self.click_element(self.loc_当前时间)
        else:
            self.driver.find_element_by_xpath(f"//div[@class='datetimepicker-hours']//span[text()='{H}']").click()
        time.sleep(0.5)

        try:
            ele = self.driver.find_element_by_xpath(
                f"//div[@class='datetimepicker-minutes']//span[text()='{M}']").is_enabled()
            if ele is False:
                self.click_element(self.lco_当前分钟)
            else:
                self.driver.find_element_by_xpath(
                    f"//div[@class='datetimepicker-minutes']//span[text()='{M}']").click()
        except:
            self.click_element(self.lco_当前分钟)

    return self


def get_online_msg(driver):
    '''获取社区上线的信息'''
    Page_Home(driver).click_社区()
    text = Page_Community_management(driver).get_社区上线信息()
    return text
