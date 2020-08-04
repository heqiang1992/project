#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang

"""
app id :wx06c79109521e34d2

"""

#扫码登录微信
# from wxpy import *
# bot = Bot(cache_path=True)
#
# bot.file_helper.send("hello")

import requests
import wechatpy
import itchat
from flask import Flask, request, make_response

app = Flask(__name__)
app.debug = True


@app.route('/')  # 默认网址
def index():
    return '测试页面'



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80, debug=True)




