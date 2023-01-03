from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
driver.get('http://www.baidu.com')
time.sleep(2)

# TODO driver.find_element_by_css_selector(css选择器)
# 基础选择器
"""
print(driver.find_element_by_css_selector('.s_ipt').get_attribute('outerHTML'))
print(driver.find_element_by_css_selector('#kw').get_attribute('outerHTML'))
print(driver.find_element_by_css_selector('*').get_attribute('outerHTML'))
"""

# 复合选择器
"""
print(driver.find_element_by_css_selector('span').get_attribute('outerHTML'))
print(driver.find_element_by_css_selector('#form span').get_attribute('outerHTML'))
print(driver.find_element_by_css_selector('#form>span').get_attribute('outerHTML'))
"""

# 伪类选择器
# css索引
# print(driver.find_element_by_css_selector('#form>input:nth-child(3)').get_attribute('outerHTML'))
# 第11个子的input标签
# print(driver.find_element_by_css_selector('#form>input:nth-child(11)').get_attribute('outerHTML'))

# 属性定位
# [属性名=属性值]
print(driver.find_element_by_css_selector('[autocomplete="off"]').get_attribute('outerHTML'))
# 定位属性maxlength="255"的任意标签
print(driver.find_element_by_css_selector('[maxlength="255"]').get_attribute('outerHTML'))
# 定位属性maxlength="255"的input的标签
print(driver.find_element_by_css_selector('input[maxlength="255"]').get_attribute('outerHTML'))
# 选择器：定位属性名叫做maxlength的标签
print(driver.find_element_by_css_selector('[maxlength]').get_attribute('outerHTML'))

print(driver.find_element_by_css_selector('[maxlength="255"][name="wd"]').get_attribute('outerHTML'))











# 退出浏览器
driver.quit()