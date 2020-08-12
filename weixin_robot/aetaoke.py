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
    tkl_urlencode = parse.quote(tkl)
    formData = "appkey=%s&sid=%s&pid=%s&tkl=%s&signurl=5" % (appkey, sid, pid, tkl_urlencode)
    # print(formData)
    con = requests.get(url=url + "?" + formData)
    if con.status_code == 200:
        res = con.content.decode("utf-8")
        product_messages = json.loads(res)["content"][0]
        # print(dd["content"])
        if "\"status\":200" in res:
            info_tuple = (product_messages["title"], product_messages["tkl"], product_messages["size"],
                          product_messages["coupon_info_money"], product_messages["quanhou_jiage"], "off", "offf")
            info = "%s一一一一反 利 消 息一一一一\n%s\n【原  价】%s\n【卷  额】%s\n【付  费】%s\n【预计返】%s\n------------------\n復.制本信息，再去τao寶下单，为威信预计返%s" % info_tuple

            return info
        else:
            return "淘口令 错误"
    else:
        return "返回错误，请检查参数"


if __name__ == "__main__":
    kouling = tkl_api(
        "fu至内容€nvNlcYfTPba€达开ta0寶或點击链街https://m.tb.cn/h.VGQzIXv?sm=5eeeb8 至瀏lan嘂..【珍视明蒸汽眼罩热敷眼睛罩睡眠遮光透气眼疲劳发热眼贴缓解男女】")
    print(kouling)

    # kouling = tkl_api(
    #     "fu植内容¢0oqCcYN3Zea¢达开τao寶【2020年新款夏季网红上衣服早秋原宿港风超火ins情侣女装短袖t恤潮】")
    # print(kouling)

    # kouling = tkl_api(
    #     "复制这条信息，￥0oqCcYN3Zea￥，打开【手机淘宝】即可")
    # print(kouling)
