# --coding:utf-8--
import unittest
import os
from selenium import webdriver
from common.config_utils import config
current = os.path.dirname(__file__)
driver_path = os.path.join(current,'../webdriver/chromedriver.exe')

class Action():
    def selenium_default(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get(config.get_url())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver