from Business.base_url import url_index
from Common.tools.do_redis import do_redis
from Common.tools.rw_ini import read_config
from Page_Object.page_register import Page_Register
from Page_Object.community.page_index import Page_Index
import time


def register(driver):
    """注册业务"""
    rc = read_config("Config/env.ini")
    phone = rc.get("register", "phone")
    orgName = rc.get("register", "orgName")
    driver.get(url_index)
    Page_Index(driver).click_加入我们()
    Page_Register(driver).send_phone(phone).click_code()
    time.sleep(5)
    code = do_redis(phone)
    Page_Register(driver).send_code(code).send_orgName(orgName).click_勾选().click_注册按钮()
