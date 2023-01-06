from selenium import webdriver
import os
import time

# 创建options对象
options = webdriver.ChromeOptions()
download_path = os.path.abspath('download')
prefs = {
    'profile.default_content_settings.popups': 0,  # 取消弹窗
    'download.default_directory': download_path  # 设置保存位置
}
options.add_experimental_option('prefs', prefs)

# 打开浏览器，设置options
driver = webdriver.Chrome(options=options)

# 请求目标网址
driver.get('https://pypi.org/project/requests/#files')
time.sleep(1)

# 下载操作，点击下载的链接
requests_element = driver.find_element_by_partial_link_text('requests-2.28.1.tar.gz')
requests_element.click()
