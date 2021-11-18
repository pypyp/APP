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
from pages.TestTaskPage import TestTask
import logging
from appium import webdriver
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


@allure.feature('检测任务功能')
class Test_TestTask(object):
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
            cls.test_task_page = TestTask(cls.base_page)
        except Exception as e:
            print('错误类型是', e.__class__.__name__)
            print('错误明细是', e)
            BasePage.get_screen('screen_shot/')

    @classmethod
    def teardown_class(cls):
        print("断开连接")



    @allure.story("检测任务")
    @allure.severity("normal")
    @allure.description("进入任务列表")
    @allure.title("进入任务列表")
    def test_testtask_01(self):
        self.main_page.click_test_task_button()
        res = self.test_task_page.is_search_title_exist()
        assert res

    @allure.story("检测任务")
    @allure.severity("normal")
    @allure.description("任务列表筛选")
    @allure.title("任务列表筛选")
    def test_testtask_02(self):
        self.test_task_page.click_department_button()
        self.test_task_page.click_right_button()
        self.test_task_page.click_responsible_patient_button()
        self.test_task_page.click_right_button()
        self.test_task_page.click_time_type_button()
        time.sleep(1)
        # TouchAction(self.driver).press(x=238, y=751).wait(300).move_to(x=238, y=708).release().perform()
        self.driver.swipe(238, 751, 238, 708)
        time.sleep(1)
        self.test_task_page.click_right_button()
        self.time_interval = self.test_task_page.get_time_interval_exist()
        res = True
        assert res

    @allure.story("检测任务")
    @allure.severity("normal")
    @allure.description("任务列表-搜索")
    @allure.title("任务列表-搜索")
    def test_testtask_03(self):
        self.test_task_page.input_search('测试20')
        self.test_task_page.click_search()
        self.driver.keyevent(66)
        res = self.base_page.is_element_exist(By.XPATH, "//*[@text='测试2021']")
        assert res


    @allure.story("检测任务")
    @allure.severity("normal")
    @allure.description("检测任务-详情")
    @allure.title("检测任务-详情")
    def test_record_04(self):
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'测试2021')]").click()
        task = self.test_task_page.get_task_title_exist()
        assert task == "测试2021"

    @allure.story("检测任务")
    @allure.severity("normal")
    @allure.description("检测任务-血糖检测")
    @allure.title("检测任务-血糖检测")
    def test_record_05(self):
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B01200110126600051100001100020701087D")
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000522000011000203010C7D")
        time.sleep(1)
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000533000011000D0F010F7D")
        time.sleep(5)
        os.system("adb shell am broadcast -a com.vivachek.simulateSerialPort --es data 7B012001101266000544011E110608040B7D")
        self.base_page.swipe_to_up()
        self.test_task_page.click_save1_button()
        res = self.base_page.is_toast_exist('添加成功')
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'取消')]").click()
        assert res


    @allure.story("检测任务")
    @allure.severity("normal")
    @allure.description("检测任务-扫码")
    @allure.title("检测任务-扫码")
    def test_record_06(self):
        os.system("adb shell am broadcast -a android.intent.action.ACTION_OPEN_SCAN")
        os.system("adb shell am broadcast -a COM.CUSTOM.SCAN.RESULT --ez status true --es code 0001")
        res = self.base_page.is_element_exist(By.XPATH, "//*[@text='测试001']")
        assert res

    @allure.story("检测任务")
    @allure.severity("normal")
    @allure.description("检测任务-详情")
    @allure.title("检测任务-详情")
    def test_record_07(self):
        self.base_page.find_element(By.XPATH, "//*[contains(@text,'测试001')]").click()
        task = self.test_task_page.get_task_title_exist()
        assert task == "测试001"

    @allure.story("检测任务")
    @allure.severity("normal")
    @allure.description("检测任务-关闭今日任务")
    @allure.title("检测任务-关闭今日任务")
    def test_record_08(self):
        self.test_task_page.click_today_mission_button()
        self.test_task_page.click_right_button()
        res = self.base_page.is_toast_exist('停止任务成功')
        assert res


    @allure.story("检测任务")
    @allure.severity("normal")
    @allure.description("返回首页")
    @allure.title("返回首页")
    def test_testtask_20(self):
        self.test_task_page.click_back_button()
        res = self.main_page.is_main_title_exist()
        assert res


if __name__ == '__main__':
    pytest.main(["test_testtask.py"])
    print('检测任务 测试完成')