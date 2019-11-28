#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import win32com.client
import pyttsx3



mession = {"1": "五分钟快到了", "2": "10分钟快到了", "3": "15分钟快到了"}
pre_warning_set = 30  # unit :second


class TIMER():

    def __init__(self):
        self.read_mession()
        # self.speaker=win32com.client.Dispatch("SAPI.SpVoice")
        self.engine = pyttsx3.init()
    def read_mession(self):
        self.time_list = mession.keys()

    def start(self):
        timestamp_start = time.time()
        for point in self.time_list:
            while True:
                now=time.time()
                difference =int(point)*60-(now - timestamp_start)
                if difference > 0 and difference < pre_warning_set :
                    self.attention(point)
                    break
                elif difference < 0:
                    break
                time.sleep(10)

    def attention(self,point):
        print(mession[point])
        # self.speaker.Speak("hello")
        self.engine.say('中文')
        self.engine.runAndWait()
        # self.engine.startLoop()
        # self.engine.endLoop()

if __name__ == "__main__":
    a = TIMER()
    a.start()