# 导入selenium下的webdriver
from selenium import webdriver
import time

# 打开chrome浏览器, 返回浏览器驱动对象
driver = webdriver.Chrome()

# 请求目标网址
# 说明：向目标网址发起GET请求
# 注意：目标网址要写完整网址
# driver.get(目标网址)
time.sleep(2)
driver.get('https://www.baidu.com')
time.sleep(2)

# 退出浏览器
driver.quit()

