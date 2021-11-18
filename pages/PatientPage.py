# -*- encoding: utf-8 -*-

# here put the import lib
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from pages.BasePage import BasePage


class PatientPage(BasePage):
    '''欢迎页面元素及方法
        该类继承自BasePage类

    Attributes:
        属性说明
    '''
    # 搜索框
    search_input = (MobileBy.ACCESSIBILITY_ID, '院内患者搜索框')

    # 患者登记title
    patient_registration_title = (By.XPATH, "//*[contains(@text,'患者登记')]")

    # 患者登记按钮
    patient_registration_button = (MobileBy.ACCESSIBILITY_ID, 'icon添加患者')


    # 返回按钮
    back_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/ivBack')

    # 添加患者页面
    # 姓名输入框
    name_input = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/etName')

    # 性别选择按钮
    gender_button = (MobileBy.ACCESSIBILITY_ID, 'sw性别')

    # 出生日期选择框
    birthday_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/flBirthday')

    # 确认
    right_button = (By.XPATH, "//*[contains(@text,'确认')]")

    # 取消
    left_button = (By.XPATH, "//*[contains(@text,'取消')]")

    # 科室选择框
    department_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/tvDept')

    # 住院号输入框
    hospital_number_input = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/etHospitalNum')

    # 床号输入框
    bed_number_input = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/etBedNo')

    # 登记按钮
    register_button = (By.CLASS_NAME, 'android.widget.Button')

    # 确认搜索框
    def is_search_input_exist(self):
        return self.is_element_exist(*self.search_input)

    # 输入搜索框
    def input_search(self, content):
        self.find_element(*self.search_input).send_keys(content)

    # 点击搜索框
    def click_search(self):
        self.find_element(*self.search_input).click()

    # 点击登记患者按钮
    def click_patient_registration_button(self):
        self.find_element(*self.patient_registration_button).click()

    # 确认患者登记
    def is_patient_registration_title_exist(self):
        return self.is_element_exist(*self.patient_registration_title)

    # 输入姓名
    def input_name(self, name):
        self.find_element(*self.name_input).send_keys(name)

    # 性别按钮
    def click_gender_button(self):
        self.find_element(*self.gender_button).click()

    # 出生日期
    def click_birthday_button(self):
        self.find_element(*self.birthday_button).click()

    # 科室
    def click_department_button(self):
        self.find_element(*self.department_button).click()

    # 确认
    def click_right_button(self):
        self.find_element(*self.right_button).click()

    # 取消
    def click_left_button(self):
        self.find_element(*self.left_button).click()

    # 住院号
    def input_hospital_number(self, hostnum):
        self.find_element(*self.hospital_number_input).send_keys(hostnum)

    # 床号
    def input_bed_number(self, bednum):
        self.find_element(*self.bed_number_input).send_keys(bednum)

    # 登记按钮
    def click_register_button(self):
        self.find_element(*self.register_button).click()

    # 返回按钮
    def click_back_button(self):
        self.find_element(*self.back_button).click()


if __name__ == '__main__':
    print(123)
