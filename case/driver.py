from appium import webdriver
import logging

def init_driver():
    desired_caps = {
        'platformName': 'Android',
        # 'deviceName': '127.0.0.1:5554',  # 手机设备名称，通过adb devices查看
        'deviceName': '359B0000360',  # 手机设备名称，通过adb devices查看
        'platformVersion': '7.0',  # android系统的版本号
        'appPackage': 'com.vivachek.nova.tnineeightzeroone',  # apk包名
        # apk的launcherActivity
        'appActivity': 'com.vivachek.t9801.MainActivity',
        'noReset': 'True',
        'noSign': 'True',
        'fullReset': 'false',
        'automationName': 'Uiautomator2'

    }
    # 手机驱动对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver

    logging.info("driver.quit:清理driver进程！！！")
    driver.quit()

    # 172.21.21.116