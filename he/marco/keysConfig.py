#!/usr/bin/env python
# -*- coding: utf-8 -*-

#A##D*F*G*H##0.2*0.2*0.5*0.7



import os

def keysConfig():
    config={}
    filename = os.path.join(os.getcwd(),"config.l")
    f = open(filename,"a+")
    for line in f.readlines():
        l=line.split("##")
        type_inter = map(lambda x : x.split("*"),l[1:])
        config[l[0]] = {"typeKey":type_inter[0],"interval":type_inter[1]}
    return config
