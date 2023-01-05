from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址-百度
driver.get('http://www.baidu.com')
time.sleep(1)

# 在搜索框输入-天气预报
kw = driver.find_element_by_id('kw')
kw.find_element_by_id()


kw.send_keys('天气预报')
time.sleep(1)

# 选中搜索框中的关键字
kw.send_keys(Keys.CONTROL, 'a')
time.sleep(1)

# 复制搜索框中的关键字
kw.send_keys(Keys.CONTROL, 'c')
time.sleep(1)

# 请求目标网址-360搜索
driver.get('http://www.so.com')
time.sleep(1)

# 搜索框中粘贴当前复制的内容
input = driver.find_element_by_id('input')
input.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 回车搜索
input.send_keys(Keys.ENTER)
time.sleep(3)

# 退出浏览器
driver.quit()
