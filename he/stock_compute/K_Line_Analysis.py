#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
import tushare as ts
import datetime
import time


class K_Rich():

    def __init__(self):
        token = "e7c38cff0d4898d24330567100b0328848f7f6333f160db8a6f77878"
        ts.set_token(token)
        self.pro = ts.pro_api()

    def get_stock_data(self, num):
        self.df = ts.get_k_data(num)
        self.df.index = pd.to_datetime(self.df.date)
        self.df.drop("date", axis=1, inplace=True)

    def daily_analysis(self, ts_code, start_date, end_date):

        df = self.pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date, )
        # 将数据的index转换成date字段对应的日期 df.index = pd.to_datetime(df.trade_date, format="%Y%m%d")
        df = df.set_index("trade_date")
        d1 = df.iloc[0]
        d2 = df.iloc[1]
        summary = ""
        return summary

    def date_day_stamp(self, day="today", delta=None):
        """

        :param day: today or yesterday
        :param delta: int
        :return:
        """
        timestamp = datetime.datetime.fromtimestamp(time.time())
        if day == "yesterday":
            timestamp = timestamp + datetime.timedelta(days=-1)
        if delta:
            timestamp = timestamp - datetime.timedelta(days=delta)
        date = datetime.datetime.strftime(timestamp, "%Y%m%d")
        return date

    def compute_two_series(self, series1, series2):
        """

        :param series1:
        :param series2: older time
        :return:
        """
        summary = {}
        if series1["close"] > series2["close"]:
            summary["price"] = "UP"
        elif series1["close"] == series2["close"]:
            summary["price"] = "TIE"
        else:
            summary["price"] = "DOWN"

    def k_strategy(self, series):
        if series["close"] > series["open"]:
            color = "red"
            entity = series["close"] - series["open"]
        elif series["close"] == series["open"]:
            color = "gray"
            entity = 0
        else:
            color = "green"
            entity = series["open"] - series["close"]
        if series["low"] < series["close"]:
            shadow_bottom = series["close"] - series["low"]
        if series["low"] < series["close"]:
            shadow_head = series["open"] - series["high"]



t = K_Rich()
end_date = t.date_day_stamp(day="yesterday")
start_date = t.date_day_stamp(day="yesterday", delta=10)
t.daily_analysis(ts_code="000725.SZ", start_date=start_date, end_date=end_date)
