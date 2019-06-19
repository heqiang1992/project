#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '16482528'
API_KEY = 'UDa5KcN5w4vZP7BWy3Z3GnA1'
SECRET_KEY = 'XpLIMwtRifUEudzarzhZ0qb8oZxosZGa'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('空山新雨后天气晚来秋', 'zh', 1, {
    'vol': 5,  # 音量
    'spd': 3,  # 语速
    'pit': 9,  # 语调
    'per': 3,  # 0：女 1：男 3：逍遥 4：小萝莉
})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)