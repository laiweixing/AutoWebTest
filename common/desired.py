#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
启动配置 

"""
from selenium import webdriver

def desired_chrome():
    driverfile_path = r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driverfile_path)
    bicycle_38 = "https://thirty-eight.e-stronger.com/admin/index.php?route=bicycle/bicycle"
    driver.get(bicycle_38)
    return driver


if __name__ == "__main__":
    desired_chrome()