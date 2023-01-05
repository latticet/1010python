from selenium import webdriver
import time


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.itsource.cn')
        time.sleep(1)

    def scroll1(self):
        # TODO 第一种
        # 滚动条滚动页面末尾
        # window.scrollTo(x坐标， y坐标)
        js1 = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js1)
        time.sleep(1)

        # 滚动条滚到到页面顶部
        js2 = 'window.scrollTo(0, 0)'
        self.driver.execute_script(js2)
        time.sleep(1)

        # TODO 第二种
        # window.scrollTo(options)
        # 平滑滚动到页面底部
        js3 = 'window.scrollTo({top:document.body.scrollHeight, left:0, behavior:"smooth"})'
        self.driver.execute_script(js3)
        time.sleep(1)

        # 平滑滚动到页面顶部
        js4 = 'window.scrollTo({top:0, left:0, behavior:"smooth"})'
        self.driver.execute_script(js4)

    def scroll2(self):
        # 定位要滚动到位置的元素
        div_element = self.driver.find_element_by_xpath('//div[text()="源码动态"]')

        # 滚动条滚动到目标元素
        self.driver.execute_script('arguments[0].scrollIntoView()', div_element)

    def quit(self, seconds=5):
        time.sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.scroll1()
    # case.scroll2()

    case.quit(100)
