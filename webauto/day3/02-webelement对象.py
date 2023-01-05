import os

from selenium import webdriver
import time


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # 浏览器窗口最大化
        self.driver.get('http://www.baidu.com')

    def attribute(self):
        """WebElement对象属性"""
        # id id标识
        kw_element = self.driver.find_element_by_id('kw')
        print(kw_element.id)
        print('--' * 20)

        # size # 宽高
        print(kw_element.size)

        # rect 宽高和坐标
        print(kw_element.rect)

        # tag_name  # 标签名
        print(kw_element.tag_name)

        # text # 文本内容
        print('input:', kw_element.text)
        news_element = self.driver.find_element_by_link_text('新闻')
        print('a:', news_element.text)

    def send_keys(self):
        """在文本域中输入内容"""
        # 定位输入框
        kw = self.driver.find_element_by_id('kw')
        # 输入内容
        kw.send_keys('hello world')

    def clear(self):
        """清空文本域中的内容"""
        time.sleep(1)
        kw = self.driver.find_element_by_id('kw')
        kw.clear()

    def click(self):
        """可以点击的标签 a input:button input:submit"""
        self.driver.find_element_by_id('kw').send_keys('hello')
        su = self.driver.find_element_by_id('su')
        su.click()

    def get_attribute(self):
        """获取标签属性"""
        kw = self.driver.find_element_by_id('kw')
        print(kw.get_attribute('id'))
        print(kw.get_attribute('name'))
        print(kw.get_attribute('class'))
        print(kw.get_attribute('autocomplete'))
        print(kw.get_attribute('outerHTML'))

    def is_displayed(self):
        """判断元素是否可见"""
        # 请求目标网址
        url = os.path.join(os.path.abspath('html'), 'webelement.html')
        self.driver.get(url)

        # 定位元素
        div1 = self.driver.find_element_by_id('div1')
        div2 = self.driver.find_element_by_id('div2')

        # 可见性方法
        print(div1.is_displayed())
        print(div2.is_displayed())

    def is_enabled(self):
        """判断元素是否可用"""
        # 请求目标网址
        url = os.path.join(os.path.abspath('html'), 'webelement.html')
        self.driver.get(url)

        # 定位元素
        ipt1 = self.driver.find_element_by_xpath('//input[@name="input1"]')
        ipt2 = self.driver.find_element_by_xpath('//input[@name="input2"]')

        # 判断是否可用
        print(ipt1.is_enabled())
        print(ipt2.is_enabled())

    def quit(self, seconds=3):
        time.sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.attribute()

    # case.send_keys()
    # case.clear()
    # case.click()
    # case.get_attribute()
    # case.is_displayed()

    case.is_enabled()

    case.quit()
