from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.sahitest.com/demo/selectTest.htm')
        time.sleep(1)

    def select1(self):
        """
        第一种：普通方式
        :return:
        """
        # 选中email
        email_element = self.driver.find_element_by_xpath('//option[@value="48"]')
        email_element.click()

        # 选中id2
        id2_element = self.driver.find_element_by_id('id2')
        id2_element.click()
        time.sleep(1)

        # 先定位select，然后在定位要选中的option
        s1_element = self.driver.find_element_by_id('s1')
        # WebElement.find_element_by_xx()
        home_phone_element = s1_element.find_element_by_xpath('//option[@value="51"]')
        home_phone_element.click()

    def select2(self):
        """
        第二种： select对象方式
        :return:
        """
        # 定位要选择的select
        s1_element = self.driver.find_element_by_id('s1')

        # TODO 创建select对象
        select = Select(s1_element)

        # TODO 选择选项
        # 1. select.select_by_index(index)  通过索引值选择option
        select.select_by_index(3)
        time.sleep(1)
        # 2. select.select_by_value(value值) 通过value属性选择option
        select.select_by_value('49')
        time.sleep(1)
        # select.select_by_visible_text(文本内容) 通过内容选择option
        select.select_by_visible_text('Mail')

    def quit(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.select1()
    case.select2()

    case.quit()
