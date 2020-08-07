#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang
#与公众号接发消息，校验token

from flask import Flask, request, make_response
import hashlib
from weixin_robot.handle import *

app = Flask(__name__)
app.debug = True

@app.route('/')  # 默认网址
def index():
    return '测试页面'


@app.route('/wx', methods=['GET', 'POST'])
def wechat_auth():  # 处理微信请求的处理函数，get方法用于认证，post方法取得微信转发的数据
    if request.method == 'GET':
        token = 'jiuhuacanmandishang'  # 这里填公众号里设置的token。
        data = request.args
        signature = data.get('signature', '')
        timestamp = data.get('timestamp', '')
        # print(timestamp)
        nonce = data.get('nonce', '')
        echostr = data.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        s = s.encode(encoding='utf-8')
        #加密后的token匹配上signature
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)
        else:
            return 'signature is error'
    else:
        token = 'jiuhuacanmandishang'  # 这里填公众号里设置的token。
        data = request.args
        signature = data.get('signature', '')
        timestamp = data.get('timestamp', '')
        # print(timestamp)
        nonce = data.get('nonce', '')
        echostr = data.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        s = s.encode(encoding='utf-8')
        # 加密后的token匹配上signature
        if (hashlib.sha1(s).hexdigest() == signature):
            rec = request.stream.read()
            # with open("./debug.log", "a") as file:
            #     file.write(rec)
            # file.close()
            resp = parse_msg(rec)
            return make_response(resp.encode("gbk"))
        else:
            return 'signature is error'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug=True)