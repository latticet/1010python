from selenium import webdriver
from pprint import pprint

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
driver.get('http://www.baidu.com')
hot_list = driver.find_elements_by_class_name('hotsearch-item')
# pprint(hot_list)

print(hot_list[2].get_attribute('outerHTML'))

# 退出浏览器
driver.quit()