#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
板块不同：沪市只有A主板与B股；深市有A主板、中小板、创业板和B股。
股票代码不同：沪市主板是60开头，B股是900开头；深市主板是000开头，中小板是002开头、创业板是300开头、B股是200开头。
B股标价不同：沪市是以美元竞价；深市是以港币竞价。
"""
import requests
import json
from he.stock_compute.FigureMap import *


def decide_market(q):
    if q[0] in ["6", "9"]:
        return "sh" + q
    elif q[0] in ["0", "2", "3"]:
        return "sz" + q


def get_data(q):
    """
    获取目标股票数据
    :return:
    """
    q = decide_market(q)
    url = "http://qt.gtimg.cn/q=%s" % (q)
    c = requests.get(url)
    print(c.content)
    return c.content.decode("gbk")


def get_s_data(q):
    """
    获取股票简要信息
    :param q:
    :return:
    """
    q = decide_market(q)
    url = "http://qt.gtimg.cn/q=s_%s" % (q)
    c = requests.get(url)
    print(c.content)
    return c.content.decode("gbk")


def get_s_pk(q):
    """
    获取股票盘口信息
    :param q:
    :return:
    """
    q = decide_market(q)
    url = "http://qt.gtimg.cn/q=s_pk%s" % (q)
    c = requests.get(url)
    res = c.content.decode("gbk").split("=\"")[1]
    res = res.split("\"")[0]
    return res


def get_ff_data(q):
    """
    获取股票资金流向
    :param q:
    :return:
    """
    q = decide_market(q)
    url = "http://qt.gtimg.cn/q=ff_%s" % (q)
    c = requests.get(url)
    res = c.content.decode("gbk").split("=\"")[1]
    return res


def makeup_data(dataType, q):
    data_makeuped = {}
    if dataType == "RT":
        data_string = get_data(q)
        data_list = data_string.split("~")
        for index, num in enumerate(data_list):
            if index == 0:
                continue
            elif 9 <= index <= 18 or 19 <= index <= 28:
                continue
            elif index == 49:
                break
            else:
                data_makeuped[RT[str(index)]] = num
        buy5 = {}
        segment = data_list[9:19:2]
        for index, d in enumerate(segment):
            buy5[d] = data_list[index * 2 + 10]
        data_makeuped["买5"] = buy5
        sale5 = {}
        segment = data_list[19:29:2]
        for index, d in enumerate(segment):
            sale5[d] = data_list[index * 2 + 20]
        data_makeuped["卖5"] = sale5
    elif dataType == "ff":
        data_string = get_ff_data(q)
        data_list = data_string.split("~")
        for index, num in enumerate(data_list):
            if index == 14:
                break
            data_makeuped[FF[str(index)]] = num
    elif dataType == "s_pk":
        data_string = get_s_pk(q)
        data_list = data_string.split("~")
        for index, num in enumerate(data_list):
            data_makeuped[HANDICAP[str(index)]] = num
    elif dataType == "s_":
        data_string = get_s_data(q)
        data_list = data_string.split("~")
        for index, num in enumerate(data_list):
            if index == 10:
                 break
            else:
                data_makeuped[SIMPLE[str(index)]] = num

    print(data_makeuped)
    return data_makeuped


if __name__ == "__main__":
    makeup_data(dataType="RT", q="000725")
