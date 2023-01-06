from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
url = os.path.join(os.path.abspath('html'), 'form_radio_checkbox.html')
driver.get(url)
time.sleep(1)

# TODO 上传文件操作
# 定位上传的表单域，然后send_keys传入资源（绝对路径）
file_element = driver.find_element_by_xpath('//input[@type="file"]')
resource_path = os.path.join(os.path.abspath('images'), 'cat.webp')
file_element.send_keys(resource_path)
