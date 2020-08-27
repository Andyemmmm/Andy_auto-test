from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Doctor_Invite(SeleniumBase):
    '''这个是社区--医生模块--邀请医生页面'''
    loc_输入邀请医生名称 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div/div/div[2]/div/div[1]/span/span[1]/div/input')
    loc_输入邀请医生手机号 = (
        By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div/div/div[2]/div/div[1]/span/span[2]/div/input')
    loc_添加 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div/div/div[2]/div/div[1]/span/button')
    loc_确认 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/button[1]')
    loc_取消 = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/button[2]')

    # loc_用户 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[4]/li/span')
    # loc_财务 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[5]/li/span')
    # loc_应用 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[6]/li/span')
    # loc_设置 = (By.XPATH, '//*[@id="app"]/section/aside/div/ul/div[7]/li/span')

    def click_添加(self):
        self.click_element(self.loc_添加)
        return self

    def click_确认(self):
        self.click_element(self.loc_确认)
        return self

    def click_取消(self):
        self.click_element(self.loc_取消)
        return self

    def send_输入邀请医生名称(self, name):
        self.send_keys(self.loc_输入邀请医生名称, name)
        return self

    def send_输入邀请医生手机号(self, phone):
        self.send_keys(self.loc_输入邀请医生手机号, phone)
        return self
