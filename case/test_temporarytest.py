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
from pages.TemporaryTestPage import TemporaryTest
import logging
from appium import webdriver
import time
from selenium.webdriver.common.by import By



@allure.feature('测试临时检测功能')
class Test_TemporaryTest(object):
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
            cls.temporary_test_page = TemporaryTest(cls.base_page)
        except Exception as e:
            print('错误类型是', e.__class__.__name__)
            print('错误明细是', e)
            BasePage.get_screen('screen_shot/')

    @classmethod
    def teardown_class(cls):
        print("断开连接")

    @allure.story("临时检测")
    @allure.severity("normal")
    @allure.description("进入血糖检测")
    @allure.title("进入血糖检测")
    def test_temporary_0(self):
        self.main_page.click_temporary_test_button()
        res = self.temporary_test_page.is_blood_glucose_detection_title_exist()
        assert res


    @allure.story("临时检测")
    @allure.severity("normal")
    @allure.description("血糖检测")
    @allure.title("血糖检测")
    def test_temporary_1(self):
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B01200110126600051100001100020701087D")
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000522000011000203010C7D")
        time.sleep(1)
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000533000011000D0F010F7D")
        time.sleep(5)
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000544011E110608040B7D")
        self.test_time_1 = self.temporary_test_page.is_test_time_exist()
        self.temporary_test_page.click_save1_button()
        res = self.base_page.is_toast_exist('添加成功')
        assert res




    @allure.story("临时检测")
    @allure.severity("normal")
    @allure.description("选择")
    @allure.title("进入血糖检测")
    def test_temporary_2(self):
        self.temporary_test_page.click_test_record_button()
        res = self.temporary_test_page.is_test_record_title_exist()
        assert res

    @allure.story("临时检测")
    @allure.severity("normal")
    @allure.description("选择血糖")
    @allure.title("进入血糖检测")
    def test_temporary_3(self, ):
        # psgs = self.test_time_1
        # print(psgs)
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'7.2')]").click()
        res = self.temporary_test_page.is_test_details_title_exist()
        assert res



    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("检测详情-修改")
    @allure.title("检测详情-修改")
    def test_temporary_4(self):
        self.temporary_test_page.click_time_type_button()
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'晚餐前')]").click()
        self.temporary_test_page.click_right_button()
        self.temporary_test_page.input_remarks("备注内容")
        self.temporary_test_page.click_save1_button()
        res = self.base_page.is_toast_exist('修改成功')
        assert res

    @allure.story("临时检测")
    @allure.severity("normal")
    @allure.description("检测详情-删除")
    @allure.title("删除血糖")
    def test_temporary_5(self):
        # psge = "//*[contains(@text,'{}')]".format(self.test_time)
        # print(psge)
        # self.base_page.find_element(By.XPATH, psge).click()
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'7.2')]").click()
        self.temporary_test_page.click_del_button()
        self.temporary_test_page.click_right_button()
        res = self.base_page.is_toast_exist('删除成功')
        assert res

    @allure.story("临时检测")
    @allure.severity("normal")
    @allure.description("血糖检测-被测患者")
    @allure.title("血糖检测选择患者")
    def test_temporary_6(self):
        self.temporary_test_page.click_back_button()
        # self.temporary_test_page.click_right_button()
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B01200110126600051100001100020701087D")
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000522000011000203010C7D")
        time.sleep(1)
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000533000011000D0F010F7D")
        time.sleep(5)
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000544003F1102010D0B7D")
        self.time_2 = self.temporary_test_page.is_test_time_exist()
        self.temporary_test_page.click_save1_button()
        res = self.base_page.is_toast_exist('添加成功')
        self.temporary_test_page.click_test_record_button()
        rest = self.temporary_test_page.is_test_record_title_exist()
        assert res and rest

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("检测详情-修改")
    @allure.title("检测详情-修改")
    def test_temporary_7(self):
        # psge = "//*[contains(@text,'{}')]".format(self.time_2)
        # print(psge)
        # self.base_page.find_element(By.XPATH, psge).click()
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'3.5')]").click()
        self.temporary_test_page.click_patient_button()
        self.temporary_test_page.input_search('测试')
        self.temporary_test_page.click_search()
        self.driver.keyevent(66)
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'测试001')]").click()
        self.temporary_test_page.click_save1_button()
        res = self.base_page.is_toast_exist('修改成功')
        assert res

    @allure.story("临时检测")
    @allure.severity("normal")
    @allure.description("血糖检测-被测患者")
    @allure.title("血糖检测选择患者")
    def test_temporary_8(self):
        self.temporary_test_page.click_back_button()
        # self.driver.keyevent(3)
        # self.main_page.click_temporary_test_button()
        self.temporary_test_page.click_time_type_button()
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'晚餐后')]").click()
        self.temporary_test_page.click_right_button()
        self.temporary_test_page.click_patient_button()
        self.temporary_test_page.input_search('测试')
        self.temporary_test_page.click_search()
        self.driver.keyevent(66)
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'测试002')]").click()
        rest = self.base_page.is_element_exist(By.XPATH, "//*[contains(@text,'测试002')]")
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B01200110126600051100001100020701087D")
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000522000011000203010C7D")
        time.sleep(1)
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000533000011000D0F010F7D")
        time.sleep(5)
        os.system(
            "adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000544011E110608040B7D")
        self.temporary_test_page.click_save1_button()
        res = self.base_page.is_toast_exist('添加成功')
        assert res and rest

    @allure.story("临时检测")
    @allure.severity("normal")
    @allure.description("返回首页")
    @allure.title("返回首页")
    def test_temporary_20(self):
        # self.temporary_test_page.click_back_button()
        # self.temporary_test_page.click_back_button()
        self.driver.keyevent(3)
        res = self.main_page.is_main_title_exist()
        assert res


if __name__ == '__main__':
    pytest.main(["test_temporarytest.py"])
    print('临时检测 测试完成')