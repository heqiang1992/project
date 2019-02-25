#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
import datetime

TIMESTAMP = str(int(time.time()))
FILEPATH = os.path.join(os.getcwd(), TIMESTAMP+".html")
PNGPATH = os.path.join(os.getcwd(), TIMESTAMP+".png")