# --coding:utf-8--


from selenium.webdriver.common.by import By

class LoginUtils():

    def login(self,driver,username,password):
        driver.find_element(By.XPATH,'//input[@id="account"]').send_keys(username)
        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//button[@id="submit"]').click()

    def default_login(self,driver):
        self.login(driver,'test01','newdream123')