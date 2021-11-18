# -*- encoding: utf-8 -*-

# here put the import lib
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import traceback
import pytest
import allure
from case.driver import init_driver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from util.LoggingUtil import LoggingUtil
from pages.BasePage import BasePage
from pages.MainPage import MainPage
from pages.PatientPage import PatientPage
from pages.PatientDetailsPage import PatientDetailsPage
import logging
from selenium.webdriver.common.by import By
from appium import webdriver
import time




@allure.feature('测试患者管理功能')
class Test_Patient(object):
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
            time.sleep(3)
            cls.base_page = BasePage(cls.driver)
            cls.main_page = MainPage(cls.base_page)
            cls.patient_page = PatientPage(cls.base_page)

            cls.patient_details_page = PatientDetailsPage(cls.base_page)
        except Exception as e:
            print('错误类型是', e.__class__.__name__)
            print('错误明细是', e)
            traceback.print_exc()
            BasePage.get_screen('screen_shot/')


    @classmethod
    def teardown_class(cls):
        print("断开连接")



    @allure.story("患者管理")
    @allure.severity("normal")
    @allure.description("进入患者管理")
    @allure.title("进入患者管理")
    def test_patient_1(self):
        time.sleep(3)
        self.main_page.click_patient_management_button()
        res = self.patient_page.is_search_input_exist()
        assert res

    @allure.story("患者登记")
    @allure.severity("normal")
    @allure.description("进入患者登记")
    @allure.title("进入患者登记")
    def test_patient_01(self):
        self.patient_page.click_patient_registration_button()
        res = self.patient_page.is_patient_registration_title_exist()
        assert res

    @allure.story("患者管理")
    @allure.severity("normal")
    @allure.description("患者登记")
    @allure.title("患者登记")
    def test_patient_02(self):
        self.patient_page.input_name('测试2001')
        self.patient_page.click_birthday_button()
        time.sleep(1)
        self.patient_page.click_right_button()
        time.sleep(1)
        self.patient_page.click_department_button()
        time.sleep(1)
        self.patient_page.click_right_button()
        time.sleep(1)
        self.patient_page.input_hospital_number('000123453')
        self.patient_page.click_register_button()
        res = self.base_page.is_toast_exist('添加成功')
        assert res

    @allure.story("患者管理")
    @allure.severity("normal")
    @allure.description("搜索")
    @allure.title("搜索")
    def test_patient_03(self):
        self.patient_page.input_search('测试')
        self.patient_page.click_search()
        self.driver.keyevent(66)
        time.sleep(2)
        res = self.base_page.is_element_exist(By.XPATH, "//*[@text='测试2021']")
        # for title in titles:
        #     print(title.text)
        #     res = self.base_page.is_element_exist(title)
        assert res

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-扫码")
    @allure.title("患者详情-扫码")
    def test_patient_04(self):
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'取消')]").click()
        os.system("adb shell am broadcast -a android.intent.action.ACTION_OPEN_SCAN")
        os.system("adb shell am broadcast -a COM.CUSTOM.SCAN.RESULT --ez status true --es code 000012345")
        res = self.patient_details_page.is_patient_details_title_exist()
        rest = self.patient_details_page.is_blood_test_button_exist()
        assert (res and rest)

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-血糖检测")
    @allure.title("患者详情-血糖检测")
    def test_patient_05(self):
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B01200110126600051100001100020701087D")
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000522000011000203010C7D")
        time.sleep(1)
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000533000011000D0F010F7D")
        time.sleep(5)
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000544011E110608040B7D")
        self.patient_details_page.click_save_button()
        res = self.base_page.is_toast_exist('添加成功')
        assert res

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-添加血糖")
    @allure.title("患者详情-添加血糖")
    def test_patient_06(self):
        self.patient_details_page.click_add_button()
        res = self.patient_details_page.is_add_text_exist()
        assert res

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-添加血糖")
    @allure.title("患者详情-添加血糖")
    def test_patient_07(self):
        self.patient_details_page.input_blood_num("5.6")
        self.patient_details_page.click_save_button()
        res = self.base_page.is_toast_exist('添加成功')
        assert res

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("添加血糖")
    @allure.title("添加血糖")
    def test_patient_08(self):
        self.patient_details_page.click_add_button()
        self.patient_details_page.input_blood_num("7.2")
        self.patient_details_page.click_time_type_button()
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'早餐后')]").click()
        self.patient_details_page.click_right_button()
        self.patient_details_page.click_save_button()
        res = self.base_page.is_toast_exist('添加成功')
        assert res

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-血糖检测")
    @allure.title("患者详情-血糖检测")
    def test_patient_09(self):
        self.patient_details_page.click_time_type_button()
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'午餐后')]").click()
        self.patient_details_page.click_right_button()
        self.patient_details_page.input_remarks("1234")
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B01200110126600051100001100020701087D")
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000522000011000203010C7D")
        time.sleep(1)
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000533000011000D0F010F7D")
        time.sleep(5)
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000544003F1102010D0B7D")
        self.patient_details_page.click_save_button()
        res = self.base_page.is_toast_exist('添加成功')
        assert res



    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-基本信息")
    @allure.title("患者详情-基本信息")
    def test_patient_10(self):
        self.patient_details_page.click_basic_information_button()
        res = self.patient_details_page.is_basic_information_button_exist()
        assert res


    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-检测记录")
    @allure.title("患者详情-检测记录")
    def test_patient_11(self):
        self.patient_details_page.click_test_record_button()
        res = self.patient_details_page.is_test_record_button_exist()
        rst = self.patient_details_page.is_test_record_text_exist()
        assert res and rst

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-检测记录详情")
    @allure.title("患者详情-检测记录详情")
    def test_patient_12(self):
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'5.6')]").click()
        res = self.patient_details_page.is_test_details_text_exist()
        assert res

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-修改")
    @allure.title("患者详情-修改")
    def test_patient_13(self):
        self.patient_details_page.click_time_type_button()
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'凌晨')]").click()
        self.patient_details_page.click_right_button()
        self.patient_details_page.input_remarks("备注内容")
        self.patient_details_page.click_save1_button()
        self.patient_details_page.click_right_button()
        res = self.base_page.is_toast_exist('修改成功')
        assert res

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-确认")
    @allure.title("患者详情-确认")
    def test_patient_14(self):
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'5.6')]").click()
        res = self.patient_details_page.is_test_details_text_exist()
        assert res

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-删除")
    @allure.title("患者详情-删除")
    def test_patient_15(self):
        self.patient_details_page.click_del_button()
        self.patient_details_page.click_right_button()
        res = self.base_page.is_toast_exist('删除成功')
        assert res

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-血糖报告")
    @allure.title("患者详情-血糖报告")
    def test_patient_16(self):
        self.patient_details_page.click_test_record_button()
        self.patient_details_page.click_test_report_text()
        res = self.patient_details_page.is_test_report_text_exist()
        rst = self.patient_details_page.is_test_record_button_exist()
        assert res and rst

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("患者详情-趋势统计图")
    @allure.title("患者详情-趋势统计图")
    def test_patient_17(self):
        self.patient_details_page.click_test_record_button()
        self.patient_details_page.click_statistical_chart_text()
        res = self.patient_details_page.is_statistical_chart_text_exist()
        rst = self.patient_details_page.is_test_record_button_exist()
        assert res and rst

    @allure.story("患者详情")
    @allure.severity("normal")
    @allure.description("返回")
    @allure.title("返回")
    def test_patient_18(self):
        self.patient_details_page.click_back_button()
        res = self.patient_page.is_search_input_exist()
        assert res

    @allure.story("患者管理")
    @allure.severity("normal")
    @allure.description("返回首页")
    @allure.title("返回首页")
    def test_patient_20(self):
        self.patient_page.click_back_button()
        res = self.main_page.is_main_title_exist()
        assert res


if __name__ == '__main__':
    pytest.main(["test_patient.py"])
    print('患者管理 测试完成')