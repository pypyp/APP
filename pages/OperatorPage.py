# -*- encoding: utf-8 -*-

# here put the import lib
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy

class OperatorPage(BasePage):
    '''欢迎页面元素及方法
        该类继承自BasePage类

    Attributes:
        属性说明
    '''
    # 操作人员title
    operator_title = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/tvTitle")

    # 操作人员登记按钮
    patient_registration_button = (MobileBy.ACCESSIBILITY_ID, 'icon添加医护人员')

    # 返回按钮
    back_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/ivBack')




    def is_operator_title_exist(self):
        return self.is_element_exist(*self.operator_title)

    def click_back_button(self):
        self.find_element(*self.back_button).click()


    def click_patient_registration_button(self):
        self.find_element(*self.patient_registration_button).click()

if __name__ == '__main__':
    print(123)
