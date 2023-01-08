from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 打开浏览器
driver = webdriver.Chrome()

# 请求百度
driver.get('http://www.baidu.com')

# TODO until
# result = WebDriverWait(driver, 5).until(EC.title_is('百度一下，你就知道1'), message='标题不一致')

# TODO until_not
# result = WebDriverWait(driver, 5).until_not(EC.title_is('百度一下，你就知道'), message='标题不一致')

# TODO expected_conditions
# result = WebDriverWait(driver, 5).until(EC.title_is('百度一下，你就知道1'), message='标题不一致')

# EC.presence_of_element_located(locator)
# locator : (定位方式， 定位语法)
# ('id', 'kw')
# (By.ID, 'kw')
# ('id', 'su')
# ('xpath', 'xxx')
# ('link text', 'xxx')
# input#kw
# 显示等待返回的结果
# 1. until的method方法中返回的值
# 2. until在最长时间没有返回最终结果，抛出TimeoutException
"""
kw_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'kw1')))
# print(kw_element.get_attribute('outerHTML'))
print(kw_element)
"""
"""
input_elements = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located([By.TAG_NAME, 'input']))
print(input_elements)
print(len(input_elements))
"""

print(WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.LINK_TEXT, '新闻'), '新')))
print(WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.LINK_TEXT, '新闻'), '闻1')))

# input#kw
# element:  driver.find_element_by_id('kw')
# locator: (id, 'kw')
