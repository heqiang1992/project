#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import request
import SC_Data
import os

class sinaBase():

    def __init__(self):
        pass
        self.login()

    def login(self):
        pass

    def get_homepage(self):
        get_data = {}
        res = request("get", "https://m.weibo.cn/")
        print res.status_code
        self.generate_html_file(res.content)
        return res

    def generate_html_file(self, string):
        f = open(SC_Data.FILEPATH, "a+")
        f.write(string)
        f.close()

a = sinaBase()
a.get_homepage()
