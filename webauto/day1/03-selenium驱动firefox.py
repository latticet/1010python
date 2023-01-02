# 导入selenium下的webdriver
from selenium import webdriver
import time

# 打开chrome浏览器, 返回浏览器驱动对象
driver = webdriver.Firefox()
time.sleep(2)

# 请求百度
driver.get('https://www.baidu.com')
time.sleep(2)

# 退出浏览器
driver.quit()

