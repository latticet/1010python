from selenium import webdriver
import os

# 打开浏览器
driver = webdriver.Chrome()

# 请求目标网址
url = os.path.join(os.path.abspath('html'), 'frame.html')
driver.get(url)

# 元素定位
# TODO frame
# 定位frame页面中的元素
print(driver.find_element_by_tag_name('h3').get_attribute('outerHTML'))
print('--' * 20)

# 定位inner页面中的元素
# print(driver.find_element_by_id('inner_h3'))   # 定位不到
# TODO inner
# 切换frame-inner
# 语法：driver.switch_to.frame(frame)
# frame：frame的id|frame的name|selenium获取的标签对象
# id
# driver.switch_to.frame('f1')
# name
driver.switch_to.frame('inner')
print(driver.find_element_by_id('inner_h3').get_attribute('outerHTML'))
print('--' * 20)

# 定位inner_sub中的元素
# print(driver.find_element_by_id('p1'))   # 定位不到

# TODO inner-sub
# 切换frame - inner-sub
f2_iframe_element = driver.find_element_by_id('f2')
driver.switch_to.frame(f2_iframe_element)
print(driver.find_element_by_id('p1').get_attribute('outerHTML'))
print('==' * 20)

# 定位inner页面中的元素
# print(driver.find_element_by_id('inner_h3').get_attribute('outerHTML'))  # 定位不到

# TODO inner
# 从inner-sub切换到inner
driver.switch_to.parent_frame()
print(driver.find_element_by_id('inner_h3').get_attribute('outerHTML'))
print('--' * 20)

# TODO frame
# 从inner切换到frame
driver.switch_to.parent_frame()
print(driver.find_element_by_tag_name('h3').get_attribute('outerHTML'))
print('--' * 20)

# TODO inner_sub
# frame->inner->inner_sub
driver.switch_to.frame('f1')
driver.switch_to.frame('f2')

# TODO frame
# inner_sub -> frame
# 切换到主页面
driver.switch_to.default_content()
print(driver.find_element_by_tag_name('h3').get_attribute('outerHTML'))

# 退出浏览器
driver.quit()
