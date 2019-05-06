#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from common.desired import desired_chrome
from logs.loger import logging
from time import sleep


class startEnd(unittest.TestCase):

    def setUp(self):
        logging.info('======setUp======')
        self.driver = desired_chrome()

    def tearDown(self):
        logging.info('======tearDown======')
        sleep(10)
        self.driver.close_app()
