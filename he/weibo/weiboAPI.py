#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weibo import APIClient, HttpObject
import webbrowser
import requests
import json, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
from he.weibo.SC_Data import weiboAPP

"""
接口文档
https://open.weibo.com/wiki/2/statuses/user_timeline
"""


class WaterRobot():

    def __init__(self):
        pass

    def authorization(self, **kwargs):
        APP_KEY = kwargs.get("APP_KEY")
        APP_SECRET = kwargs.get("APP_SECRET")
        CALLBACK_URL = kwargs.get("CALLBACK_URL")
        USER = kwargs.get("USER")
        PWD = kwargs.get("PWD")
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
        url = client.get_authorize_url()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(url)
        time.sleep(5)
        driver.find_element_by_id("userId").send_keys(USER)
        ActionChains(driver).double_click(
            driver.find_element(by=By.XPATH, value="/html/body/label")).perform()
        for i in PWD:
            pyautogui.hotkey(i)
        time.sleep(2)
        dis = driver.find_element_by_xpath("//*[@id=\"outer\"]/div/div[2]/form/div/div[1]/div[1]/p[3]").get_attribute(
            "style")
        if not dis == 'display: none;':
            ActionChains(driver).double_click(
                driver.find_element(by=By.XPATH,
                                    value="//*[@id=\"outer\"]/div/div[2]/form/div/div[1]/div[1]/p[3]/label")).perform()
            print('输入输入验证码登录后再往控制台按回车键：')
            input()

        driver.find_element_by_xpath("//*[@id=\"outer\"]/div/div[2]/form/div/div[2]/div/p/a[1]").click()
        time.sleep(1)
        try:
            driver.find_element_by_xpath("//*[@id=\"outer\"]/div/div[2]/form/div/div[2]/div/p/a[1]").click()
            time.sleep(1)
        except:
            pass
        code = driver.current_url.split("code=")[-1]
        driver.minimize_window()
        print(code)
        r = client.request_access_token(code)
        print(r)
        self.access_token = r.access_token  # 新浪（授权服务器）返回的token
        expires_in = r.expires_in

        client.set_access_token(self.access_token, expires_in)
        self.client = client
        driver.close()

    def public_timeline(self):
        result = self.client.public_timeline()  # 公共微博的数据
        print(json.dumps(result, indent=2, ensure_ascii=False))
        number = result["total_number"]
        print(number, "users:")
        for u in result["statuses"]:
            print(u["user"]["screen_name"])
            print(u["user"]["location"])
            print(u["text"])
        return result

    def comments_create(self, comment, id):

        # data = {"access_token": access_token,"comment":"nihao","id":"1005055013"}
        # con = requests.post(url="https://api.weibo.com/2/comments/create.json",json=data)
        c = HttpObject(client=self.client, method=1)
        res = c.comments__create(comment=comment, id=id)
        print(res)
        return res

    def user_timeline(self):
        data = {"access_token":self.access_token}
        con = self.client.get(url="https://api.weibo.com/2/statuses/user_timeline.json",data=json.dumps(data))
        # res = c.statuses__user_timeline()
        print(con)
        # return res

    def users_show(self, uid):
        c = HttpObject(client=self.client, method=0)
        res = c.users__show(uid=uid)
        print(res)
        return res

    def get_statuses_id(self, index=0):
        """
        只能获取自己账户的微博列表
        :param index: 获取第几条的ID
        :return:
        """
        res = self.user_timeline()
        target = res["statuses"][index]
        print("微博内容是：%s" % (target["text"]))
        return target["id"]



c1 = WaterRobot()
c1.authorization(**weiboAPP[0])
id = c1.user_timeline()
# c2 = WaterRobot()
# c2.authorization(**weiboAPP[1])
# c2.comments_create(comment="nihao",id=id)
