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
import wechatpy
import itchat
from flask import Flask, request, make_response
import json

# app = Flask(__name__)
# app.debug = True
#
#
# @app.route('/')  # 默认网址
# def index():
#     return '测试页面'
#
#
#
# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port=80, debug=True)


url = "https://api.zhetaoke.com:10001/api/open_gaoyongzhuanlian_tkl.ashx"
appkey = "c163ccbe7f7b4291a81afb74804e7d35"
sid = "36576"
pid = "mm_55844929_1958550315_110731150452"
tkl = "%E7%B7%AE%E7%BD%AE%E6%9C%AC%E6%AE%B5%E5%86%85%E5%AE%B9%E2%82%B3tQxac0mHeEd%E2%82%B3%E8%BE%BE%E5%BC%80%E6%B7%98tao%E5%AF%B3%E6%88%96%E7%82%B9%E5%87%A0%E9%93%BE%E8%A1%97https%3A%2F%2Fm.tb.cn%2Fh.Vu1DHx7%3Fsm%3Db0ffd3%20%E8%87%B3%E6%B5%8F.%E8%A7%88%E8%A7%88.%E5%99%A8%E3%80%90%E5%85%A8%E6%B0%91K%E6%AD%8C%E7%A5%9E%E5%99%A8%E6%89%8B%E6%9C%BA%E9%BA%A6%E5%85%8B%E9%A3%8E%E6%97%A0%E7%BA%BF%E8%93%9D%E7%89%99%E5%AE%B6%E7%94%A8%E5%94%B1%E6%AD%8C%E5%84%BF%E7%AB%A5%E8%AF%9D%E7%AD%92%E9%9F%B3%E5%93%8D%E4%B8%80%E4%BD%93%E7%94%B5%E8%84%91%E5%8F%B0%E5%BC%8F%E7%94%B5%E5%AE%B9%E9%BA%A6%E5%85%A8%E8%83%BD%E9%BA%A6%E5%85%A8%E5%90%8D%E5%8D%A1%E6%8B%89OK%E4%B8%93%E7%94%A8%E9%80%9A%E7%94%A8%E3%80%91"
formData = "appkey=%s&sid=%s&pid=%s&tkl=%s&signurl=5" % (appkey, sid, pid, tkl)
# print(formData)
con = requests.get(url=url + "?" + formData)
res = con.content.decode("utf-8")
dd = json.loads(res)
print(dd["content"])

# url = "https://api.zhetaoke.com:10001/api/open_gaoyongzhuanlian.ashx"
# appkey = "c163ccbe7f7b4291a81afb74804e7d35"
# sid = "36576"
# pid = "mm_55844929_1958550315_110731150452"
# tkl = "%E7%B7%AE%E7%BD%AE%E6%9C%AC%E6%AE%B5%E5%86%85%E5%AE%B9%E2%82%B3tQxac0mHeEd%E2%82%B3%E8%BE%BE%E5%BC%80%E6%B7%98tao%E5%AF%B3%E6%88%96%E7%82%B9%E5%87%A0%E9%93%BE%E8%A1%97https%3A%2F%2Fm.tb.cn%2Fh.Vu1DHx7%3Fsm%3Db0ffd3%20%E8%87%B3%E6%B5%8F.%E8%A7%88%E8%A7%88.%E5%99%A8%E3%80%90%E5%85%A8%E6%B0%91K%E6%AD%8C%E7%A5%9E%E5%99%A8%E6%89%8B%E6%9C%BA%E9%BA%A6%E5%85%8B%E9%A3%8E%E6%97%A0%E7%BA%BF%E8%93%9D%E7%89%99%E5%AE%B6%E7%94%A8%E5%94%B1%E6%AD%8C%E5%84%BF%E7%AB%A5%E8%AF%9D%E7%AD%92%E9%9F%B3%E5%93%8D%E4%B8%80%E4%BD%93%E7%94%B5%E8%84%91%E5%8F%B0%E5%BC%8F%E7%94%B5%E5%AE%B9%E9%BA%A6%E5%85%A8%E8%83%BD%E9%BA%A6%E5%85%A8%E5%90%8D%E5%8D%A1%E6%8B%89OK%E4%B8%93%E7%94%A8%E9%80%9A%E7%94%A8%E3%80%91"
# formData = "appkey=%s&sid=#%s#&pid=#%s#&tkl=%s&signurl=5"%(appkey,sid,pid,tkl)
# print(formData)
# con = requests.post(url=url+"?"+formData)
#
# print(con.content.decode("utf-8"))
