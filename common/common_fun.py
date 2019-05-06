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

    homepageBtn = (By.ID, 'content-wrapper')
    messageBtn = (By.ID, 'button-message')
    myselfBtn = (By.CLASS_NAME, 'dropdown-toggle')

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

    # 点击主页图标
    def click_homepageBtn(self):
        self.driver.find_element(*self, homepageBtn).click()

    # 点击消息通知图标
    def click_messageBtn(self):
        self.driver.find_element(*self, messageBtn).click()

    # 点击我的信息
    def click_myselfBtn(self):
        self.driver.find_element(*self, myselfBtn).click()



class PageModule(BaseView):

    dash_board_Btn = (By.LINK_TEXT, '仪表盘')

    # 进入仪表盘模块
    def click_dash_board_Btn(self):
        self.driver.find_element(*self, dash_board_Btn).click()


class Page(BaseView):

    bicycle_details_Btn = (By.LINK_TEXT, '单车明细')

    # 进入单车明细页面
    def click_bicycle_details_Btn(self):
        self.driver.find_element(*self, bicycle_details_Btn).click()



if __name__ == "__main__":
    print("ok")