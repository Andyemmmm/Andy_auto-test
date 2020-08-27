from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Register(SeleniumBase):
    """注册页面"""
    loc_phone = (By.XPATH, '//input[@placeholder="请输入手机号码"]')
    loc_click_code = (By.XPATH, '//span[@class="send-code-btn validCode"]')
    loc_send_code = (By.XPATH, '//input[@placeholder="请输入验证码"]')
    loc_orgName = (By.NAME, "orgName")
    loc_勾选 = (By.XPATH, '//span[@class="el-checkbox__input is-checked"]')
    loc_registsubmit = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/button/span')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def send_phone(self, phone):
        self.send_keys(self.loc_phone, phone)
        return self

    def send_code(self, code):
        self.send_keys(self.loc_send_code, code)
        return self

    def click_code(self):
        self.send_keys(self.loc_click_code)
        return self

    def send_orgName(self, orgName):
        self.send_keys(self.loc_orgName, orgName)
        return self

    def click_勾选(self):
        self.click_element(self.loc_勾选)
        return self

    def click_注册按钮(self):
        self.click_element(self.loc_registsubmit)
        return self

    def get_msg(self):
        return self.get_element_text(self.loc_msg)
