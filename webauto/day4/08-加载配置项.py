from selenium import webdriver

# 创建option对象
options = webdriver.ChromeOptions()
# 注意：路径中不需要default
user_data_dir = r'--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data'
options.add_argument(user_data_dir)

# 打开浏览器，设置options
driver = webdriver.Chrome(options=options)
# 默认情况，selenium打开浏览器不会加载任何配置信息
driver.get('https://mail.163.com')
