# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LogIn(unittest.TestCase):
    #继承unittest.TestCase
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_log_in(self):
        driver = self.driver
        driver.get(self.base_url + "/smeoa/login")
        log_file = open("d:\\log_in.txt","r")
        log_info_recv = open("d:\\log_info.txt","a+")
        for line in log_file.readlines():
            line = line.strip()
            new_line = line.split(",")
            print(new_line)
            # if new_line[0] == "admin" and new_line[1] == "admin":
            driver.find_element_by_id("emp_no").clear()
            driver.find_element_by_id("emp_no").send_keys(new_line[0])
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(new_line[1])
            driver.find_element_by_xpath(u"//input[@value='登录']").click()
            time.sleep(3)
            try:
                self.assertRegexpMatches(driver.find_element_by_link_text(u"小微企业信息化").text,
                                         r"^[\s\S]*小微企业信息化[\s\S]*$")
            except Exception as e:
                print("没有通过：",new_line[0]," , ",new_line[1])
                log_info_recv.write("[errror]:%s , %s\n"%(new_line[0],new_line[1]))
            else:
                print("passed")
                log_info_recv.write("[passed]:%s , %s\n"%(new_line[0],new_line[1]))
                driver.find_element_by_xpath("//div[@id='navbar-collapse-6']/ul/a[13]").click()
            time.sleep(5)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except Exception as e: return False
        return True
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except Exception as e: return False
        return True
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    def start_log(self):
        unittest.main()
if __name__ == "__main__":
    unittest.main()
