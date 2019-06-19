#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
18230036107
569247yq
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import SC_Data
import time
from PIL import Image
import pytesseract


class LoginBase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://weibo.com/"

    def init_wed_driver(self):
        self.driver.get(self.base_url)

    def login(self):
        self.driver.find_element_by_id()

    def input_info(self, username, password):
        """
        输入账号
        :param username:
        :param password:
        :return:
        """
        element = self.driver.find_element_by_id("loginname")
        element.clear()
        element.send_keys(username)
        element = self.driver.find_element(by=By.XPATH, value="//*[@id=\"pl_login_form\"]/div/div[3]/div[2]/div/input")
        element.clear()
        element.send_keys(password)
        time.sleep(5)


    def get_png(self):
        """
        获取验证码图片
        """
        screen_cap = SC_Data.PNGPATH
        self.driver.save_screenshot(screen_cap)
        png_location = self.driver.find_element_by_xpath("//*[@id=\"pl_login_form\"]/div/div[3]/div[3]/a/img").location
        png_size = self.driver.find_element_by_xpath("//*[@id=\"pl_login_form\"]/div/div[3]/div[3]/a/img").size
        rangle = (
        int(png_location['x']), int(png_location['y']), int(png_location['x'] + png_size['width']), int(png_location['y'] + png_size['height']))
        i = Image.open(screen_cap)
        code_png = i.crop(rangle)
        code_png.save(screen_cap)
        return screen_cap


if __name__ == "__main__":
    item = LoginBase()
    item.init_wed_driver()
    item.input_info("18230036107", "569247yq")
    item.get_png()
