# -*- encoding: utf-8 -*-

# here put the import lib
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pytest
import allure
from case.driver import init_driver
from util.LoggingUtil import LoggingUtil
from pages.LoginPage import LoginPage
from pages.BasePage import BasePage
from pages.MainPage import MainPage
import logging
from appium import webdriver
import time



@allure.feature('测试登录功能')
class Test_login(object):
    '''类注释
    详细描述

    Attributes:
        属性说明
    '''

    @classmethod
    def setup_class(cls):
        # cls.logging_util = LoggingUtil()
        # cls.logging_util.setup_logging()
        cls.logger = logging.getLogger()

        cls.logger.info('启动app')
        try:
            cls.driver = init_driver()
            time.sleep(5)
            cls.base_page = BasePage(cls.driver)
            cls.login_page = LoginPage(cls.base_page)
            cls.main_page = MainPage(cls.base_page)
        except Exception as e:
            print('错误类型是', e.__class__.__name__)
            print('错误明细是', e)

            BasePage.get_screen('screen_shot/')

    @classmethod
    def teardown_class(cls):
        print("断开连接")

    # @allure.story('登录-用户不存在')
    # def test_login_1(self):
    #     self.logger.info('开始测试test_login_1==================================')
    #     self.login_page.input_username('15628811988')
    #     self.login_page.input_passwd('12345678')
    #     self.login_page.click_signin_button()
    #     res = self.base_page.is_toast_exist('用户不存在')
    #     assert res
    #     self.logger.info('测试结束=====================================')

    @allure.story("登录")
    @allure.severity("normal")
    @allure.description("登录-账号或密码错误")
    @allure.title("账号密码错误")
    def test_login_2(self):
        time.sleep(2)
        self.login_page.input_username('8131')
        self.login_page.input_passwd('123456789')
        self.login_page.click_signin_button()
        res = self.base_page.is_toast_exist('账号或者密码错误')
        assert res



    @allure.story("登录")
    @allure.severity("normal")
    @allure.description("登录-未输入密码")
    @allure.title("未输入密码")
    def test_login_3(self):
        time.sleep(1)
        self.login_page.input_username('8131')
        self.login_page.input_passwd('')
        self.login_page.click_signin_button()
        res = self.base_page.is_toast_exist('密码不能为空')
        assert res



    @allure.story("登录")
    @allure.severity("normal")
    @allure.description("登录-未输入账号")
    @allure.title("未输入账号")
    def test_login_5(self):
        time.sleep(1)
        self.login_page.input_username('')
        self.login_page.input_passwd('12345678')
        self.login_page.click_signin_button()
        res = self.base_page.is_toast_exist('账号不能为空')
        assert res



    @allure.story("登录")
    @allure.severity("normal")
    @allure.description("登录-正常")
    @allure.title("成功登录")
    def test_right(self):
        time.sleep(1)
        self.login_page.input_username('18500000001')
        self.login_page.input_passwd('000001')
        self.login_page.click_signin_button()
        res = self.main_page.is_main_title_exist()
        assert res
        self.logger.info('测试完成')



if __name__ == '__main__':
    pytest.main(["test_login.py"])
    print('登录 测试完成')