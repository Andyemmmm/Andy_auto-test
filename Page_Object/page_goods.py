from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Page_Good(SeleniumBase):
    loc_加入购物车 = (By.CLASS_NAME, "btn-append")
    loc_提示 = (By.CSS_SELECTOR, ".center_pop_p .ts")
    loc_提示数量 = (By.CSS_SELECTOR, ".desc strong")
    loc_价格 = (By.ID, "ECS_SHOPPRICE")
    loc_提示价格 = (By.CLASS_NAME, "saleP")

    def click_加入购物车(self):
        self.click_element(self.loc_加入购物车)

    def get_加入购物车提示(self):
        return self.get_element_text(self.loc_提示)

    def get_加入购物车提示数量(self):
        return self.get_element_text(self.loc_提示数量).strip("(").strip(")")

    def get_价格(self):
        return self.get_element_text(self.loc_价格)[1:]

    def get_提示价格(self):
        return self.get_element_text(self.loc_提示价格)
