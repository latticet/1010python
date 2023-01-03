from selenium import webdriver
from pprint import pprint


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def find_element_by_xx(self):
        # TODO driver.find_element_by_xx
        # 说明：定位匹配到的第一个元素,如果没有匹配到会抛出错误
        # 通过标签名定位  driver.find_element_by_tag_name('标签名')
        input_web_element = self.driver.find_element_by_tag_name('input')
        # WebElement.get_attribute(属性名)  通过标签属性名获取属性值
        print(input_web_element.get_attribute('outerHTML'))  # outerHTML:标签内容

        # 通过id定位  driver.find_element_by_id('id名')
        # 定位不到抛出错误
        self.driver.find_element_by_id('abcd')

    def find_elements_by_xx(self):
        # TODO driver.find_elements_by_xx()
        # 定位匹配到的所有元素,返回一个列表.匹配不到,返回空列表
        # input标签
        input_list = self.driver.find_elements_by_tag_name('input')
        pprint(input_list)
        print(len(input_list))

        id_list = self.driver.find_elements_by_id('abcd')
        print(id_list)

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()

    # find_element_by_xx
    # case.find_element_by_xx()

    # find_elements_by_xx
    case.find_elements_by_xx()

    case.quit()
