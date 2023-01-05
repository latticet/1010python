from selenium import webdriver
import time


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def attribute(self):
        """常用属性"""
        # driver.name 浏览器名称
        print(self.driver.name)

        # driver.current_url  当前url
        print(self.driver.current_url)

        # driver.title 当前页面标题
        print(self.driver.title)
        print('==' * 20)

        # driver.page_source 当前页面源码
        # print(self.driver.page_source)
        # print('==' * 20)

        # 打开新闻页面
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.find_element_by_link_text('贴吧').click()

        # driver.current_window_handle 当前窗口句柄
        print(self.driver.current_window_handle)
        print('--' * 20)

        # driver.window_handles   列表：所有窗口的句柄（id） 打开浏览器的所有窗口句柄
        print(self.driver.window_handles)

    def quit(self, seconds=3):
        time.sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.attribute()

    case.quit(10)
