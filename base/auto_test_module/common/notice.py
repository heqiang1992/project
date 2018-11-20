# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from auto_test_module.common.setup import setup
from auto_test_module.common.login import login
from auto_test_module.element.notice import notice_element

class notice(login):
    def __init__(self):
        login.__init__(self)
        self.login_start("admin","admin")
        self.driver.find_element_by_xpath(notice_element["button_notice"]).click()
    def create(self,title="默认：这里是标题",content="默认：这里是公告内容"):
        driver = self.driver
        driver.find_element_by_link_text(notice_element["notice_name"]).click()
        driver.find_element_by_link_text(u"新建").click()
        driver.find_element_by_id("name").send_keys(title)
        iframe = driver.find_element_by_class_name("ke-edit-iframe")
        driver.switch_to_frame(iframe)
        driver.find_element_by_class_name("ke-content").send_keys(content)
        driver.switch_to.default_content()
        driver.find_element_by_xpath(u"//input[@value='保存']").click()
    def create_judge(self,ID,expected):
        if self.driver.find_elements_by_class_name("system-message"):
            print(ID,"公告创建成功  预期结果：",expected)
        else:
            print(ID,"公告创建失败  预期结果：",expected)
        time.sleep(2)
        self.driver.quit()

    def notice_manage(self,title="notice-2017"):
        self.driver.find_element_by_link_text(u"公告管理").click()
        self.driver.find_element_by_id("name").send_keys(title)
        self.driver.find_element_by_xpath(notice_element["choose_node_button"]).click()
        iframe_target=self.driver.find_element_by_xpath("/html/body/div[4]/iframe")
        self.driver.switch_to.frame(iframe_target)
        self.driver.find_element_by_xpath(notice_element["choose_node"]).click()
        self.driver.find_element_by_link_text("确定").click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/"
                                              "div/div[3]/div[2]/form/div[3]/div/div/a/i").click()
        iframe_target=self.driver.find_element_by_class_name("myFrame")
        self.driver.switch_to.frame(iframe_target)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]"  #点击总经理
                                          "/div[1]/div[2]/div[2]/ul/li[1]/a/i").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/" #选择
                                          "div[1]/div[3]/div/nobr/label/span").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/"         #添加
                                          "div[2]/div[2]/div[2]/label/a").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/" #点击部长
                                           "div[1]/div[2]/div[2]/ul/li[2]/a/span").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/" #选择
                                          "div[1]/div[3]/div/nobr[3]/label/span").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/" #添加
                                          "div[2]/div[4]/label/a/i").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/" #点击员工
                                          "div[1]/div[2]/div[2]/ul/li[4]/a/span").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/"  #选择
                                          "div[1]/div[3]/div/nobr[2]/label/span").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[2]/"  #添加
                                          "div[2]/div[6]/label/a/i").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[1]/div[2]/a[1]").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/a[1]").click()
    def manage_assert(self):
        if self.driver.find_elements_by_class_name("system-message"):
            print("创建成功")
        else:
            print("创建失败")




