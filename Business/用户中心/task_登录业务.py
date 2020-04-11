from selenium.webdriver.common.by import By
from Common.tools.rw_ini import read_config
import time

from Business.base_url import url_index, url_login

from Page_Object.page_index import Page_Index
from Page_Object.page_login import Page_Login


def lgoin(se, username, password):
    """登录业务流程"""
    se.get(url_login)
    se.logger.info(f"输入手机号码：{username}")
    se.send_keys((By.XPATH, '//*[@id="pane-login"]/form/div[1]/div/div/input'), username)
    se.logger.info(f"输入密码：{password}")
    se.send_keys((By.XPATH, '//*[@id="pane-login"]/form/div[2]/div/div/input'), password)
    se.click_element((By.XPATH, '//*[@id="pane-login"]/form/div[4]/div/button'))


def login_po(driver, username, password):
    """登录业务流程"""
    driver.get(url_login)
    Page_Index(driver).click_登陆()
    Page_Login(driver).click_passrd_login()
    time.sleep(1)
    Page_Login(driver).send_用户名(username).send_密码(password).click_登录按钮()


