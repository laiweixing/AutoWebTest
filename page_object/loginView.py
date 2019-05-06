#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
登录功能封装 

"""
from common.desired import desired_chrome
from logs.loger import logging
from common.common_fun import Common
from selenium.webdriver.common.by import By


class LoginView(Common):

    username_type = (By.ID, 'input-username')
    password_type = (By.ID, 'input-password')
    loginBtn = (By.TAG_NAME, 'button')

    def login_action(self, username, password):
        logging.info('======登录开始======')
        logging.info('username is:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('======点击登录按钮======')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('======登录完成======')


if __name__ == '__main__':
    driver = desired_chrome()
    login = LoginView(driver)
    login.login_action('admin', '123456')