# --coding:utf-8--
import time
import unittest
from selenium.webdriver.common.by import By
from common.login_utils import LoginUtils
from common.action import Action

class Product(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Action().selenium_default()
        LoginUtils().default_login(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_product(self):
        '''点击产品链接测试'''
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//li[@data-id="product"]').click()
        time.sleep(1)
        title = self.driver.title
        self.assertEqual(title,'产品主页 - 禅道','test_product测试失败')