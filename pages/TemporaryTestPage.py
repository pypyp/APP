# -*- encoding: utf-8 -*-

# here put the import lib
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class TemporaryTest(BasePage):
    '''欢迎页面元素及方法
        该类继承自BasePage类

    Attributes:
        属性说明
    '''

    # 血糖检测title
    blood_glucose_detection_title = (By.XPATH, "//*[contains(@text,'血糖检测')]")

    # 返回按钮
    back_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/ivBack')

    # 保存
    save1_button = (By.XPATH, "//*[contains(@text,'保存')]")

    # 临时检测记录
    test_record_button = (By.XPATH, "//*[contains(@text,'临时检测记录')]")

    test_time_input = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/tvMeasureTime")

    test_details_title = (By.XPATH, "//*[contains(@text,'检测详情')]")

    # 检测时段
    time_type_button = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/tvTimeType")

    # 确认
    right_button = (By.XPATH, "//*[contains(@text,'确认')]")

    # 取消
    left_button = (By.XPATH, "//*[contains(@text,'取消')]")

    # 删除
    del_button = (By.XPATH, "//*[contains(@text,'删除')]")

    # 备注
    remarks_input = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/etComment")

    # 被测患者
    patient_button = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/tvPatientHint")

    # 搜索框
    search_input = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/et")

    # 备注
    def input_remarks(self, name):
        self.find_element(*self.remarks_input).send_keys(name)

    def is_blood_glucose_detection_title_exist(self):
        return self.is_element_exist(*self.blood_glucose_detection_title)

    def click_back_button(self):
        self.find_element(*self.back_button).click()

    # 保存按钮
    def click_save1_button(self):
        self.find_element(*self.save1_button).click()

    # 临时检测记录按钮
    def click_test_record_button(self):
        self.find_element(*self.test_record_button).click()

    # 临时检测记录确认
    def is_test_record_title_exist(self):
        return self.is_element_exist(*self.test_record_button)

    # 检测时间值
    def is_test_time_exist(self):
        return self.find_element(*self.test_time_input).get_attribute("text")

    # 检测详情
    def is_test_details_title_exist(self):
        return self.is_element_exist(*self.test_details_title)

    # 检测时段
    def click_time_type_button(self):
        self.find_element(*self.time_type_button).click()



    # 确认
    def click_right_button(self):
        self.find_element(*self.right_button).click()

    # 取消
    def click_left_button(self):
        self.find_element(*self.left_button).click()

    # 删除
    def click_del_button(self):
        self.find_element(*self.del_button).click()

    # 被测患者
    def click_patient_button(self):
        self.find_element(*self.patient_button).click()

    # 输入搜索框
    def input_search(self, content):
        self.find_element(*self.search_input).send_keys(content)

    # 点击搜索框
    def click_search(self):
        self.find_element(*self.search_input).click()

if __name__ == '__main__':
    print(123)



