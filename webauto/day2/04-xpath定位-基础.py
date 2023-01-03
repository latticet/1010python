import time

from selenium import webdriver
import os
from pprint import pprint

"""
xpath: xml path language(xml 路径查找语言)
xml: 可以自定义标签的标签语言
html作用: 渲染页面
xml作用：存储数据，数据传输
"""
# 刘杨18成都1000
# 贺倩19重庆1000

# json
# xml
"""
<?xml version="1.0" encoding="UTF-8"?>
<class>
    <student>
        <name>刘杨</name>
        <age>18</age>
    </student>
    <student>
        <name>贺倩</name>
        <age>19</age>
    </student>
</class>
"""
# 打开浏览器
driver = webdriver.Chrome()

# 获取资源的绝对路径 os.path.abspath('资源')
resource_path = os.path.abspath('resource')

# 路径拼接  os.path.join(路径, 路径)
# 请求目标网址
url = os.path.join(resource_path, 'xpath定位页面.html')

# driver.get(路径)
driver.get(url)

# 定位元素
# driver.find_element_by_xpath(xpath语法)
# TODO 绝对路径
"""
# h1: /html/body/div/h1
print(driver.find_element_by_xpath('/html/body/div/h1').get_attribute('outerHTML'))
print('==' * 20)
# ul
print(driver.find_element_by_xpath('/html/body/ul').get_attribute('outerHTML'))
print('==' * 20)
# li
print(driver.find_element_by_xpath('/html/body/ul/li').get_attribute('outerHTML'))
print('==' * 20)
li_list = driver.find_elements_by_xpath('/html/body/ul/li')
pprint(li_list)
print(len(li_list))
"""

# 相对路径
# h1
# 查找当前页面中所有的h1标签
print(driver.find_element_by_xpath('//h1').get_attribute('outerHTML'))
print('==' * 20)
for element in driver.find_elements_by_xpath('//h1'):
    print(element.get_attribute('outerHTML'))
print('==' * 20)

# //div/h1


# ul
# li



# 退出浏览器
time.sleep(5)
driver.quit()
