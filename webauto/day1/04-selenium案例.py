from selenium import webdriver
import time

# 1、打开Chrome，打开百度首页
# 打开chrome浏览器，返回驱动对象
driver = webdriver.Chrome()
time.sleep(1)

# 请求目标网址-百度首页
driver.get('https://www.baidu.com')
time.sleep(2)

# 2、搜索框输入天气预报，点击百度一下
# 元素定位
# id元素定位：通过标签的id来定位元素
# WebElement对象
kw_element = driver.find_element_by_id('kw')
# 输入框输入内容
# WebElement对象.send_keys('内容')
kw_element.send_keys('天气预报')

# 点击百度一下
# 通过id定位百度一下标签
driver.find_element_by_id('su').click()

# 3、等待2秒
time.sleep(2)


# 4、获取页面标题，并打印出来
# driver.title 获取当前页面的标题
print(driver.title)

# 5、检查'天气’关键字是否在标题中
print('天气' in driver.title)


# 6、关闭Chrome浏览器
time.sleep(3)
driver.quit()

"""
总结：
1. 元素定位
driver.find_element_by_id('id值')   
    通过id定位元素
    返回WebElement对象
2. WebElement对象
    WebElement.send_keys()  输入框输入内容
    WebElement.click()  点击操作
3. driver
    driver.title 获取当前页面的标题
"""