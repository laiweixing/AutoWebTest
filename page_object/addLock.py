#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
添加车锁功能封装

"""

from common.desired import desired_chrome
from common.common_fun import Common
from selenium.webdriver.common.by import By
from page_object.loginView import LoginView
from time import sleep

class AddLock(Common):

    bicycle_management_Btn = (By.LINK_TEXT, '单车管理')
    car_lock_management_Btn = (By.LINK_TEXT, '车锁管理')
    lock_number_Btn = (By.NAME, 'lock_sn')
    lock_name_Btn = (By.NAME, 'lock_name')
    lot_number_Btn = (By.NAME, 'batch_num')
    submitBtn = (By.CSS_SELECTOR, '.btn-success')
    backBtn = (By.LINK_TEXT, '返回')
    addBtn = (By.LINK_TEXT, '新增')
    exportBtn = (By.XPATH, '导出')
    searchBtn = (By.LINK_TEXT, '搜索')

    def addLock_action(self, count):
        # 进入单车管理模块
        self.driver.find_element(*self.bicycle_management_Btn).click()
        sleep(2)
        # 进入车锁管理页面
        self.driver.find_element(*self.car_lock_management_Btn).click()
        sleep(2)
        # 点击新增按钮
        self.driver.find_element(*self.addBtn).click()
        sleep(2)
        # 输入锁编号
        self.driver.find_element(*self.lock_number_Btn).send_keys(count)
        sleep(2)
        # 输入锁名称
        self.driver.find_element(*self.lock_name_Btn).send_keys(count)
        sleep(2)
        # 输入批号
        self.driver.find_element(*self.lot_number_Btn).send_keys(count)
        sleep(2)
        # 点击提交按钮
        self.driver.find_element(*self.submitBtn).click()

        return count


if __name__ == "__main__":
    driver = desired_chrome()
    login = LoginView(driver)
    login.login_action('admin', '123456')
    add = AddLock(driver)
    count = 1363
    i = 1 
    while i < 200:
        add.addLock_action(count)
        i = i + 1
        count = count + 1