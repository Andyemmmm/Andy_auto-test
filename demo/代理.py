from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://192.168.64.1:10800')

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub",
    options=options
)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()
