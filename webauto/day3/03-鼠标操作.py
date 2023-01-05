import os

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class TestCase:
    def __init__(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        # 请求目标网址
        self.driver.get('https://www.sahitest.com/demo/clicks.htm')
        self.ac = ActionChains(self.driver)
        time.sleep(1)

    def click(self):
        """单击"""
        # 第一种：简单方式
        click_element = self.driver.find_element_by_xpath('//input[@value="click me"]')
        # click_element.click()

        # 第二种：ac对象
        # TODO 创建ac对象
        ac = ActionChains(self.driver)
        # 给click_element元素绑定了单击事件，然后perform执行
        ac.click(click_element).perform()

    def context_click(self):
        """右击"""
        # 创建ac对象

        # 调用事件方法并执行
        right_element = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        self.ac.context_click(right_element).perform()

    def double_click(self):
        """双击"""
        dbl_element = self.driver.find_element_by_css_selector('input[value="dbl click me"]')
        self.ac.double_click(dbl_element).perform()

    def drag_and_drop(self):
        """拖动"""
        # 请求目标网址
        self.driver.get('https://www.sahitest.com/demo/dragDropMooTools.htm')
        # 定位元素
        source_element = self.driver.find_element_by_id('dragger')
        target_element = self.driver.find_element_by_xpath('//div[4]')
        # 执行拖动
        self.ac.drag_and_drop(source_element, target_element).perform()

    def move_to_element(self):
        """悬停"""
        self.driver.get('https://www.sahitest.com/demo/mouseover.htm')

        # 定位元素
        input_element = self.driver.find_element_by_name('b1')

        # 悬停操作
        self.ac.move_to_element(input_element).perform()

    def click_and_hold(self):
        """按下鼠标左键在一个元素上"""
        # 请求目标网址
        url = os.path.join(os.path.abspath('html'), 'mouse_hold.html')
        self.driver.get(url)

        # 定位标签
        btn_element = self.driver.find_element_by_id('btn1')

        # 执行事件
        self.ac.click_and_hold(btn_element).perform()

    def quit(self):
        # 退出浏览器
        time.sleep(10)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.click()
    # case.context_click()
    # case.double_click()
    # case.drag_and_drop()
    # case.move_to_element()
    case.click_and_hold()

    case.quit()
