#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import os

class PerfectWorld():

    def __init__(self):
        self.url = "https://www.dota2.com.cn/heroes/index.htm"


    def hero(self):
        url = "https://www.dota2.com.cn/heroes/index.htm"
        con=requests.get(url=url,verify=False)
        path = os.getcwd()
        f = open(os.path.join(path,"test.html"),mode="a+")
        f.write(con.content.decode(""))
        f.close()
        print(con.status_code)


if __name__ == "__main__":
    PerfectWorld().hero()