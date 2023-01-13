from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, WebDriverException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

"""
作用：对selenium进行二次封装，供page包中的类继承
类名：
    Base
方法:
    __init__: 创建driver对象
    get: 请求目标网址
    find_element: 单数元素定位
    find_elements: 复数元素定位
    send_keys: 表单域输入内容
    click: 点击操作
"""


def get_driver(browser='chrome'):
    if browser == 'chrome':
        return webdriver.Chrome()
    else:
        return webdriver.Firefox()


class Base:
    def __init__(self, driver):
        # 初始化driver
        self.driver = driver

    def get(self, url):
        # 请求目标网址
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(5)
        except (InvalidArgumentException, WebDriverException) as e:
            print(e)

    def find_element(self, locator, timeout=5, poll_frequency=0.5):
        """
        单数元素定位
        :param locator: 定位器  (定位方式，定位值)
        :param timeout: 最长定位时间
        :param poll_frequency: 间隔时间
        :return: WebElement|None
        """
        try:
            return WebDriverWait(self.driver, timeout, poll_frequency) \
                .until(EC.presence_of_element_located(locator), message='单数元素定位失败')
        except TimeoutException as e:
            # print(e)
            pass

    def find_elements(self, locator, timeout=5, poll_frequency=0.5):
        """
        单数元素定位
        :param locator: 定位器  (定位方式，定位值)
        :param timeout: 最长定位时间
        :param poll_frequency: 间隔时间
        :return: []
        """
        try:
            return WebDriverWait(self.driver, timeout, poll_frequency) \
                .until(EC.presence_of_all_elements_located(locator), message='复数元素定位失败')
        except TimeoutException as e:
            # print(e)
            return []

    def send_keys(self, locator, content):
        """表单域输入内容"""
        element = self.find_element(locator)
        if element:
            element.send_keys(content)

    def click(self, locator):
        element = self.find_element(locator)
        if element:
            element.click()

    def text(self, locator):
        element = self.find_element(locator)
        if element:
            return element.text

    def quit(self, seconds=0):
        time.sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    driver = get_driver()
    base = Base(driver)

    base.get('http://www.baidu.com/')
    # 域名格式不正确： selenium.common.exceptions.InvalidArgumentException
    # 访问不存在的网址：selenium.common.exceptions.WebDriverException

    kw = base.find_element((By.ID, 'kw1'), timeout=1)
    print(kw)
    print('==' * 20)

    inputs = base.find_elements((By.TAG_NAME, 'input1'), timeout=1)
    print(inputs)
    print(len(inputs))
