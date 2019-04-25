from Page_Object.page_register import Page_Register


def register(driver, username, password, pwdRepeat, mobile_phone):
    """注册业务"""
    rp = Page_Register(driver)
    rp.send_用户名(username)
    rp.send_密码(password)
    rp.send_确认密码(pwdRepeat)
    rp.send_手机号码(mobile_phone)
    rp.click_注册按钮()
