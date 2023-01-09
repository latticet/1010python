from common.base import Base, By, get_driver, time

"""
作用：封装当前页面的操作
类名：
    IndexPage(Base)
方法：
    input_kw_send_keys
    input_submit_click
"""


class IndexPage(Base):
    def input_kw_send_keys(self, content):
        """搜索框输入内容"""
        self.send_keys((By.ID, 'kw'), content)

    def input_submit_click(self):
        """百度一下按钮点击"""
        self.click((By.ID, 'su'))


if __name__ == '__main__':
    # 打开浏览器
    driver = get_driver()
    index_page = IndexPage(driver)

    # 请求目标网址
    index_page.get('http://www.baidu.com')

    # 方法调用
    index_page.input_kw_send_keys('天气预报')
    time.sleep(1)
    index_page.input_submit_click()
    index_page.quit(3)
