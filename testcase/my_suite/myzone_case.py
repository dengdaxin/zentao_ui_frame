# --coding:utf-8--
import time
import unittest
from selenium.webdriver.common.by import By
from common.login_utils import LoginUtils
from common.action import Action

class Myzone(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Action().selenium_default()
        LoginUtils().default_login(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_myzone(self):
        '''点击我的地盘测试'''
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//li[@data-id="my"]').click()
        time.sleep(1)
        title = self.driver.title
        self.assertEqual(title,'我的地盘 - 禅道','test_myzone测试失败')