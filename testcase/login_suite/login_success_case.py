# --coding:utf-8--

import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.login_utils import LoginUtils
from common.config_utils import config
from common.action import Action
current = os.path.dirname(__file__)
driver_path = os.path.join(current,'../../webdriver/chromedriver.exe')

class LoginSuccess(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Action().selenium_default()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()


    def test_login_success(self):
        '''登录成功测试'''
        LoginUtils().login(self.driver,'test01','newdream123')
        # self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('test01')
        # self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        # self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        time.sleep(1)
        result = self.driver.find_element(By.XPATH,'//span[@class="user-name"]').text
        self.assertEqual(result,'测试人员1','test_login_success测试失败')





