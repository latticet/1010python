from selenium import webdriver
import os
import time


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        url = os.path.join(os.path.abspath('html'), 'form_radio_checkbox.html')
        self.driver.get(url)
        time.sleep(1)

    def radio(self):
        """单选"""
        # 定位要选择的标签然后点击
        radio1 = self.driver.find_element_by_xpath('//input[@type="radio"]')
        radio2 = self.driver.find_element_by_xpath('//input[2]')
        radio1.click()
        print(radio1.is_selected())
        print(radio2.is_selected())

        time.sleep(1)

        radio2.click()
        print(radio1.is_selected())
        print(radio2.is_selected())

    def checkbox(self):
        """多选"""
        checkboxes = self.driver.find_elements_by_xpath('//input[@type="checkbox"]')
        # 选中python和linux
        checkboxes[0].click()
        time.sleep(1)
        checkboxes[2].click()

        # 反向选择
        for checkbox_element in checkboxes:
            time.sleep(1)
            checkbox_element.click()


if __name__ == '__main__':
    case = TestCase()
    # case.radio()

    case.checkbox()
