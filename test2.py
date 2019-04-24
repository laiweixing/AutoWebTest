#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
添加车锁

"""
import login
from login import driver
from time import sleep

# 进入车锁管理页面
sleep(5)
driver.find_element_by_link_text('单车管理').click()
sleep(1)
driver.find_element_by_link_text('车锁管理').click()
sleep(1)

# 添加锁信息
count = 1356
i = 1
while i < 267:
    driver.find_element_by_link_text('新增').click()
    sleep(1)
    driver.find_element_by_name('lock_sn').send_keys(count)
    sleep(1)
    driver.find_element_by_name('lock_name').send_keys(count)
    sleep(1)
    driver.find_element_by_name('batch_num').send_keys(count)
    sleep(1)
    driver.find_element_by_css_selector('.btn-success').click()
    sleep(3)
    i = i + 1
    count = count + 1
print("500把锁编号添加完成")



if __name__ == '__main__':
    print("ok")