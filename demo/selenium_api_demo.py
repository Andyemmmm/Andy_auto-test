from selenium import webdriver

# 创建浏览器实例
driver = webdriver.Chrome()
# driver_ie = webdriver.Ie()
# driver_firefox = webdriver.Firefox()

# 浏览器类型
driver.name
# 最大化浏览器
driver.maximize_window()
# 最小化浏览器
driver.minimize_window()
# 全屏浏览器
driver.fullscreen_window()
# 设置高度与宽度
driver.set_window_size('768', "1024")
# 定义变量保存网址
url = "https://liushilive.github.io/html_example/index1.html"
# 打开网址
driver.get(url)
# 网页标题
driver.title
# 获取当前网址
driver.current_url
# 获取网页源代码
with open(r"D:\1.html", 'w', encoding="utf-8") as f:
    f.write(driver.page_source)
# 截图
driver.save_screenshot(r"d:\1.png")
# 网页刷新
driver.refresh()
# 后退
driver.back()
# 前进
driver.forward()

# 关闭标签页
driver.close()
# 关闭浏览器
driver.quit()
# driver_ie.quit()
# driver_firefox.quit()

# 定位元素
# 定位单个元素
# id
ele = driver.find_element_by_id("uid")
# name
ele = driver.find_element_by_name("user")
# xpath
ele = driver.find_element_by_xpath('//label[@for="uid"]')
# link text
ele = driver.find_element_by_link_text("返回演示官网")
# partial link text
ele = driver.find_element_by_partial_link_text("演示")
# class name
ele = driver.find_element_by_class_name("A")
# tag name
ele = driver.find_element_by_tag_name("h2")
# css selector
ele = driver.find_element_by_css_selector("#uid")
# 原始形式
from selenium.webdriver.common.by import By

ele = driver.find_element(By.ID, "uid")

# 查找多个元素
eles = driver.find_elements_by_tag_name("h2")
len(eles)

# 元素基本属性
ele = driver.find_element_by_id("click")
# 标签名
ele.tag_name
# 文本值
ele.text
# 属性值
ele.get_attribute("name")
# css 样式属性值
ele.value_of_css_property("height")
# 是否可见
ele.is_displayed()
# 是否可使用
ele.is_enabled()
# 元素大小与位置
ele.size
ele.location
ele.rect
# 可见位置：如果不可见返回 None
print(ele.location_once_scrolled_into_view)
# 点击
ele.click()

# 模拟键盘输入
ele = driver.find_element_by_id("uid")
# 清空
ele.clear()
# 输入内容
ele.send_keys("123456")
# 模拟键盘按键
from selenium.webdriver.common.keys import Keys

# 删除3
ele.send_keys(Keys.LEFT * 3, Keys.BACKSPACE)

# 下拉框
# 模拟人操作
ele = driver.find_element_by_id("s1Id")
ele.click()
ele_option = driver.find_element_by_css_selector('[value="sz"]')
ele_option.click()
ele.click()

# select 对象
from selenium.webdriver.support.select import Select

# 单选
ele = driver.find_element_by_id("s1Id")
# 创建一个下拉框对象
select = Select(ele)
# 判断是否为多选，单选返回 None，多选返回 True
print(select.is_multiple)
# 根据下标选择：0
select.select_by_index(0)
# 根据 value 属性值
select.select_by_value("sh")
# 根据显式文本选择
select.select_by_visible_text("深圳")

# 多选
ele = driver.find_element_by_id("s3Id")
select = Select(ele)
select.is_multiple
select.select_by_index(0)
select.select_by_index(1)
select.select_by_index(2)
select.select_by_index(3)
select.select_by_index(5)
select.select_by_index(6)
# 当前已经选择的项目
select.all_selected_options
for i in select.all_selected_options:
    print(i.text)

# 取消选择
select.deselect_by_index(1)
select.deselect_by_index(3)
select.deselect_by_index(5)
select.deselect_all()

