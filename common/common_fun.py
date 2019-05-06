#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
公共函数、点击按钮

"""

from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
from logs.loger import logging
import time
import os
from selenium.webdriver.common.by import By


# 公共函数 封装成类 以供调用
class Common(BaseView):

    # 获取当前时间
    def getTime(self):
        logging.info("获取当前时间")
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now     

    # 截图函数
    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + "/screenshots/%s_%s.png" %(module, time)

        logging.info("get %s screenshot" %module)
        self.driver.get_sceenshot_as_file(image_file)


# 点击按钮 封装成类 以供调用
class Button(BaseView):

    homepageBtn = (By.ID, 'content-wrapper')
    messageBtn = (By.ID, 'button-message')
    myselfBtn = (By.CLASS_NAME, 'dropdown-toggle')
    submitBtn = (By.XPATH, '//*[@id="bicycle"]/form/div/div[4]/div/div/button')
    backBtn = (By.LINK_TEXT, '返回')
    addBtn = (By.LINK_TEXT, '新增')
    exportBtn = (By.XPATH, '导出')
    searchBtn = (By.LINK_TEXT, '搜索')

    # 点击主页图标
    def click_homepageBtn(self):
        self.driver.find_element(*self, homepageBtn).click()

    # 点击消息通知图标
    def click_messageBtn(self):
        self.driver.find_element(*self, messageBtn).click()

    # 点击我的信息
    def click_myselfBtn(self):
        self.driver.find_element(*self, myselfBtn).click()

    # 点击提交按钮
    def click_submitBtn(self):
        self.driver.find_element(*self, submitBtn).click()

    # 点击返回按钮
    def click_backBtn(self):
        self.driver.find_element(*self, backBtn).click()

    # 点击新增按钮
    def click_addNew(self):
        self.driver.find_element(*self, addBtn).click()

    # 点击导出按钮
    def click_export(self):
        self.driver.find_element(*self, export).click()

    # 点击搜索按钮
    def click_search(self):
        self.driver.find_element(*self, searchBtn).click()

if __name__ == "__main__":
    print("ok")