from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from auto_test_module.common.setup import setup
import time
class login:
    def __init__(self):
        self.driver = setup().driver
    def __input(self,username,passwd):
        self.driver.find_element_by_id("emp_no").clear()
        self.driver.find_element_by_id("emp_no").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(passwd)
    def __click_login_button(self):
        self.driver.find_element_by_xpath("//form[@id='form_login']/div[4]/div/input").click()
    def __click_login_key(self):
        self.driver.find_element_by(tag_name="button",value="登录").click()
    def login_start(self,username,passwd):
        self.__input(username,passwd)
        self.__click_login_button()
    def ASSERT(self):
        try:
            self.driver.find_element_by_class_name("navbar-brand")
        except:
            print("log  failed ")
        else:
            print("log  success ")
        return self.driver
    def quit(self):
        time.sleep(2)
        self.driver.quit()
        time.sleep(2)