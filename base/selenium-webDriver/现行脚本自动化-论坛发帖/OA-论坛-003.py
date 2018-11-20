# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class L001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()#.Ie(r"C:\Program Files\Internet Explorer\iexplore.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_001(self):
        driver = self.driver
        driver.get(self.base_url + "/smeoa/login")
        driver.find_element_by_id("emp_no").clear()
        driver.find_element_by_id("emp_no").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_xpath(u"//input[@value='登录']").click()
        driver.find_element_by_link_text(u"论坛").click()
        driver.find_element_by_css_selector("div.auto > a").click()
        driver.find_element_by_link_text(u"发帖").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | _self | 30000]]
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"哈哈哈哈")
        iframe = driver.find_element_by_class_name("ke-edit-iframe")
        driver.switch_to_frame(iframe)
        driver.find_element_by_class_name("ke-content").send_keys("")
        driver.switch_to.default_content()
        driver.find_element_by_xpath(u"//input[@value='保存']").click()
        time.sleep(0.5)
        # self.assertRegexpMatches(driver.find_element_by_xpath("//form[@id='form_data']/li[2]").text, r"^[\s\S]*新年快乐！[\s\S]*$")
        log = open("D:\\test_info.log","a+")
        if driver.find_element_by_class_name("gritter-item").text == "请输入内容":
            log.write("[fail !]OA-论坛-002\n")
            driver.quit()
        else:
            log.write("[success !]OA-论坛-002\n")
            driver.quit()
        log.close()
        time.sleep(2)
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

if __name__ == "__main__":
    unittest.main()
