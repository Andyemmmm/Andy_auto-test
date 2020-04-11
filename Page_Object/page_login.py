from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Login(SeleniumBase):
    '''这是社区B端的登陆页'''
    loc_auth_code = (By.XPATH, '//div[1]/div[2]/div/div[1]/ul/li[1]/span')
    loc_passrd_login = (By.XPATH, '//div[1]/div[2]/div/div[1]/ul/li[2]/span')
    loc_phone = (By.XPATH, '//div[1]/div[2]/div/form[2]/div[1]/div/div/input')
    loc_phone_code = (By.XPATH, '//div[2]/div/form[1]/div[1]/div/div[1]/input')
    loc_send_code = (By.XPATH, '//div[2]/div/form[1]/div[2]/div/span')
    loc_password = (By.XPATH, '//div[1]/div[2]/div/form[2]/div[2]/div/div/input')
    loc_password_code = (By.XPATH, '//div[2]/div/form[1]/div[2]/div/div/input')
    loc_loginSubmit = (By.XPATH, '//div[1]/div[2]/div/button/span')
    loc_msg_error = (By.XPATH, '//div[@class="el-form-item__error"]')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")

    def send_用户名(self, username):
        self.send_keys(self.loc_phone, username)
        return self

    def send_phone_code(self, phone):
        self.send_keys(self.loc_phone_code, phone)
        return self

    def send_密码(self, password):
        self.send_keys(self.loc_password, password)
        return self

    def click_send_code(self):
        self.click_element(self.loc_send_code)
        return self

    def send_code(self, code):
        self.send_keys(self.loc_password_code, code)
        return self

    def click_登录按钮(self):
        self.click_element(self.loc_loginSubmit)
        return self

    def get_登录错误提示(self):
        return self.get_element_text(self.loc_msg_error)

    def get_msg(self):
        return self.get_element_text(self.loc_msg)

    def click_code_login(self):
        self.click_element(self.loc_auth_code)
        return self

    def click_passrd_login(self):
        self.click_element(self.loc_passrd_login)
