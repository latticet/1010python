import time

from selenium import webdriver

driver = webdriver.Chrome()
# 打开百度
driver.get('http://www.baidu.com')

# 点击新闻链接
driver.find_element_by_link_text('新闻').click()

# 获取所有窗口句柄
print(driver.window_handles)
# 获取当前窗口句柄
print(driver.current_window_handle)
print('--' * 20)

# 关闭当前窗口
# driver.close()

# 切换窗口
driver.switch_to.window(driver.window_handles[1])

# 获取所有窗口句柄
print(driver.window_handles)
# 获取当前窗口句柄
print(driver.current_window_handle)
time.sleep(1)

driver.close()