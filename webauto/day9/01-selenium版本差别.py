from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# TODO selenium3.0
# 定位
# driver.find_element_by_id()

# TODO selenium4.0
# 单数
# driver.find_element(By.xx， 定位值)
driver.find_element(By.ID, 'su')

# 复数
# driver.find_elements(By.xx， 定位值)

# 3.0早期用法
driver.switch_to_frame()

# 4.0
# driver.switch_to.frame()
# driver.switch_to.alert
# driver.switch_to.window()
