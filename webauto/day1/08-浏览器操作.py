from selenium import webdriver
import time


class TestCase:
    def __init__(self):
        # 创建驱动对象
        self.driver = webdriver.Chrome()

    def window_size(self):
        """浏览器窗口大小设置"""
        time.sleep(1)
        # 设置浏览器宽480、高800
        self.driver.set_window_size(480, 800)

        time.sleep(1)
        # 浏览器窗口最大化
        self.driver.maximize_window()

        time.sleep(1)
        # 浏览器窗口最小化
        self.driver.minimize_window()

    def forward_back(self):
        """浏览器页面前进后退"""
        # 请求百度
        self.driver.get('https://www.baidu.com')
        time.sleep(2)

        # 浏览器后退
        self.driver.back()
        time.sleep(2)

        # 浏览器前进
        self.driver.forward()

    def refresh(self):
        """浏览器页面刷新"""
        # 请求百度
        self.driver.get('https://www.baidu.com')
        time.sleep(2)

        # 浏览器刷新
        self.driver.refresh()

    def close(self):
        """关闭当前窗口"""
        # 打开百度
        self.driver.get('http://www.baidu.com')
        time.sleep(2)

        # 点击新闻链接
        # 通过链接文本定位标签
        self.driver.find_element_by_link_text('新闻').click()
        time.sleep(2)

        # 关闭当前窗口
        self.driver.close()

    def quit(self, seconds=3):
        time.sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # 览器窗口大小设置
    # case.window_size()

    # 浏览器页面前进后退
    # case.forward_back()

    # 浏览器刷新
    # case.refresh()

    # 关闭当前窗口
    case.close()
    case.quit()
