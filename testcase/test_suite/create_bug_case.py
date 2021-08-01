# --coding:utf-8--
import time
import unittest
from selenium.webdriver.common.by import By
from common.login_utils import LoginUtils
from common.action import Action

class CreateBug(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Action().selenium_default()
        LoginUtils().default_login(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_create_bug(self):
        '''新增bug测试'''
        self.driver.find_element(By.XPATH, '//li[@data-id="qa"]').click()
        self.driver.find_element(By.XPATH, '//li[@data-id="bug"]').click()
        self.driver.find_element(By.XPATH,
                            '//a[@href="/zentao/www/index.php?m=bug&f=create&productID=5&branch=0&extra=moduleID=0"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[@id="product_chosen"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//li[@title="DBShop电商项目"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[@id="module_chosen"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//li[@title="/统计分析"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="project_chosen"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//li[@title="DBShopv1.0"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//div[@id="openedBuild_chosen"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//li[@title="主干"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//div[@id="assignedTo_chosen"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//li[@title="D:开发人员1"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@id="deadline"]').send_keys('2021-07-30')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//div[@id="type_chosen"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//li[@title="安全相关"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//div[@id="os_chosen"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//li[@title="全部"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//div[@id="browser_chosen"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//li[@title="chrome"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@id="title"]').send_keys('ddx到此一游,永劫无间开黑咯，啊哈哈哈哈哈哈')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//div[@data-type="severity"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//span[@data-value="4"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//div[@data-type="pri"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                            '/html/body/main/div/div[1]/div/form/table/tbody/tr[5]/td/div/div[3]/div/div/span[4]').click()
        time.sleep(1)
        iframe = self.driver.find_element(By.XPATH, '//iframe[@class="ke-edit-iframe"]')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.XPATH, '//body[@class="article-content"]').clear()
        self.driver.find_element(By.XPATH, '//body[@class="article-content"]').send_keys('这就是bug描述而已')
        self.driver.switch_to.default_content()
        time.sleep(2)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        self.driver.find_element(By.XPATH, '//*[@id="submit"]').click()