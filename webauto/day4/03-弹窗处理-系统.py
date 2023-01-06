from selenium import webdriver
import os
import time


class TestCase:
    def __init__(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()

        # 请求目标网址
        url = os.path.join(os.path.abspath('html'), 'popup.html')
        self.driver.get(url)
        self.buttons = self.driver.find_elements_by_tag_name('button')

    def alert(self):
        """alert弹窗"""
        alert_btn = self.buttons[0]
        alert_btn.click()
        time.sleep(1)

        # TODO 获取当前弹窗（切换弹窗）
        alert = self.driver.switch_to.alert
        #  alert.accept() 确定
        alert.accept()

        # 定位div
        print(self.driver.find_element_by_tag_name('div').get_attribute('outerHTML'))

    def confirm(self):
        """confirm弹窗"""
        self.buttons[1].click()
        time.sleep(1)

        # 获取当前弹窗
        alert = self.driver.switch_to.alert
        # 确定
        # alert.accept()
        # 取消
        alert.dismiss()

    def prompt(self):
        """prompt弹窗"""
        self.buttons[2].click()
        time.sleep(1)

        # 获取当前窗口
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()
        # alert.dismiss()


if __name__ == '__main__':
    case = TestCase()
    # case.alert()
    # case.confirm()
    case.prompt()
