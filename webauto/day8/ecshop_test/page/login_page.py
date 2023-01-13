from common.base import Base, By, get_driver


class LoginPage(Base):
    login_url = "https://ecshop.test2.shopex123.com/user.php"

    def username_input(self, username):
        self.send_keys((By.NAME, 'username'), username)

    def password_input(self, password):
        self.send_keys((By.NAME, 'password'), password)

    def remember_checkbox(self):
        self.click((By.ID, 'remember'))

    def submit_button(self):
        self.click((By.NAME, 'submit'))


if __name__ == '__main__':
    driver = get_driver()
    login_page = LoginPage(driver)
    login_page.get(login_page.login_url)

    # 测试方法
    login_page.username_input('fine1')
    login_page.password_input('123456')
    login_page.remember_checkbox()
    login_page.submit_button()
