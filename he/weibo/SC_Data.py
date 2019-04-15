#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
import datetime

# 时间戳生成文件名
TIMESTAMP = datetime.datetime.fromtimestamp(time.time())
DATE = datetime.datetime.strftime(TIMESTAMP, "%Y%m%d%H%M%S")
DATE = str(DATE).replace(" ", "_")
FILEPATH = os.path.join(os.getcwd(), DATE + ".html")
PNGPATH = os.path.join(os.getcwd(), DATE + ".png")
