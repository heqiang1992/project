# -*- coding:utf-8 -*-
__autthor__ = "heqiang"

from selenium import webdriver
import os, time
from selenium.webdriver.common.action_chains import ActionChains





class taobao():

    def __init__(self,username,pwd):
        self.driver = webdriver.Chrome()

        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        # driver = webdriver.Chrome(options = option)

        url = "https://www.taobao.com"
        self.username = username
        self.pwd = pwd
        self.driver.get(url)

    def login(self):
        self.driver.find_element_by_xpath(xpath="//*[@id=\"J_SiteNavLogin\"]/div[1]/div[1]/a[1]")

        #密码登录
        if self.driver.find_element_by_id("J_Quick2Static"):
            self.driver.find_element_by_id("J_Quick2Static").click()
        self.driver.find_element_by_name("TPL_username").send_keys(self.username)
        self.driver.find_element_by_name("TPL_password").send_keys(self.pwd)

        self.driver.find_element_by_id("J_SubmitStatic").click()


if __name__ == "__main__":
    t = taobao(username="18502886670",pwd="heqiang1992")
    t.login()