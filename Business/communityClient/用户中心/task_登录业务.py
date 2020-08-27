from selenium.webdriver.common.by import By
from Common.tools.rw_ini import read_config
import time
from Common.tools.do_redis import do_redis
from Business.base_url import url_index, url_login
from Page_Object.community.page_bseting import Page_Bseting
from Page_Object.community.page_communityList import Page_CommunityList
from Page_Object.community.page_index import Page_Index
from Page_Object.community.page_login import Page_Login


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
    driver.get(url_index)
    Page_Index(driver).click_登陆()
    Page_Login(driver).click_passrd_login()
    time.sleep(1)
    Page_Login(driver).send_用户名(username).send_密码(password).click_check().click_登录按钮()


def experience_community(driver, name, phone, company=None):
    """申请体验社区"""
    driver.get(url_index)
    Page_Index(driver).click_登陆()
    Page_Login(driver).click_experience().send_name(name).send_phone_ex(phone).send_company(company).click_submit()


def login_code(driver):
    '''验证码登录业务流程'''
    rc = read_config("Config/env.ini")
    username = rc.get("account", "username")
    driver.get(url_index)
    Page_Index(driver).click_登陆()
    Page_Login(driver).click_code_login()
    time.sleep(1)
    Page_Login(driver).send_phone_code(username).click_send_code()
    time.sleep(5)
    code = do_redis(username)
    Page_Login(driver).send_code(code).click_登录按钮()


def loginout(driver):
    '''退出登录业务流程'''
    Page_Bseting(driver).mouse_over_用户信息()
    time.sleep(0.5)
    Page_Bseting(driver).mouse_click_退出登录()
    time.sleep(1)
    Page_CommunityList(driver).click_退出登录确定()


def start_test(driver, ini=None, skt=None):
    '''
    测试用例执行前登录获取账号密码,是否进入社区，获取社区ID的方法
    :param driver: 浏览器
    :param ini: 是否进入社区的参数
    :param skt: 获取配置文件中的ID还是给定的社区ID
    :return:
    '''
    rc = read_config("Config/env.ini")
    local_user = rc.getboolean("local_user", "user")
    username = rc.get("account", "username")
    password = rc.get("account", "password")
    community = rc.get("community", "communityID")
    du_name = rc.get("default", "username")
    du_pwd = rc.get("default", "password")
    if local_user:
        login_po(driver, username, password)
    else:
        login_po(driver, du_name, du_pwd)
    if ini:
        if skt:
            Page_CommunityList(driver).mouse_click_社区(skt)
        else:
            Page_CommunityList(driver).mouse_click_社区(community)
    else:
        pass
