from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Register(SeleniumBase):
    """注册页面"""
    loc_username = (By.ID, "username")
    loc_password = (By.ID, "pwd")
    loc_confirm_password = (By.ID, "pwdRepeat")
    loc_mobile_phone = (By.ID, "mobile_phone")
    loc_registsubmit = (By.ID, "registsubmit")

    def send_用户名(self, username):
        self.send_keys(self.loc_username, username)

    def send_密码(self, password):
        self.send_keys(self.loc_password, password)

    def send_确认密码(self, pwdRepeat):
        self.send_keys(self.loc_confirm_password, pwdRepeat)

    def send_手机号码(self, mobile_phone):
        self.send_keys(self.loc_mobile_phone, mobile_phone)

    def click_注册按钮(self):
        self.click_element(self.loc_registsubmit)
