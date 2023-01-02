from selenium import webdriver
import time

# 1. 打开浏览器
driver = webdriver.Chrome()
time.sleep(1)

# 2. 地址栏输入百度网址
driver.get('https://www.baidu.com')
time.sleep(1)

# 3. 搜索框输入“天气预报”
driver.find_element_by_id('kw').send_keys('天气预报')
time.sleep(1)

# 4. 点击“百度一下”按钮
driver.find_element_by_id('su').click()
time.sleep(2)

# 5. 退出浏览器
driver.quit()