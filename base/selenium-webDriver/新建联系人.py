# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class add_contact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get("http://localhost/smeoa/login")
        driver.find_element_by_id("emp_no").clear()
        driver.find_element_by_id("emp_no").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_xpath(u"//input[@value='登录']").click()
        driver.find_element_by_xpath("//div[@id='navbar-collapse-6']/ul/a[9]/i").click()
        driver.find_element_by_link_text(u"新建").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | _self | 30000]]
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"张三")
        driver.find_element_by_id("dept").clear()
        driver.find_element_by_id("dept").send_keys(u"研发部")
        driver.find_element_by_id("office_tel").clear()
        driver.find_element_by_id("office_tel").send_keys("13455553445")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("65182863@qq.com")
        driver.find_element_by_xpath(u"//input[@value='保存']").click()
        time.sleep(3)
        self.assertRegexpMatches(driver.find_element_by_css_selector("div.modal-content").text, r"^[\s\S]*新增成功[\s\S]*$")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        # driver.find_element_by_tag_name()
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
#当该module被其他的module引入使用时,不会自己执行。
if __name__ == "__main__":
    unittest.main()