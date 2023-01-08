from selenium import webdriver
import time


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://mail.163.com')
        time.sleep(1)

    def login(self):
        # 登录操作
        # 切换到登录页面的frame
        iframe = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(iframe)

        # 定位登录相关的元素
        email_element = self.driver.find_element_by_name('email')
        password_element = self.driver.find_element_by_name('password')
        do_login_element = self.driver.find_element_by_id('dologin')

        # 登录操作
        email_element.send_keys('itsourcetest')
        password_element.send_keys('Itsource123.')
        do_login_element.click()
        time.sleep(2)

    def into_send_mail(self):
        # 进入写信页面操作
        # 定位写信按钮，然后点击
        self.driver.find_elements_by_xpath('//span[@class="oz0"]')[1].click()
        time.sleep(2)

    def write_mail(self):
        # 写信操作
        addressee_element = self.driver.find_element_by_xpath('//input[@class="nui-editableAddr-ipt"]')
        subject_element = self.driver.find_element_by_xpath('//div[@class="bz0"]//input[@class="nui-ipt-input"]')
        iframe_element = self.driver.find_element_by_tag_name('iframe')
        send_element = self.driver.find_element_by_xpath('//span[text()="发送"]')

        # 写入内容
        addressee_element.send_keys('hello@hello.com')
        subject_element.send_keys('hello world')

        # 切换到富文本页面
        self.driver.switch_to.frame(iframe_element)
        body_element = self.driver.find_element_by_tag_name('body')
        body_element.send_keys('hello world hello world hello world hello world hello world')
        # 切换到主页面
        self.driver.switch_to.default_content()

        # 点击发送
        send_element.click()

    def quit(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.login()
    case.into_send_mail()
    case.write_mail()
    case.quit()
