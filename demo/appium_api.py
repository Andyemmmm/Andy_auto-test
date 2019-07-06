from appium import webdriver

# 所需能力
# http://appium.io/docs/en/writing-running-appium/caps/
# http://appium.io/docs/en/writing-running-appium/other/reset-strategies/index.html
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "",
    "deviceName": "android",
    "newCommandTimeout": 60000,
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "appPackage": "io.github.liushilive.at",
    "appActivity": ".MainActivity"
    # "app": "at.apk",
    # "app": "https://github.com/liushilive/liushilive.github.io/releases/download/v2.0/app-v2.0.apk"
}
# appium 服务器地址
# command_executor = "http://127.0.0.1:4723/wd/hub"
command_executor = "http://192.168.2.254:4723/wd/hub"
driver = webdriver.Remote(
    command_executor=command_executor,
    desired_capabilities=desired_capabilities
)

# 是否已经安装app
driver.is_app_installed("io.github.liushilive.at")
# 卸载app
driver.remove_app("io.github.liushilive.at")
# 安装app
driver.install_app("https://github.com/liushilive/liushilive.github.io/releases/download/v2.0/app-v2.0.apk")
# 启动app
driver.start_activity("io.github.liushilive.at", ".MainActivity")

# 查找元素
# resource-id
driver.find_element_by_id("type_text_button")
# content-desc
driver.find_element_by_accessibility_id("文本类型")
# xpath
driver.find_element_by_xpath("//*[@text='文本类型']")
# class
driver.find_element_by_class_name("android.widget.Button")

# 文本类型
ele = driver.find_element_by_id("type_text_button")
# 文本值
ele.text
# 元素的大小
ele.size
# 当前位置
ele.location
# 点击元素
ele.click()
# 输入内容
ele = driver.find_element_by_id("name_edittext")
ele.send_keys("刘士")
ele.text
# 清空
ele.clear()
# 点击 Next
ele = driver.find_element_by_id("next_button")
ele.click()
driver.find_element_by_id("error_text").text
# 后退
driver.find_element_by_accessibility_id("后退").click()

# 下拉菜单
driver.find_element_by_accessibility_id("下拉菜单").click()
# 点出下拉框
driver.find_element_by_id("text1").click()
# 选择中国
driver.find_element_by_xpath("//*[@text='中国']").click()
# 后退
# https://blog.csdn.net/xl_tang/article/details/8720953
driver.keyevent(4)

# 书籍列表
driver.find_element_by_accessibility_id("书籍列表").click()

eles = driver.find_elements_by_id("book_title")
for ele in eles:
    print("书名：", ele.text)

ele = driver.find_element_by_xpath("//*[contains(@text, 'with Rails 4')]")

# 滚动查找单个元素
ele = driver.find_element_by_android_uiautomator(
    'new UiScrollable(new UiSelector().scrollable(true))'
    '.scrollIntoView(new UiSelector().textContains("with Rails 4"))'
)
ele.text
driver.keyevent(4)

# 对话框
driver.find_element_by_accessibility_id("对话框").click()
driver.find_element_by_id("confirm_dialog_button").click()
driver.find_element_by_id("button1").click()
driver.keyevent(4)

# 底层的手势
"""
press       短按
release     释放
moveTo      移动
tap         点击
longPress   长按
cancel      取消
perform     执行
"""

from appium.webdriver.common.touch_action import TouchAction

# 画布
driver.find_element_by_accessibility_id("画布").click()

ele = driver.find_element_by_id("finger_view")
x = ele.rect.get("x") + 100
y = ele.rect.get("y") + 100
w = ele.rect.get("width") - 200
h = ele.rect.get("height") - 200

# 画五角星：计算坐标点
x1, y1 = x, y + h / 3
x2, y2 = x + w, y + h / 3
x3, y3 = x + w / 4, y + h
x4, y4 = x + w / 2, y
x5, y5 = x + w * 3 / 4, y + h

