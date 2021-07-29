# --coding:utf-8--

import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.login_utils import LoginUtils
from common.action import Action
current = os.path.dirname(__file__)
driver_path = os.path.join(current,'../../webdriver/chromedriver.exe')

class LoginFail(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Action().selenium_default()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()


    def test_login_fail(self):
        '''密码错误的登录测试'''
        LoginUtils().login(self.driver,'test01','newdream')
        # self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('test01')
        # self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream')
        # self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        time.sleep(1)
        alter_text = self.driver.switch_to.alert.text
        self.assertEqual(alter_text,'登录失败，请检查您的用户名或密码是否填写正确。','test_login_fail测试失败')


    def test_login_fail02(self):
        '''账号错误的登录测试'''
        LoginUtils().login(self.driver, 'test090', 'newdream123')
        # self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('test090')
        # self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        # self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        time.sleep(2)
        alter_text = self.driver.switch_to.alert.text
        self.assertEqual(alter_text,'登录失败，请检查您的用户名或密码是否填写正确。','test_login_fail02测试失败')




