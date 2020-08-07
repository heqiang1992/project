#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang

"""
app id :wx06c79109521e34d2

"""

# 扫码登录微信
# from wxpy import *
# bot = Bot(cache_path=True)
#
# bot.file_helper.send("hello")

import requests
from urllib import parse
import itchat
from flask import Flask, request, make_response
import json


url = "https://api.zhetaoke.com:10001/api/open_gaoyongzhuanlian_tkl.ashx"
appkey = "c163ccbe7f7b4291a81afb74804e7d35"
sid = "36576"
pid = "mm_55844929_1958550315_110731150452"

def tkl_api(tkl):
    tkl_urlencode = tkl.encode("gbk")
    formData = "appkey=%s&sid=%s&pid=%s&tkl=%s&signurl=5" % (appkey, sid, pid, tkl_urlencode)
    # print(formData)
    con = requests.get(url=url + "?" + formData)
    if con.status_code == "200":
        res = con.content.decode("utf-8")
        product_messages = json.loads(res)["content"]
        # print(dd["content"])
        return product_messages["tkl"]
    else:
        return "tkl 错误"

