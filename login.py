#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
登录界面 

"""
from selenium import webdriver
from time import sleep

# ----------引入第三方库-------------

# 驱动文件路径
driverfile_path = r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
# 启动浏览器
driver = webdriver.Chrome(executable_path=driverfile_path)
# 打开38所共享单车后台管理系统
driver.get(r'https://thirty-eight.e-stronger.com/admin/index.php?route=bicycle/bicycle')


# 登录
def login():
    driver.find_element_by_id('input-username').send_keys('admin')
    sleep(1)
    driver.find_element_by_id('input-password').send_keys('123456')
    sleep(1)
    driver.find_element_by_tag_name('button').click()
    sleep(3)

login()

if __name__ == '__main__':
    login()