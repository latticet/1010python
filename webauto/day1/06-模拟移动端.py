import time

from selenium import webdriver

# 创建options对象
options = webdriver.ChromeOptions()
# 添加配置项
options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone SE'})

# 打开浏览器
driver = webdriver.Chrome(options=options)
time.sleep(2)

# 请求百度
driver.get('https://www.baidu.com')
time.sleep(2)

# 输入关键字，点击
driver.find_element_by_id('index-kw').send_keys('selenium')
time.sleep(1)
driver.find_element_by_id('index-bn').click()
time.sleep(3)

# 退出浏览器
driver.quit()

