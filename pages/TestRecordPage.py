# -*- encoding: utf-8 -*-

# here put the import lib
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from pages.BasePage import BasePage


class TestRecord(BasePage):
    '''欢迎页面元素及方法
        该类继承自BasePage类

    Attributes:
        属性说明
    '''

    # 搜索按钮
    search_input = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/et')

    # 搜索确认
    search_title = (MobileBy.ACCESSIBILITY_ID, '检测记录搜索框')

    # 返回按钮
    back_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/ivBack')

    # 前一天
    forward_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/ivForward')

    # 后一天
    backward_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/ivBackward')

    # 时间
    time_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/tvDate')

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

    # 保存
    save1_button = (By.XPATH, "//*[contains(@text,'保存')]")


    # 确认搜索title
    def is_search_title_exist(self):
        return self.is_element_exist(*self.search_title)

    # 输入搜索框
    def input_search(self, content):
        self.find_element(*self.search_input).send_keys(content)

    # 点击搜索框
    def click_search(self):
        self.find_element(*self.search_input).click()

    # 后退
    def click_back_button(self):
        self.find_element(*self.back_button).click()

    # 前一天
    def click_forward_button(self):
        self.find_element(*self.forward_button).click()

    # 后一天
    def click_backward_button(self):
        self.find_element(*self.backward_button).click()

    # 时间值
    def is_time_exist(self):
        return self.find_element(*self.time_button).get_attribute("text")

    # 时间点击
    def click_time_button(self):
        self.find_element(*self.time_button).click()

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

    # 保存按钮
    def click_save1_button(self):
        self.find_element(*self.save1_button).click()

if __name__ == '__main__':
    print(123)



