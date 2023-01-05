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

    def quit(self, seconds=3):
        time.sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.attribute()

    case.quit()