# 警告框
driver.find_element_by_name("b1").click()
# 得到警告框对象
alert = driver.switch_to.alert
# 警告框文本
alert.text
# 点击确定
alert.accept()
# 点击取消
alert.dismiss()

driver.find_element_by_name("b2").click()
alert = driver.switch_to.alert
alert.send_keys("123")
alert.accept()

# 双击元素
ele = driver.find_element_by_xpath("//*[contains(text(), '请双击这里')]")
# 创建行动链对象
ac = webdriver.ActionChains(driver)
# 定义双击元素的行为
ac.double_click(ele)
# 执行行动链
ac.perform()

# 悬浮
ele = driver.find_element_by_link_text("分 类")
webdriver.ActionChains(driver).move_to_element(ele).perform()
ele = driver.find_element_by_link_text("编程语言")
webdriver.ActionChains(driver).move_to_element(ele).perform()

# 验证码
import time

# 查找滑动块
ele1 = driver.find_element_by_class_name("handler_bg")
# 滑动验证区域
ele2 = driver.find_element_by_class_name("drag_text")
# 计算滑动的距离
w = ele2.size.get("width")
# 一次性拖动
# webdriver.ActionChains(driver).drag_and_drop_by_offset(ele1, w, 0).perform()
# 模拟人为拖动
# 在元素上按下左键
webdriver.ActionChains(driver).click_and_hold(ele1).perform()
for i in range(50):
    # 将鼠标从当前位置移动一个偏移量
    webdriver.ActionChains(driver).move_by_offset(w / 50, 0).perform()
    time.sleep(0.1)
# 释放按键
webdriver.ActionChains(driver).release().perform()

# 拖拽元素
ele1 = driver.find_element_by_css_selector('[data-dad-id="1"]')
ele2 = driver.find_element_by_css_selector('[data-dad-id="2"]')
webdriver.ActionChains(driver).drag_and_drop(ele1, ele2).perform()

# 交换位置
for i in range(1, 6):
    ele_6 = driver.find_element_by_css_selector('[data-dad-id="6"]')
    ele = driver.find_element_by_css_selector(f'[data-dad-id="{i}"]')
    webdriver.ActionChains(driver).drag_and_drop(ele, ele_6).perform()
    time.sleep(0.5)

# JS
# 定义js脚本：滚动到顶部
scroll_top_js = "window.scrollTo(0,0);"
# 定义js脚本：滚动到底部
scroll_end_js = "window.scrollTo(0,document.body.scrollHeight);"
# 定义js脚本：滚动到元素
scroll_view_js = "arguments[0].scrollIntoView();"
# 执行js脚本
driver.execute_script(scroll_top_js)
driver.execute_script(scroll_end_js)
ele = driver.find_element_by_name("b2")
driver.execute_script(scroll_view_js, ele)

# js选择下拉框
driver.execute_script(
    """
    $('#s1Id').val('sh');
    $('#s1Id').trigger('change');
    """
)

# Cookies
# 添加
driver.add_cookie({'name': 'foo', 'value': 'bar'})
driver.add_cookie({'name': 'foo1', 'value': '123'})
# 读取
driver.get_cookie("foo")
driver.get_cookies()
# 删除
driver.delete_cookie("foo1")
driver.delete_all_cookies()

# frame
# 找到frame元素
ele_frame = driver.find_element_by_name("frame1")
# 跳转到元素内部
driver.switch_to.frame(ele_frame)
ele = driver.find_element_by_id("sb_form_q")
ele.send_keys("liushilive")
driver.find_element_by_id("sb_form_go").click()
# 跳到父框架
# driver.switch_to.parent_frame()
# 跳到默认框架
driver.switch_to.default_content()

# 标签页
# 当前标签页的句柄
driver.current_window_handle
# 新标签页打开网址
driver.execute_script("window.open('https://www.baidu.com')")
driver.execute_script("window.open('https://www.bing.com')")
driver.execute_script("window.open('https://www.qq.com')")
# 所有标签页的句柄
driver.window_handles

