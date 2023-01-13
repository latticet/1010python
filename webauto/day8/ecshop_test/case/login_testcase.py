import unittest
from page.login_page import LoginPage, get_driver
from page.index_page import IndexPage
import time
import ddt
from common.dataoperation import DataOperation

data = DataOperation('user_info.csv')
userinfo_list = data.read_dict()
"""
[
{'title': 'yes', 'username': 'fine1', 'password': 123456}, 
{'title': 'username_error', 'username': 'fine0', 'password': 123456}, 
{'title': 'password_error', 'username': 'fine1', 'password': 111111}
]
"""


@ddt.ddt
class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 打开浏览器， 请求目标网址
        driver = get_driver()
        cls.login_page = LoginPage(driver)

        # index_page
        cls.index_page = IndexPage(driver)

    @ddt.data(*userinfo_list)
    def test_login(self, userinfo):
        self.login_page.get(self.login_page.login_url)
        time.sleep(1)
        # 登录操作
        # 输入用户名
        expect_username = userinfo['username']
        password = userinfo['password']
        self.login_page.username_input(expect_username)
        # 输入密  码
        self.login_page.password_input(password)
        # 点击保存用户信息
        self.login_page.remember_checkbox()
        # 点击登录
        self.login_page.submit_button()

        # 断言
        actual_username = self.index_page.font_text()
        if userinfo['title'] == 'yes':
            self.assertEqual(expect_username, actual_username, msg=userinfo['title'])
        else:
            self.assertNotEqual(expect_username, actual_username, msg=userinfo['title'])

    def tearDown(self) -> None:
        self.index_page.a_logout()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.login_page.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
