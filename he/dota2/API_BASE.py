#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import os

#接口文档 https://docs.opendota.com/#section/Authentication

class PerfectWorld():

    def __init__(self):
        self.url = "https://api.opendota.com/api/"

    def get_heroes_list(self):
        url = self.url + "heroes"
        con = requests.get(url=url, verify=False)
        print(con.content.encode)
    def hero(self):
        url = self.url+"heroes"
        con=requests.get(url=url,verify=False)
        path = os.getcwd()
        f = open(os.path.join(path,"test.html"),mode="a+")
        f.write(con.content.decode(""))
        f.close()
        print(con.status_code)


if __name__ == "__main__":
    a = PerfectWorld()
    a.get_heroes_list()