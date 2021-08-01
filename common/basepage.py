# encoding:utf-8
# @author:ddx
# @time:2021/8/1 13:58
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.log_utils import logger
from selenium import webdriver

class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开网页：%s' % url)

    def get_title(self):
        title = self.driver.title
        logger.info('获取页面title，title为：%s' % title)
        return title

    def input(self,element_info,content):
        element = self.find_element(element_info)
        try:
            element.send_keys(content)
            logger.info('%s元素输入内容，输入的内容是：%s' % (element_info['element_name'],content))
        except Exception as e:
            logger.error('[%s]元素输入内容失败,原因是：%s' % (element_info['element_name'],e))

    def find_element(self,element_info):
        try:
            element_name = element_info['element_name']
            element_type_name = element_info['element_type']
            element_value = element_info['element_value']
            timeout = element_info['timeout']
            if element_type_name == 'xpath':
                element_type = By.XPATH
            if element_type_name == 'id':
                element_type = By.ID
            if element_type_name == 'name':
                element_type = By.NAME
            element = WebDriverWait(self.driver,timeout).until(lambda x: x.find_element(element_type,element_value))
            logger.info('元素识别成功，元素名称是：%s' % element_name)
        except Exception as e:
            logger.error('[%s]元素识别失败' % element_name)
        return element

    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('%s元素点击成功'% element_info['element_name'])

    def max_windows(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')