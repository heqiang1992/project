#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import requests
import json
from he.weibo import SC_Data
from bs4 import BeautifulSoup


class HistoryDC(object):

    def __init__(self):
        print "double color start..."
        con = self.WebConnection()
        self.BS_Parser(con)
        self.this_issue = self.get_issue()
        self.generate_pool()

    def get_issue(self):
        issue_list = [int(x) for x in self.disappear_count.keys()]
        issue_list.sort(reverse=True)
        return int(issue_list[0]) + 1

    def WebConnection(self):
        """
        建立爬虫连接
        :return: 连接对象
        """
        data = {"expect": "50", "from": "0", "to": "0", "shujcount": "0"}
        # dumps是将dict转化成str格式，loads是将str转化成dict格式。
        # dump和load也是类似的功能，只是与文件操作结合起来了。dump为2个参数，第二个参数为文件对象

        con = requests.get("http://datachart.500.com/ssq/", data=json.dumps(data))
        # print(con.status_code)
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
        self.num_pool = []
        self.disappear_count = {}
        self.history_bingo = {}
        self.history_statistic = {}
        soup = BeautifulSoup(con.content, "lxml")
        num_pool = list(soup.body.find("tr", attrs={"id": "menuitem"}).children)
        for item in num_pool:
            if hasattr(item, "text"):
                self.num_pool.append(item.text.encode("utf-8"))
        tr_every_cycle = list(soup.body.find("tbody", attrs={"id": "tdata"}).children)
        # 获取出现记录和miss数
        for tr in tr_every_cycle:
            disappear_counts = []
            bingo_num = []
            key = None
            for td in tr:
                if isinstance(td, unicode):
                    continue
                elif td.has_attr("class"):
                    if td["class"] != ["yl01"] and td["class"] != ["yl02"]:
                        disappear_counts.append("0")
                        bingo_num.append(int(td.text.encode("utf-8")))
                    else:
                        disappear_counts.append(int(td.text.encode("utf-8")))
                elif td.has_attr("align"):
                    key = td.text.encode("utf-8")
            if key:
                self.disappear_count[key] = disappear_counts
                self.history_bingo[key] = bingo_num

        statistic_demo = list(soup.body.find("table", attrs={"id": "chartsTable"}).children)
        name_list = {'\xb3\xf6\xcf\xd6\xd7\xdc\xb4\xce\xca\xfd': 'total_appear',
                     '\xc6\xbd\xbe\xf9\xd2\xc5\xc2\xa9\xd6\xb5': 'average_miss',
                     '\xd7\xee\xb4\xf3\xc1\xac\xb3\xf6\xd6\xb5': 'max_continue',
                     '\xd7\xee\xb4\xf3\xd2\xc5\xc2\xa9\xd6\xb5': 'max_miss'}
        for tr in statistic_demo:
            # 获取统计数
            if isinstance(tr, unicode) or tr.has_attr("id") or tr.has_attr("colspan"):
                continue
            else:
                pail = []
                for td in tr.children:
                    if isinstance(td, unicode):
                        continue
                    elif td.has_attr("align") and not td.has_attr("bgcolor"):
                        unic = td.text.replace(u"\xa0", u"")
                        key = unic.encode("gbk")
                    elif td.has_attr("class") and not td.has_attr("bgcolor"):
                        pail.append(td.text.encode("utf-8"))
                    elif not td.has_attr("class"):
                        pail.append(td.text.encode("utf-8"))
                if key in name_list.keys():
                    key_en = name_list[key]
                    self.history_statistic[key_en] = pail
        return True

    def generate_pool(self):
        print "start compute"
        self.red_pool = []
        self.blue_pool = []
        # 根据出现次数添加球数
        for index, values in enumerate(self.history_statistic["total_appear"][:33]):
            index = index + 1
            if int(values) > 20:
                self.red_pool.extend([index for x in xrange(5)])
            else:
                self.red_pool.extend([index for x in xrange(30 - int(values))])
        for index, values in enumerate(self.history_statistic["total_appear"][33:]):
            index = index + 1
            if int(values) > 20:
                self.blue_pool.extend([index for x in xrange(5)])
            else:
                self.blue_pool.extend([index for x in xrange(30 - int(values))])

        # 平均遗漏值最小的5个数 + 2
        red_average_miss = [(index, values) for index, values in
                            enumerate(self.history_statistic["average_miss"][:33])]

        # 按出现次数升序排列
        def takeSecond(elem):
            return elem[1]

        red_average_miss.sort(key=takeSecond, reverse=False)
        for i in red_average_miss[:5]:
            index = i[0] + 1
            self.red_pool.extend([index for x in xrange(2)])

        blue_average_miss = [(index, values) for index, values in
                             enumerate(self.history_statistic["average_miss"][33:])]

        blue_average_miss.sort(key=takeSecond, reverse=False)
        for i in blue_average_miss[:5]:
            index = i[0] + 1
            self.blue_pool.extend([index for x in xrange(2)])

        # 最大遗漏值的5个数+1
        red_max_miss = [(index, values) for index, values in
                             enumerate(self.history_statistic["max_miss"][:33])]

        red_max_miss.sort(key=takeSecond, reverse=False)
        for i in red_max_miss[:5]:
            index = i[0] + 1
            self.blue_pool.extend([index])
        blue_max_miss = [(index, values) for index, values in
                             enumerate(self.history_statistic["max_miss"][33:])]

        blue_max_miss.sort(key=takeSecond, reverse=False)
        for i in blue_max_miss[:5]:
            index = i[0] + 1
            self.blue_pool.extend([index])

        # 近5期每期遗漏值最大 + 2%
        # self.disappear_count

        random.shuffle(self.red_pool)
        random.shuffle(self.blue_pool)
        return self.red_pool, self.blue_pool

    def compute(self, times=1):
        print "本期期号：%s. 推荐买：" % self.this_issue
        for i in xrange(times):
            bingo_list = []
            while len(bingo_list) < 6:
                ball = random.choice(self.red_pool)
                if ball in bingo_list:
                    continue
                bingo_list.append(ball)
            bingo_list.sort(reverse=False)
            bingo_list.append(random.choice(self.blue_pool))
            bingo_str = ""
            for num in bingo_list:
                bingo_str += str(num) + "   "
            print bingo_str

        return True


if __name__ == "__main__":
    item = HistoryDC()
    item.compute(times=5)
