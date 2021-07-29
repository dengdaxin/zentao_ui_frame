# --coding:utf-8--
import time
import unittest
from selenium.webdriver.common.by import By
from common.login_utils import LoginUtils
from common.action import Action

class Quit(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Action().selenium_default()
        LoginUtils().default_login(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_quit(self):
        '''退出登录测试'''
        self.driver.find_element(By.XPATH,'//ul[@id="userNav"]').click()
        self.driver.find_element(By.XPATH, '//a[text()="退出"]').click()
        time.sleep(1)
        title =self.driver.title
        self.assertEqual(title,'用户登录 - 禅道','test_quit测试失败')