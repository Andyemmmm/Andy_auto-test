from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub",
    options=options
)

driver.get("https://www.baidu.com")
print(driver.title)
driver.quit()
