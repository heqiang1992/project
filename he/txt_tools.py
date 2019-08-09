#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, sys, time
import threading
import re


def celect_data():
    data = []
    file_list = os.walk("D:\\ftp_root\\read\\tier+ssd\\")
    file_list = list(file_list)
    for file in file_list[0][-1]:
        path = os.path.join(str(file_list[0][0]),file)
        try:
            with open(path, "r") as f:
                string_demo = re.search("read: IOPS=\d+",f.read()).group(0)
                d = string_demo.split("=")[-1]
                data.append(d)
                print(d)
        except:
            print("err")
            continue
    ss = "\n".join(data)



if __name__ == "__main__":
    celect_data()