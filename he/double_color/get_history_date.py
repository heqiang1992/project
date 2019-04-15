#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import requests
import json
from he.weibo import SC_Data
from bs4 import BeautifulSoup


class HistoryDC(object):

    def __init__(self):
        self.num_pool = []
        self.historyData = {}

    def WebConnection(self):
        """
        建立爬虫连接
        :return: 连接对象
        """
        data = {"expect": "all", "from": "19005", "to": "19034", "shujcount": "0"}
        # dumps是将dict转化成str格式，loads是将str转化成dict格式。
        # dump和load也是类似的功能，只是与文件操作结合起来了。dump为2个参数，第二个参数为文件对象

        con = requests.get("http://datachart.500.com/ssq/", data=json.dumps(data))
        print(con.status_code)
        return con

    def SaveContent(self, con):
        """
        保存响应返回的content
        :param con:
        :return:
        """
        f = open(SC_Data.FILEPATH, "w+")
        f.write(con.content)
        f.close()

    def BS_Parser(self, con):
        """
        解析文本内容，获取目标数据
        :param con: 返回的相应对象
        :return:
        """

        soup = BeautifulSoup(con.content, "lxml")
        num_pool = list(soup.body.find("tr", attrs={"id": "menuitem"}).children)
        for item in num_pool:
            if hasattr(item, "text"):
                self.num_pool.append(item.text)
        tr_every_cycle = list(soup.body.find("tbody", attrs={"id": "tdata"}).children)
        for tr in tr_every_cycle:
            appear_counts = []
            key = None
            for td in tr:
                if td.has_attr("class"):
                    appear_counts.append(str(td.text))
                elif td.has_attr("align"):
                    key = td.text
            if key:
                self.historyData[key] = appear_counts
        print self.num_pool


if __name__ == "__main__":
    item = HistoryDC()
    c = item.WebConnection()
    item.BS_Parser(c)
