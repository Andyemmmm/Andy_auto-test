from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Home(SeleniumBase):
    '''这个是社区内部首页'''
    loc_账号角色 = (By.XPATH, '//*[@id="app"]/section/section/header/div/div/div/div[1]/div[2]/p[2]/span[2]')
    loc_社区名 = (By.XPATH, '//*[@id="app"]/section/section/header/div/div/div/div[1]/div[2]/p[1]')
    loc_首页 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[1]/li/span')
    loc_社区 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[2]/li/span')
    loc_医生 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[3]/li/span')
    loc_用户 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[4]/li/span')
    loc_财务 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[5]/li/span')
    loc_应用 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[6]/li/span')
    loc_设置 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[7]/li/span')
    loc_立即上线 = (By.XPATH, '//span[@class="alert-btn" and text()="立即上线"]')
    loc_立即上线_确定 = (By.XPATH, "//div[@class='el-dialog']//span[text()='确 定']")
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def click_首页(self):
        self.click_element(self.loc_首页)

    def click_社区(self):
        self.click_element(self.loc_社区)

    def click_医生(self):
        self.click_element(self.loc_医生)

    def click_用户(self):
        self.click_element(self.loc_用户)

    def click_财务(self):
        self.click_element(self.loc_财务)

    def click_应用(self):
        self.click_element(self.loc_应用)

    def click_设置(self):
        self.click_element(self.loc_设置)

    def get_获取社区名(self):
        return self.get_element_text(self.loc_社区名)

    def get_获取账号角色(self):
        return self.get_element_text(self.loc_账号角色)

    def click_online(self):
        self.click_element(self.loc_立即上线)
        return self

    def click_online_confirm(self):
        self.click_element(self.loc_立即上线_确定)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)