# 通过标题跳转
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "Bing" in driver.title:
        break
# 通过 url 跳转
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "liushi" in driver.current_url:
        break

driver.close()
driver.title

# 等待
# 显式等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver.refresh()
ele = WebDriverWait(driver, 15).until(
    ec.presence_of_element_located((By.ID, "t1"))
)

# 隐式等待：智能等待
driver.implicitly_wait(15)  # s
driver.refresh()
driver.find_element_by_id("t1")


# 获取tr/td表格中的所有内容

def get_dept_list(self):
    row = self.driver.find_elements_by_tag_name('tr')
    list = []
    for i in row:
        j = i.find_elements_by_tag_name('td')
        for item in j:
            text = item.text
            list.append(text)
    # logging.info('返回的列表数据是{0}'.format(list))
    return list


# 练习
"""练习
1、写一个函数 find_number() 返回表格中所有的电话号码（PHONE_NUMBER）
2、写一个函数 select_date(y, m, d) ，接收3个参数（2011,1,2），操作页面上的日期选择器选择为该日期
3、写一个函数 select_date_time(y, m, d, h, mm, s)，接收一个日期参数（2011,1,2,14,50,2），操作页面上的日期时间选择器选择为该日期
"""


def find_number():
    L = []
    xpath = '//*[@id="t4"]//td[4]'
    eles = driver.find_elements_by_xpath(xpath)
    for ele in eles[1:]:
        L.append(ele.text)
    return L


find_number()


def select_date(y, m, d):
    today = driver.find_element_by_class_name("today").text
    yy, mm, dd = today.split("-")
    yy, mm, dd = int(yy), int(mm), int(dd)
    # 年:abs 绝对值
    for i in range(abs(y - yy)):
        if y < yy:
            driver.find_element_by_id("prevYear").click()
        else:
            driver.find_element_by_id("nextYear").click()
    # 月:abs 绝对值
    for i in range(abs(m - mm)):
        if m < mm:
            driver.find_element_by_id("prevMonth").click()
        else:
            driver.find_element_by_id("nextMonth").click()
    # 日
    driver.find_element_by_xpath(f'//span[text()={d} and contains(@class, "currentDate")]').click()


select_date(2050, 12, 31)


def select_date_time(y, m, d, h, mm, s):
    # 点出 日期选择弹框
    ele = driver.find_element_by_css_selector('[placeholder="点我选择日期"]')
    driver.execute_script("arguments[0].click()", ele)
    # 年
    driver.execute_script(
        f"""
        $('#calendarYear').val('{y}');
        $('#calendarYear').trigger('change');
        """
    )
    # 月
    driver.execute_script(
        f"""
        $('#calendarMonth').val('{int(m) - 1}');
        $('#calendarMonth').trigger('change');
        """
    )
    # 时
    driver.execute_script(
        f"""
        $('#calendarHour').val('{int(h):02}');
        $('#calendarHour').trigger('change');
        """
    )
    # 分
    driver.execute_script(
        f"""
        $('#calendarMinute').val('{int(mm):02}');
        $('#calendarMinute').trigger('change');
        """
    )
    # 秒
    driver.execute_script(
        f"""
        $('#calendarSecond').val('{int(s):02}');
        $('#calendarSecond').trigger('change');
        """
    )
    # 日
    ele = driver.find_element_by_xpath(f'//td[text()={d}]')
    driver.execute_script("arguments[0].click()", ele)
    pass


ele = driver.find_element_by_css_selector('[placeholder="点我选择日期"]')
ele.send_keys("2019-03-24 10:34:39")
ele.get_attribute("value")

select_date_time(2011, 1, 2, 14, 50, 2)
select_date_time(1970, 1, 1, 0, 0, 0)
select_date_time(2020, 12, 31, 23, 59, 59)
