from selenium import webdriver

# 创建options对象
options = webdriver.ChromeOptions()
# 添加参数
options.add_argument('-headless')

# 打开浏览器
driver = webdriver.Chrome(options=options)
# 访问目标网址
driver.get('https://www.baidu.com')
# 获取当前标题
print(driver.title)
# 退出浏览器
driver.quit()