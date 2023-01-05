import time

from selenium import webdriver
import os

# 打开浏览器
driver = webdriver.Chrome()

"""
print(__file__)
work_path = os.path.dirname(__file__)
# 路径拼接方法  os.path.join(路径1， 路径2， 路径n)
a_path = os.path.join(work_path, 'resource', 'A.html')
print(a_path)
print('==' * 20)

"""
# 获取资源所在的目录
resource_path = os.path.abspath('resource')
a_path = os.path.join(resource_path, 'A.html')

# 请求目标网址
driver.get(a_path)

# 定位标签
h1_element = driver.find_element_by_tag_name('h1')
print(h1_element.get_attribute('outerHTML'))

p_list = driver.find_elements_by_tag_name('p')
for p_element in p_list:
    print(p_element.get_attribute('outerHTML'))

# 退出浏览器
time.sleep(5)
driver.quit()
