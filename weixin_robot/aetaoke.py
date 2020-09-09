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
from flask import Flask, request, make_response
import json
import datetime

appkey = "c163ccbe7f7b4291a81afb74804e7d35"
sid = "36576"
pid = "mm_55844929_1958550315_110731150452"


def tkl_api(tkl):
    url = "https://api.zhetaoke.com:10001/api/open_gaoyongzhuanlian_tkl.ashx"
    tkl_urlencode = parse.quote(tkl)
    formData = "appkey=%s&sid=%s&pid=%s&tkl=%s&signurl=5" % (appkey, sid, pid, tkl_urlencode)
    # print(formData)
    con = requests.get(url=url + "?" + formData)
    res = con.content.decode("utf-8")
    if con.status_code == 200 and "\"status\":200" in res:

        product_messages = json.loads(res)["content"][0]
        # print(dd["content"])
        info_tuple = (product_messages["title"], product_messages["tkl"], product_messages["size"],
                      product_messages["coupon_info_money"], product_messages["quanhou_jiage"], "off", "offf")
        info = "%s一一一一反 利 消 息一一一一\n%s\n【原  价】%s\n【卷  额】%s\n【付  费】%s\n【预计返】%s\n------------------\n復.制本信息，再去τao寶下单，为威信预计返%s" % info_tuple

        return True, info, product_messages["tao_id"]
    else:
        return False, "返回错误，请检查参数"


def order_check(starttime, type="1"):
    url = "https://api.zhetaoke.com:10001/api/open_dingdanchaxun2.ashx"
    endtime = datetime.datetime.strptime(starttime, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=3)
    formData = "appkey=%s&sid=%s&start_time=%s&end_time=%s&query_type=%s&tk_status=3&signurl=1" % (
        appkey, sid, starttime, endtime, type)
    # print(formData)
    con = requests.get(url=url + "?" + formData)
    if con.status_code == 200:
        res = con.content.decode("utf-8")
        messages = json.loads(res)
        tb_con = requests.get(url=messages["url"])
        tb_res = json.loads(tb_con.content.decode("utf-8"))
        if "publisher_order_dto" not in tb_res["tbk_sc_order_details_get_response"]["data"]["results"].keys():
            return []
        else:
            tb_message_list = tb_res["tbk_sc_order_details_get_response"]["data"]["results"][
                "publisher_order_dto"]
            print(tb_message_list)
            return tb_message_list


if __name__ == "__main__":
    # kouling = tkl_api(
    #     "fu至内容€nvNlcYfTPba€达开ta0寶或點击链街https://m.tb.cn/h.VGQzIXv?sm=5eeeb8 至瀏lan嘂..【珍视明蒸汽眼罩热敷眼睛罩睡眠遮光透气眼疲劳发热眼贴缓解男女】")
    # print(kouling)

    # kouling = tkl_api(
    #     "fu植内容¢0oqCcYN3Zea¢达开τao寶【2020年新款夏季网红上衣服早秋原宿港风超火ins情侣女装短袖t恤潮】")
    # print(kouling)

    # kouling = tkl_api(
    #     "复制这条信息，￥0oqCcYN3Zea￥，打开【手机淘宝】即可")
    # print(kouling)

    m = order_check(starttime="2020-08-21 09:00:00")
