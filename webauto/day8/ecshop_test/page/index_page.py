# //font[@id="ECS_MEMBERZONE"]/font/font
from common.base import Base, By, get_driver
from page.login_page import LoginPage


class IndexPage(Base):
    index_url = 'https://ecshop.test2.shopex123.com/index.php'

    def font_text(self):
        return self.text((By.XPATH, '//font[@id="ECS_MEMBERZONE"]/font/font'))


if __name__ == '__main__':
    # 打开浏览器，请求目标网址
    driver = get_driver()

    # 请求登录页面
    login_page = LoginPage(driver)
    login_page.get(login_page.login_url)
    # 登录操作
    login_page.username_input('fine1')
    login_page.password_input('123456')
    login_page.remember_checkbox()
    login_page.submit_button()

    index_page = IndexPage(driver)
    print(index_page.font_text())
