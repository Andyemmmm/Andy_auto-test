import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Common.selenium_library import SeleniumBase


class Page_CommunityList(SeleniumBase):
    '''这是社区B端社区列表页面'''
    loc_用户昵称 = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]/span')
    loc_退出登录确定 = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')
    loc_新建社区 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/button/span')
    loc_全部 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/ul/li[1]')
    loc_医院 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/ul/li[2]')
    loc_医生团队 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/ul/li[4]')
    loc_集团机构 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/ul/li[3]')
    loc_项目型 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/ul/li[5]')
    loc_第一个社区 = (By.XPATH, '//ul[@class="clearfix com-list"]/li[1]')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def get_msg(self):
        return self.get_element_text(self.loc_msg)

    def get_获取用户昵称(self):
        return self.get_element_text(self.loc_用户昵称)

    def click_退出登录确定(self):
        self.click_element(self.loc_退出登录确定)
        return self

    def click_新建社区(self):
        self.logger.info("点击新建社区")
        self.click_element(self.loc_新建社区)

    def click_全部(self):
        self.click_element(self.loc_全部)
        return self

    def click_医院(self):
        self.click_element(self.loc_医院)
        return self

    def click_集团机构(self):
        self.click_element(self.loc_集团机构)
        return self

    def click_项目型(self):
        self.click_element(self.loc_项目型)
        return self

    def click_第一个社区(self):
        self.mouse_over_click(self.loc_第一个社区)
        return self

    def mouse_click_社区(self, communityID):
        element = self.driver.find_element_by_xpath(f"//li[@data-id='{communityID}']")
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def scroll_view(self):
        pass
