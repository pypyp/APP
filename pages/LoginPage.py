# -*- encoding: utf-8 -*-


# here put the import lib
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    '''登录页面元素及方法
        该类继承自BasePage类

    Attributes:
        属性说明
    '''
    # 用户名输入框
    username_input = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/etHisId')
    # 密码输入框
    passwd_input = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/etPassword')
    # 登录按钮
    signin_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/btnLogin')
    # 记住密码勾选框
    rememberPass_cb = (By.ID, 'com.aiosign.dzonesign:id/cbRememberPass')
    # 注册连接
    registerUser_tv = (By.ID, 'com.aiosign.dzonesign:id/tvRegisterUser')
    # 显示密码按钮
    showPass_cb = (By.ID, 'com.aiosign.dzonesign:id/cbShowPass')

    def input_username(self, username):
        self.find_element(*self.username_input).send_keys(username)

    def input_passwd(self, passwd):
        self.find_element(*self.passwd_input).send_keys(passwd)

    def click_signin_button(self):
        self.find_element(*self.signin_button).click()

    def click_rememberPass_cb(self):
        self.find_element(*self.rememberPass_cb).click()

    def click_registerUser_tv(self):
        self.find_element(*self.registerUser_tv).click()

    def click_showPass_cb(self):
        self.find_element(*self.showPass_cb).click()

if __name__ == '__main__':
    print(123)
