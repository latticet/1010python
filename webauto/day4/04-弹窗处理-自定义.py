from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
driver.get('https://itsource.cn/')
time.sleep(2)

# driver.find_element_by_xpath('//*[@id="iframe_company_mini_div"]/h6/span[2]').click()

js = "document.getElementById('iframe_company_mini_div').style.display='none'"
driver.execute_script(js)

