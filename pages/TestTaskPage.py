# -*- encoding: utf-8 -*-

# here put the import lib
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from pages.BasePage import BasePage


class TestTask(BasePage):
    '''欢迎页面元素及方法
        该类继承自BasePage类

    Attributes:
        属性说明
    '''

    # 搜索按钮
    search_input = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/et')

    # 搜索确认
    search_title = (MobileBy.ACCESSIBILITY_ID, '检测任务搜索框')

    # 返回按钮
    back_button = (By.ID, 'com.vivachek.nova.tnineeightzeroone:id/ivBack')

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

    # 科室筛选
    department_button = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/tvDept")

    # 责任患者选框
    responsible_patient_button = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/tvPatient")

    # 时段选框
    time_interval_button = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/tvTimeType")

    # 关闭今日任务
    today_mission_button = (By.XPATH, "//*[contains(@text,'关闭今日任务')]")

    # 任务详情
    task_title = (By.ID, "com.vivachek.nova.tnineeightzeroone:id/tvTitle")



    # 确认搜索title
    def is_search_title_exist(self):
        return self.is_element_exist(*self.search_title)

    # 输入搜索框
    def input_search(self, content):
        self.find_element(*self.search_input).send_keys(content)

    # 点击搜索框
    def click_search(self):
        self.find_element(*self.search_input).click()

    def click_back_button(self):
        self.find_element(*self.back_button).click()

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

    # 科室选择
    def click_department_button(self):
        self.find_element(*self.department_button).click()

    # 责任患者
    def click_responsible_patient_button(self):
        self.find_element(*self.responsible_patient_button).click()

    # 时段筛选
    def click_time_interval_button(self):
        self.find_element(*self.time_interval_button).click()

    # 时段筛选值
    def get_time_interval_exist(self):
        return self.find_element(*self.time_interval_button).get_attribute("text")

    # 关闭今日任务
    def click_today_mission_button(self):
        self.find_element(*self.today_mission_button).click()

    # 任务详情标题
    def get_task_title_exist(self):
        return self.find_element(*self.task_title).get_attribute("text")



if __name__ == '__main__':
    print(123)
