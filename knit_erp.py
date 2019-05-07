# coding:utf8
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

z=webdriver.Chrome()
url=("https://k.szhibu.com")
z.get(url)
z.maximize_window()
time.sleep(2)
# z.find_element_by_id("kw").send_keys("天行九歌")
# z.find_element_by_xpath("*[@id='__layout']/div/div/section/div[3]/form/div[1]/div/div[1]/input").click()
z.find_element_by_xpath(".//*[@id='__layout']/div/div/section/div[3]/form/div[1]/div/div/input").send_keys("sha")
z.find_element_by_xpath(".//*[@id='__layout']/div/div/section/div[3]/form/div[2]/div/div/input").send_keys("123456")
z.find_element_by_xpath(".//*[@id='__layout']/div/div/section/div[3]/button").click()
time.sleep(2)
#点击导航生产模块
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[1]/div/ul[1]/li[2]/a/span").click()
#点击订单管理
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[1]/div/ul[2]/ul/li[1]/a").click()
time.sleep(1)
#搜索
# z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[1]/div[1]/div[2]/table/thead/tr[1]/th[1]/div/div/div[2]/input").send_keys("PDHK181217001-3")
# z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[1]/div[1]/div[2]/table/thead/tr[1]/th[1]/div/div/div[3]").click()
#新建订单
# z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[1]/div/button[8]/span").click()
z.find_element_by_xpath("//*[@id=__layout']/section/section/div[2]/section/div[1]/div/button[1]/span").click()
# time.sleep(1)
z.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[6]").click()     #选择客户
time.sleep(1)
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[2]/div[1]/input").send_keys("10010")
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("100")
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[2]/div[3]/div/div/div[1]/span/span/i").click()
time.sleep(1)
z.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[6]").click()
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[3]/div[1]/div[1]/div/div[1]/span/span/i").click()
time.sleep(1)
z.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[5]").click()
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[3]/div[1]/div[2]/div/div/span/span/i").click()
time.sleep(1)
z.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[7]/span").click()
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/div/div[1]/span/span/i").click()
time.sleep(1)
z.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[4]").click()
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div/div[1]/span/span/i").click()
time.sleep(1)
z.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[6]").click()
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[3]/div[3]/input").send_keys("莎莎")
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[4]/div[1]/select").click()
time.sleep(1)
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[4]/div[1]/select/option[4]").click()
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
time.sleep(1)
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[4]/div/div[2]/div[1]/div[2]/span[10]").click()
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[4]/div/div[2]/div[2]/button[2]").click()

time.sleep(1)
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[5]/div[2]/input").send_keys("10")
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[5]/div[3]/input").send_keys("18888")
#选择时间组件
# z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[5]/div[1]/div/div/input").click()
# time.sleep(2)
# z.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[5]/div/span").click()
#选择上机工艺
# z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[6]/input").click()
# time.sleep(1)
# z.find_element_by_xpath("//*[@id='tab-1']").click()
# z.find_element_by_xpath("//*[@id='pane-1']/ul/li[2]/div[1]/input").click()
# z.find_element_by_xpath("//*[@id='pane-1']/div/button[3]/span").click()
# time.sleep(1)
# z.find_element_by_xpath("//*[@id= 'pane-1']/ul/li[1]/button[2]").click()
#选择客户颜色
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[7]/div[1]/input").send_keys("red")
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[7]/div[2]/input").send_keys("听一千次花开的声音，等那一双清澈的眼")
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[2]/div[8]/textarea").send_keys(
    "1：抽用我司来纱, 按我司提供的模数图排纱，特别注意针路，起横，黄白纱，色仟等问题，注意卫衣不能露丝，露底"
    "2：要求成品规格跟足我司要求，横直平均缩水 5%以内，扭度3%以内，纬斜10以内"
    "3：纱长请参照我司提供数据，织开机办给我司批核再开货"
    "4：每匹布要包好布头方可交染厂，防止胚污;，出货码单一定要对应用纱并注明颜色，不可混乱"
    "5：如在织造过程出现需要染黑或要除油的胚布一定要分开等我司通知再统一出货，不可混在正常胚布出，如无注明出现质量问题全部由贵厂承担，如织造过程如发现有纱质或织造问题一定要及时通知我司或现场跟单看布，如无知会造成质量损失由贵厂承担"
    "6：黄油笔请写布头15公分内，布飞码单请注明染色颜色")
# z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[4]/div[3]/table/tbody/tr/td[1]/div/div/div/div[1]/span/span/i").click()
time.sleep(2)
# z.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[1]").click()
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[4]/div[3]/table/tbody/tr/td[2]/div/div/input").send_keys("100")
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[4]/div[3]/table/tbody/tr/td[3]/div/div/input").send_keys("蓝湛")
z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/div[4]/div[3]/table/tbody/tr/td[5]/div/div/input").send_keys("1")
selector = Select(z.find_element_by_xpath("//*[@id='__layout']/section/section/div[2]/section/div[2]/div[3]/ul/li[1]/ul/li[2]/span[2]/div/div/span/span/i").click())
time.sleep(1)
selector.select_by_visible_text("6#")


                                                                                        







