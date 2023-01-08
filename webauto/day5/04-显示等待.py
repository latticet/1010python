from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 打开浏览器
driver = webdriver.Chrome()

# 请求百度
driver.get('http://www.baidu.com')

# result = WebDriverWait(driver, 5).until(EC.title_is('百度一下，你就知道1'), message='标题不一致')
# result = WebDriverWait(driver, 5).until_not(EC.title_is('百度一下，你就知道'), message='标题不一致')



result = WebDriverWait(driver, 5).until(EC.title_is('百度一下，你就知道1'), message='标题不一致')