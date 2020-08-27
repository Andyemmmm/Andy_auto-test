from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Login(SeleniumBase):
    '''这是社区B端的登陆页----------2020--05--20维护'''
    loc_auth_code = (By.XPATH, '//div[1]/div[1]/div[1]/ul/li[1]/span')
    loc_passrd_login = (By.XPATH, '//div[1]/div[1]/div[1]/ul/li[2]/span')
    loc_phone = (By.XPATH, '//div[1]/div[1]/div[2]/form[2]/div[1]/div/div/input')
    loc_phone_code = (By.XPATH, '//div[1]/div[1]/div[2]/form[1]/div[1]/div/div/input')
    loc_send_code = (By.XPATH, '//div[1]/div[1]/div[2]/form[1]/div[2]/div/span')
    loc_password = (By.XPATH, '//div[1]/div[1]/div[2]/form[2]/div[2]/div/div/input')
    loc_password_code = (By.XPATH, '//div[1]/div[1]/div[2]/form[1]/div[2]/div/div/input')
    loc_loginSubmit = (By.XPATH, '//div/div[1]/div[1]/div[2]/button/span')
    loc_msg_error = (By.XPATH, '//div[@class="el-form-item__error"]')
    loc_msg = (By.XPATH, "//p[@class='el-message__content']")
    loc_check = (By.XPATH, '//div[1]/div[2]/div[2]/label/span[1]/span')

    loc_experience = (By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div[2]/div/span')
    loc_name = (By.XPATH, '//div[2]/div/div[2]/form/div[1]/div/div/input')
    loc_ex_phone = (By.XPATH, '//div[2]/div/div[2]/form/div[2]/div/div/input')
    loc_company = (By.XPATH, '//div[2]/div/div[2]/form/div[3]/div/div/input')
    loc_submit = (By.XPATH, '//div[2]/div/div[2]/form/div[4]/div/button/span')

    loc_scan = (By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div[2]/span/div/span')

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
        return self

    def click_check(self):
        self.click_element(self.loc_check)
        return self

    def click_experience(self):
        self.click_element(self.loc_experience)
        return self

    def send_name(self, name):
        self.send_keys(self.loc_name, name)
        return self

    def send_phone_ex(self, name):
        self.send_keys(self.loc_ex_phone, name)
        return self

    def send_company(self, company=None):
        self.send_keys(self.loc_company, company)
        return self

    def click_submit(self):
        self.click_element(self.loc_submit)
        return self

    def mouse_scan(self):
        self.mouse_over(self.loc_scan)
        return self
