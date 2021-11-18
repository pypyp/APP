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
from pages.BasePage import BasePage
from pages.MainPage import MainPage
from pages.OperatorPage import OperatorPage
import logging
from appium import webdriver
import time


@pytest.mark.skip(reason='Test_Operator')
@allure.feature('测试操作人员功能')
class Test_Operator(object):
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
            cls.main_page = MainPage(cls.base_page)
            cls.operator_page = OperatorPage(cls.base_page)
        except Exception as e:
            print('错误类型是', e.__class__.__name__)
            print('错误明细是', e)
            BasePage.get_screen('screen_shot/')

    @classmethod
    def teardown_class(cls):
        print("断开连接")



    @allure.story("操作人员")
    @allure.severity("normal")
    @allure.description("进入操作人员")
    @allure.title("进入操作人员")
    def test_patient_1(self):
        time.sleep(3)
        self.main_page.click_personal_center_button()
        res = self.operator_page.is_operator_title_exist()
        assert res





    @allure.story("操作人员")
    @allure.severity("normal")
    @allure.description("返回首页")
    @allure.title("返回首页")
    def test_patient_2(self):
        time.sleep(3)
        self.operator_page.click_back_button()
        res = self.main_page.is_main_title_exist()
        assert res


if __name__ == '__main__':
    pytest.main(["test_operator.py"])
    print('123')