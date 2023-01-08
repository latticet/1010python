from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()
# 请求百度
driver.get('http://www.baidu.com')

# 设置登录的cookie到当前浏览器中
login_cookies = [
    {
        "name": "BDUSS",
        "value": "gzRjF-VE1uR3RSQnN3RVNsUGxvZVdWMjhacVlZbTROdEt-emkwa1Uxcnl5dUZqSVFBQUFBJCQAAAAAAAAAAAEAAABmRcgnyvOx6rXmZGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPI9umPyPbpjTF"
    },
    {
        "name": "BDUSS_BFESS",
        "value": "gzRjF-VE1uR3RSQnN3RVNsUGxvZVdWMjhacVlZbTROdEt-emkwa1Uxcnl5dUZqSVFBQUFBJCQAAAAAAAAAAAEAAABmRcgnyvOx6rXmZGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPI9umPyPbpjTF"
    }
]
for cookie in login_cookies:
    driver.add_cookie(cookie)

driver.refresh()
