from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.sina.com.cn')
# 隐式等待
driver.implicitly_wait(10)   # 最长10s

a_elements = driver.find_elements_by_link_text('佛学')
print(a_elements)