TouchAction(driver).press(x=x1, y=y1).wait(1000) \
    .move_to(x=x2, y=y2).wait(1000) \
    .move_to(x=x3, y=y3).wait(1000) \
    .move_to(x=x4, y=y4).wait(1000) \
    .move_to(x=x5, y=y5).wait(1000) \
    .move_to(x=x1, y=y1).wait(1000) \
    .release().perform()

# 多点触摸
from appium.webdriver.common.multi_action import MultiAction

x1 = x + 100
y1 = y + 100
x2 = x + 300
y2 = y + 200
ac0 = TouchAction(driver).press(x=x1, y=y1).wait(10)
ac1 = TouchAction(driver).press(x=x2, y=y2).wait(10)
for i in range(5):
    x1 += 50
    ac0.move_to(x=x1, y=y1).wait(10)
    y1 += 50
    ac0.move_to(x=x1, y=y1).wait(10)
    x2 += 50
    ac1.move_to(x=x2, y=y2).wait(10)
    y2 += 50
    ac1.move_to(x=x2, y=y2).wait(10)
ac0.wait(1000).release()
ac1.wait(500).release()

m = MultiAction(driver)
m.add(ac0, ac1)
m.perform()

driver.keyevent(4)

# 长按
ele = driver.find_element_by_accessibility_id("长按")
TouchAction(driver).long_press(ele).release().perform()
driver.find_element_by_id("button1").click()

# 滑动
driver.find_element_by_accessibility_id("滑动").click()

ele = driver.find_element_by_id("seekBar1")
w = ele.rect.get("width")
h = ele.rect.get("height")
# 右移
x = ele.rect.get("x") + w * 0.05
# 按压点在中间
y = ele.rect.get("y") + h / 2
# 宽度刨除左右空白区域
w = w - w * 0.1

TouchAction(driver).press(x=x, y=y).wait(1000) \
    .move_to(x=x + w * 0.2, y=y).wait(1000) \
    .move_to(x=x + w * 0.3, y=y).wait(1000) \
    .move_to(x=x + w * 0.8, y=y).wait(1000) \
    .release().perform()

ele = driver.find_element_by_id("seekBar2")
w = ele.rect.get("width")
h = ele.rect.get("height")
# 右移
x = ele.rect.get("x") + w * 0.05
# 按压点在中间
y = ele.rect.get("y") + h / 2
# 宽度刨除左右空白区域
w = w - w * 0.1

TouchAction(driver).press(x=x, y=y).wait(1000) \
    .move_to(x=x + w * 0.2, y=y).wait(1000) \
    .move_to(x=x + w * 0.35, y=y).wait(1000) \
    .move_to(x=x + w * 0.89, y=y).wait(1000) \
    .release().perform()

driver.keyevent(4)

# WebView
# 需要对应设备的Chrome驱动，放入
# C:\Users\Administrator\AppData\Local\Programs\Appium\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win
ele = driver.find_element_by_accessibility_id("打开导航抽屉")
ele.click()
driver.find_element_by_xpath("//*[@text='WebView']").click()
# 当前上下文
driver.context
driver.contexts
# 进入webview
driver.switch_to.context('WEBVIEW_io.github.liushilive.at')

driver.find_element_by_id("欢迎来到我的个人页面").text
driver.find_element_by_link_text("常用软件下载").click()
# 跳回原始应用
driver.switch_to.context(None)

# 上传文件
import base64

with open("demo/avd.PNG", "rb") as f:
    data = base64.b16encode(f.read())
    driver.push_file(
        "/storage/emulated/0/DCIM/Camera/tmp.png",
        str(data, "utf-8")
    )

# 下载
data = driver.pull_file("/storage/emulated/0/DCIM/Camera/tmp.png")

with open(r"D:\1.png", "wb") as f:
    f.write(base64.b16decode(data))

# 关闭app
driver.close_app()
# 断开appium服务
driver.quit()
