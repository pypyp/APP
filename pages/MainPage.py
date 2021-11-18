# -*- encoding: utf-8 -*-


# here put the import lib
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class MainPage(BasePage):
    '''主页面元素及方法
    详细描述

    Attributes:
        属性说明
    '''

    #首页标题
    main_title = (By.XPATH, "//*[contains(@text,'Vivachek Pro')]")

    # 操作人员按钮
    personal_center_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/civAvatar')

    # 患者管理按钮
    patient_management_button = (By.XPATH, "//*[contains(@text,'患者管理')]")

    # 检测记录按钮
    test_record_button = (By.XPATH, "//*[contains(@text,'检测记录')]")

    # 检测任务按钮
    test_task_button = (By.XPATH, "//*[contains(@text,'检测任务')]")

    # 临时检测按钮
    temporary_test_button = (By.XPATH, "//*[contains(@text,'临时检测')]")

    # 室间质评按钮
    external_quality_button = (By.XPATH, "//*[contains(@text,'室间质评')]")

    # 设备质控按钮
    quality_control_button = (By.XPATH, "//*[contains(@text,'设备质控')]")

    # 功能设置按钮
    function_settings_button = (By.XPATH, "//*[contains(@text,'功能设置')]")

    # 退出按钮


    def click_personal_center_button(self):
        self.find_element(*self.personal_center_button).click()

    def click_patient_management_button(self):
        self.find_element(*self.patient_management_button).click()

    def click_test_record_button(self):
        self.find_element(*self.test_record_button).click()

    def click_test_task_button(self):
        self.find_element(*self.test_task_button).click()

    def click_temporary_test_button(self):
        self.find_element(*self.temporary_test_button).click()

    def click_external_quality_button(self):
        self.find_element(*self.external_quality_button).click()

    def click_quality_control_button(self):
        self.find_element(*self.quality_control_button).click()

    def click_function_settings_button(self):
        self.find_element(*self.function_settings_button).click()

    def is_main_title_exist(self):
        return self.is_element_exist(*self.main_title)


if __name__ == '__main__':
    print(123)
