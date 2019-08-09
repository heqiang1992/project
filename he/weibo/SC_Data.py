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

weiboAPP = [{"USER": "18230036107",
             "PWD": "569247yq", "APP_KEY": "994118618",
             "APP_SECRET": "5a2573b2e5a597741561ec3ec46d9a86",
             "CALLBACK_URL": "https://api.weibo.com/oauth2/default.html"},
            {"USER": "651828863@qq.com",
             "PWD": "zhuanshuhe0308", "APP_KEY": "994118618",
             "APP_SECRET": "5a2573b2e5a597741561ec3ec46d9a86",
             "CALLBACK_URL": "https://api.weibo.com/oauth2/default.html"}
            ]


# {"USER": "18230036107",
#              "PWD": "569247yq", "APP_KEY": "3961458989",
#              "APP_SECRET": "5d1c3ba0318b6ca5447b016436267872",
#              "CALLBACK_URL": "https://api.weibo.com/oauth2/default.html"},
#             {"USER": "651828863@qq.com",
#              "PWD": "zhuanshuhe0308", "APP_KEY": "994118618",
#              "APP_SECRET": "5a2573b2e5a597741561ec3ec46d9a86",
#              "CALLBACK_URL": "https://api.weibo.com/oauth2/default.html"}