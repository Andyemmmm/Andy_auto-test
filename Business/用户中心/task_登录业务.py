from selenium.webdriver.common.by import By

from Business.base_url import url_index
from Page_Object.page_index import Page_Index
from Page_Object.page_login import Page_Login


def lgoin(se, username, password):
    """登录业务流程"""
    se.get(url_index)
    se.click_element((By.LINK_TEXT, "请登录"))
    se.logger.info(f"输入用户名：{username}")
    se.send_keys((By.ID, "username"), username)
    se.send_keys((By.ID, "nloginpwd"), password)
    se.click_element((By.ID, "loginSubmit"))


def login_po(driver, username, password):
    """登录业务流程"""
    Page_Index(driver).click_请登录链接()
    # pl = Page_Login(driver)
    # pl.send_用户名(username)
    # pl.send_密码(password)
    # pl.click_登录按钮()
    Page_Login(driver).send_用户名(username).send_密码(password).click_登录按钮()
