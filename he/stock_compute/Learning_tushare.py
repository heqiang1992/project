#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tushare as ts

# http://tushare.org/trading.html
# 历史行情使用Tushare Pro新接口

# 日线daily接口实例
pro = ts.pro_api()
df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
# 或
df = pro.query('daily', ts_code='000001.SZ', start_date='20180701', end_date='20180718')
# 通过日期取历史某一天的全部历史
df = pro.daily(trade_date='20180810')

# 周线weekly接口实例
pro = ts.pro_api()
df = pro.weekly(ts_code='000001.SZ', start_date='20180101', end_date='20181101',
                fields='ts_code,trade_date,open,high,low,close,vol,amount')
# 或
df = pro.weekly(trade_date='20181123', fields='ts_code,trade_date,open,high,low,close,vol,amount')

# 月线monthly接口实例
pro = ts.pro_api()

df = pro.monthly(ts_code='000001.SZ', start_date='20180101', end_date='20181101',
                 fields='ts_code,trade_date,open,high,low,close,vol,amount')
# 或
df = pro.monthly(trade_date='20181031', fields='ts_code,trade_date,open,high,low,close,vol,amount')
