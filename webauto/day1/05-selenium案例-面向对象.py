from selenium import webdriver
import time


class TestCase:
    def __init__(self):
        # 打开浏览器，返回驱动对象
        self.driver = webdriver.Chrome()

    def get_baidu(self):
        # 请求百度
        time.sleep(1)
        self.driver.get('https://www.baidu.com')

        # 搜索框输入关键字
        time.sleep(1)
        self.driver.find_element_by_id('kw').send_keys('天气预报')

        # 点击百度一下
        time.sleep(1)
        self.driver.find_element_by_id('su').click()

        # 获取标题
        time.sleep(1)
        print(self.driver.title)

    def get_so(self):
        # www.so.com
        pass


    def quit(self, seconds=0):
        time.sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.get_baidu()

    case.quit()
