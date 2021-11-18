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
from pages.TestRecordPage import TestRecord
import logging
from appium import webdriver
import time
from selenium.webdriver.common.by import By


@allure.feature('测试检测记录功能')
class Test_TestRecord(object):
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
            cls.test_record_page = TestRecord(cls.base_page)
        except Exception as e:
            print('错误类型是', e.__class__.__name__)
            print('错误明细是', e)
            BasePage.get_screen('screen_shot/')

    @classmethod
    def teardown_class(cls):
        print("断开连接")



    @allure.story("检测记录")
    @allure.severity("normal")
    @allure.description("进入检测记录")
    @allure.title("进入检测记录")
    def test_record_0(self):
        self.main_page.click_test_record_button()
        res = self.test_record_page.is_search_title_exist()
        assert res

    @allure.story("检测记录")
    @allure.severity("normal")
    @allure.description("时间切换")
    @allure.title("时间切换")
    def test_record_1(self):
        today = self.test_record_page.is_time_exist()
        self.test_record_page.click_time_button()
        time.sleep(1)
        self.driver.swipe(248, 671, 248, 710)
        time.sleep(1)
        self.test_record_page.click_right_button()
        lastday = self.test_record_page.is_time_exist()
        assert today > lastday

    @allure.story("检测记录")
    @allure.severity("normal")
    @allure.description("时间切换-后一天")
    @allure.title("时间切换-后一天")
    def test_record_2(self):
        self.driver.keyevent(3)
        self.main_page.click_test_record_button()
        self.test_record_page.click_backward_button()
        res = self.base_page.is_toast_exist('不能超过当前日期')
        assert res

    @allure.story("检测记录")
    @allure.severity("normal")
    @allure.description("时间切换-前一天")
    @allure.title("时间切换-前一天")
    def test_record_3(self):
        today = self.test_record_page.is_time_exist()
        self.test_record_page.click_forward_button()
        yesday = self.test_record_page.is_time_exist()
        self.test_record_page.click_backward_button()
        res = self.test_record_page.is_time_exist()
        assert today > yesday and today == res


    @allure.story("检测记录")
    @allure.severity("normal")
    @allure.description("检测记录-搜索")
    @allure.title("时间切换-搜索")
    def test_record_4(self):
        self.test_record_page.input_search('测试2021')
        self.test_record_page.click_search()
        self.driver.keyevent(66)
        res = self.base_page.is_element_exist(By.XPATH, "//*[@text='测试2021']")
        assert res


    @allure.story("检测记录")
    @allure.severity("normal")
    @allure.description("检测记录-检测详情")
    @allure.title("检测记录-检测详情")
    def test_record_5(self):
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'7.2')]").click()
        res = self.test_record_page.is_test_details_text_exist()
        assert res

    @allure.story("检测记录")
    @allure.severity("normal")
    @allure.description("检测记录-修改")
    @allure.title("检测记录-修改")
    def test_record_6(self):
        self.test_record_page.click_time_type_button()
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'凌晨')]").click()
        self.test_record_page.click_right_button()
        self.test_record_page.input_remarks("0010")
        self.test_record_page.click_save1_button()
        self.test_record_page.click_right_button()
        res = self.base_page.is_toast_exist('修改成功')
        assert res

    @allure.story("检测记录")
    @allure.severity("normal")
    @allure.description("检测记录-确认")
    @allure.title("检测记录-确认")
    def test_record_7(self):
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'7.2')]").click()
        res = self.test_record_page.is_test_details_text_exist()
        assert res

    @allure.story("检测记录")
    @allure.severity("normal")
    @allure.description("检测记录-删除")
    @allure.title("检测记录-删除")
    def test_record_8(self):
        self.test_record_page.click_del_button()
        self.test_record_page.click_right_button()
        res = self.base_page.is_toast_exist('删除成功')
        assert res

    @allure.story("检测记录")
    @allure.severity("normal")
    @allure.description("返回首页")
    @allure.title("返回首页")
    def test_record_20(self):
        self.test_record_page.click_back_button()
        res = self.main_page.is_main_title_exist()
        assert res


if __name__ == '__main__':
    pytest.main(["test_testrecord.py"])
    print('检测记录 测试完成')