from selenium import webdriver


class TestCase:
    def __init__(self):
        # 打开浏览器，创建驱动对象
        self.driver = webdriver.Chrome()
        # 请求目标网址-百度
        self.driver.get('https://www.baidu.com')

    def id(self):
        # TODO id定位
        # driver.get_find_element_by_id(id值)
        id_kw_element = self.driver.find_element_by_id('kw')
        print(id_kw_element.get_attribute('outerHTML'))

        id_su_element = self.driver.find_element_by_id('su')
        print(id_su_element.get_attribute('outerHTML'))

    def class_name(self):
        # TODO classname定位
        # driver.get_find_element_by_class_name(class值)
        print(self.driver.find_element_by_class_name('s_ipt').get_attribute('outerHTML'))
        print(self.driver.find_element_by_class_name('s_btn').get_attribute('outerHTML'))

    def link_text(self):
        # TODO 链接文本定位
        # <a href='#'>链接文本</a>
        # 定位新闻链接
        print(self.driver.find_element_by_link_text('新闻').get_attribute('outerHTML'))
        # 定位图片链接
        print(self.driver.find_element_by_link_text('图片').get_attribute('outerHTML'))

    def partial_link_text(self):
        # TODO 部分链接文本定位
        # hao123链接
        print(self.driver.find_element_by_partial_link_text('hao').get_attribute('outerHTML'))
        print(self.driver.find_element_by_partial_link_text('123').get_attribute('outerHTML'))

    def name(self):
        # TODO name属性定位
        print(self.driver.find_element_by_name('wd').get_attribute('outerHTML'))
        print(self.driver.find_element_by_name('ie').get_attribute('outerHTML'))

    def tag_name(self):
        # TODO 标签名定位
        print(self.driver.find_element_by_tag_name('input').get_attribute('outerHTML'))
        print(self.driver.find_element_by_tag_name('a').get_attribute('outerHTML'))


if __name__ == '__main__':
    case = TestCase()

    # id定位
    # case.id()

    # class定位
    # case.class_name()

    # 链接文本定位
    # case.link_text()

    # 部分链接文本定位
    # case.partial_link_text()

    # name属性定位
    # case.name()

    # 标签名定位
    case.tag_name()

    # 退出浏览器
    case.driver.quit()
