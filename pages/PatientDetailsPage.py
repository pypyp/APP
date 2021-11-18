# -*- encoding: utf-8 -*-

# here put the import lib
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from pages.BasePage import BasePage


class PatientDetailsPage(BasePage):
    '''欢迎页面元素及方法
        该类继承自BasePage类

    Attributes:
        属性说明
    '''

    # 患者详情title
    patient_details_title = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/tvTitle')

    # 血糖检测
    blood_test_button = (By.XPATH, "//*[contains(@text,'血糖检测')]")

    # 基本信息
    basic_information_button = (By.XPATH, "//*[contains(@text,'基本信息')]")

    # 检测记录按钮
    test_record_button = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/rbRecord")

    # 检测记录
    test_record_text = (By.XPATH, "//*[contains(@text,'检测记录')]")

    # 血糖报告
    test_report_text = (By.XPATH, "//*[contains(@text,'血糖报告')]")

    # 趋势统计图
    statistical_chart_text = (By.XPATH, "//*[contains(@text,'趋势统计图')]")

    # 血糖报告
    test_report_exist = (By.ID, "com.vivachek.nova.tnineeightzeroone: id / hRecyclerview")

    # 检测记录
    test_record_exist = (By.ID, "com.vivachek.nova.tnineeightzeroone: id / recyclerview")

    # 折线图
    line_chart_text = (By.XPATH, "//*[contains(@text,'趋势统计图')]")

    # 返回按钮
    back_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/ivBack')

    # 保存按钮
    save_button = (By.XPATH, "//*[contains(@text,'保存血糖记录')]")

    # 保存
    save1_button = (By.XPATH, "//*[contains(@text,'保存')]")

    # 添加血糖
    add_button = (By.XPATH, "//*[contains(@text,'添加血糖')]")

    # 血糖值
    blood_num_input = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/etGlucose")

    # 检测详情
    test_details_text = (By.XPATH, "//*[contains(@text,'检测详情')]")

    # 备注
    remarks_input = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/etComment")

    # 确认
    right_button = (By.XPATH, "//*[contains(@text,'确认')]")

    # 取消
    left_button = (By.XPATH, "//*[contains(@text,'取消')]")

    # 删除
    del_button = (By.XPATH, "//*[contains(@text,'删除')]")

    # 检测时段
    time_type_button = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/tvTimeType")



    # 患者详情页面
    def is_patient_details_title_exist(self):
        return self.is_element_exist(*self.patient_details_title)

    #血糖检测确认
    def is_blood_test_button_exist(self):
        return self.find_element(*self.blood_test_button).get_attribute("checked")

    # 点击血糖检测
    def click_blood_test_button(self):
        return self.find_element(*self.blood_test_button).click()

    # 基本信息确认
    def is_basic_information_button_exist(self):
        return self.find_element(*self.basic_information_button).get_attribute("checked")

    # 点击基本信息
    def click_basic_information_button(self):
        return self.find_element(*self.basic_information_button).click()

    # 检测记录确认
    def is_test_record_button_exist(self):
        return self.find_element(*self.test_record_button).get_attribute("checked")

    # 点击检测记录
    def click_test_record_button(self):
        return self.find_element(*self.test_record_button).click()

    # 检测记录文字
    def is_test_record_text_exist(self):
        return self.is_element_exist(*self.test_record_text)

    # 点击检测记录文字
    def click_test_record_text(self):
        return self.find_element(*self.blood_test_button).click()

    # 血糖报告文字
    def is_test_report_text_exist(self):
        return self.is_element_exist(*self.test_report_text)

    # 点击血糖报告文字
    def click_test_report_text(self):
        return self.find_element(*self.test_report_text).click()

    # 趋势统计图文字
    def is_statistical_chart_text_exist(self):
        return self.is_element_exist(*self.statistical_chart_text)

    # 点击趋势统计图
    def click_statistical_chart_text(self):
        return self.find_element(*self.statistical_chart_text).click()

    # 返回按钮
    def click_back_button(self):
        self.find_element(*self.back_button).click()

    # 保存按钮
    def click_save_button(self):
        self.find_element(*self.save_button).click()

    # 保存按钮
    def click_save1_button(self):
        self.find_element(*self.save1_button).click()

    # 添加血糖按钮
    def click_add_button(self):
        self.find_element(*self.add_button).click()

    def is_add_text_exist(self):
        return self.is_element_exist(*self.add_button)

    # 血糖值
    def input_blood_num(self, name):
        self.find_element(*self.blood_num_input).send_keys(name)

    # 检测详情
    def is_test_details_text_exist(self):
        return self.is_element_exist(*self.test_details_text)

    # 备注
    def input_remarks(self, name):
        self.find_element(*self.remarks_input).send_keys(name)

    # 确认
    def click_right_button(self):
        self.find_element(*self.right_button).click()

    # 取消
    def click_left_button(self):
        self.find_element(*self.left_button).click()

    # 删除
    def click_del_button(self):
        self.find_element(*self.del_button).click()

    # 检测时段
    def click_time_type_button(self):
        self.find_element(*self.time_type_button).click()

if __name__ == '__main__':
    print(123)
