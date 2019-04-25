from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Login(SeleniumBase):
    loc_username = (By.ID, "username")
    loc_password = (By.ID, "nloginpwd")
    loc_loginSubmit = (By.ID, "loginSubmit")
    loc_msg_error = (By.CLASS_NAME, "msg-error")

    def send_用户名(self, username):
        self.send_keys(self.loc_username, username)
        return self

    def send_密码(self, password):
        self.send_keys(self.loc_password, password)
        return self

    def click_登录按钮(self):
        self.click_element(self.loc_loginSubmit)
        return self

    def get_登录错误提示(self):
        return self.get_element_text(self.loc_msg_error)
