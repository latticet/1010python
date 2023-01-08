from selenium import webdriver
import time
from pprint import pprint


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        time.sleep(1)

    def get_cookies(self):
        # driver.get_cookies()	获得所有cookie 信息
        pprint(self.driver.get_cookies())

    def get_cookie(self):
        # driver.get_cookie(name)	返回特定name 的cookie 信息
        print(self.driver.get_cookie('ZFY'))

    def add_cookie(self):
        # driver.add_cookie(cookie_dict)	添加cookie，必须有name 和value 值
        cookie = {
            'name': 'hello',
            'value': '你好'
        }
        self.driver.add_cookie(cookie)

    def delete_cookie(self):
        # driver.delete_cookie(name)	删除特定(部分)的cookie 信息
        self.driver.delete_cookie('hello')

    def delete_all_cookies(self):
        # driver.delete_all_cookies()	删除所有cookie 信息
        self.driver.delete_all_cookies()


if __name__ == '__main__':
    case = TestCase()
    # case.get_cookies()
    # case.get_cookie()
    # case.add_cookie()
    # case.delete_cookie()
    case.delete_all_cookies()
    case.get_cookies()
