# encoding:utf-8
# @author:ddx
# @time:2021/8/1 9:07

import os
from selenium import webdriver
from common.config_utils import config
from common.basepage import BasePage

current = os.path.dirname(__file__)
driver_path = os.path.join(current,'../webdriver/chromedriver.exe')

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.username_input ={'element_name':'用户名输入框',
                              'element_type':'xpath',
                              'element_value':'//input[@id="account"]',
                              'timeout':5}
        self.password_input = {'element_name': '密码输入框',
                               'element_type': 'xpath',
                               'element_value': '//input[@name="password"]',
                               'timeout': 5}
        self.login_button = {'element_name': '登录按钮',
                               'element_type': 'xpath',
                               'element_value': '//button[@id="submit"]',
                               'timeout': 5}

    def input_username(self,username):
        self.input(self.username_input,username)

    def input_password(self,password):
        self.input(self.password_input,password)

    def click_login(self):
        self.click(self.login_button)

if __name__=='__main__':
    driver = webdriver.Chrome(executable_path=driver_path)
    login = LoginPage(driver)
    login.open_url(config.get_url())
    login.input_username('test01')
    login.input_password('newdream123')
    login.click_login()

