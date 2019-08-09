#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, sys, time
import threading

ip_24 = "192.168.0."
ip_range = [3, 53]  # 要求同网段
STAF = "STAF hostIP PROCESS START SHELL COMMAND \"cmd\" SAMECONSOLE RETURNSTDOUT STDERRTOSTDOUT WAIT 2000"
cmd1 = "iozone -a -i 0 -Rb c:\\file\h.xls -f c:\\file\\testfile.txt -q 512K -s 10G -w"
cmd2 = "iozone -a -i 1 -Rb c:\\file\h.xls -f c:\\file\\testfile.txt -q 512K -s 10G -w"
d_cmd = "STAF hostIP fs DELETE ENTRY c:\\file\\hhh CONFIRM"
d_cmd2 = "STAF hostIP fs DELETE ENTRY c:\\STAF\\mytest.0.0 CONFIRM"
l_cmd = "STAF hostIP fs LIST DIRECTORY c:\\file\\"
fio = "fio -filename=c:\\file\\windows_batch_cmd.py --iodepth=4 --thread --rw=randread --bs=4K --numjobs=4 --runtime=300 --size=10G --group_reporting --name=mytest --output=c:\\file\\hhh.txt --direct=1"
d_cmd3 = "STAF hostIP fs DELETE ENTRY c:\\Users\\demo\mytest.8.0 CONFIRM"


def test_connection():
    fault = []
    success = []
    cmd = "ipconfig"
    a = STAF.replace("cmd", cmd)
    for i in range(ip_range[0], ip_range[1]):
        ip = ip_24 + str(i)
        b = a.replace("hostIP", ip)
        p = os.popen(b)
        if "Windows IP" in p.read():
            print(" %s connect success." % ip)
            success.append(ip)
        else:
            fault.append(ip)
            print(p.read())
    print("\n".join(fault))
    print("fault: %s" % str(len(fault)))
    print("success: %s" % str(len(success)))


def sned_demo(ip, i):
    a = STAF.replace("hostIP", ip)
    b = a.replace("cmd", fio)
    c = b.replace("hhh.txt", "%s.txt" % str(i))
    p = os.popen(c)
    #time.sleep(3)
    print(" %s send success." % ip)
    #print(p.read())


#    if "Run began" in p.read():
#        print " %s send success." % ip


def send_cmd():
    for i in range(ip_range[0], ip_range[1]):
        ip = ip_24 + str(i)
        t = threading.Thread(target=sned_demo, args=(ip, i))
        t.setDaemon(True)
        t.start()
    time.sleep(30)


def get_file():
    fault = []
    success = []
    cmd = "STAF LOCAL FS COPY FILE c:\\file\h.xls TODIRECTORY c:\\file\ TOMACHINE 192.168.0.53"
    a = STAF.replace("cmd", cmd)
    for i in range(ip_range[0], ip_range[1]):
        ip = ip_24 + str(i)
        b = a.replace("hostIP", ip)
        c = b.replace("h.xls", "%s.txt" % str(i))
        p = os.popen(c)


def delete_file():
    for i in range(ip_range[0], ip_range[1]):
        ip = ip_24 + str(i)
        b = d_cmd.replace("hostIP", ip)
        # p = os.popen(b)
        c = b.replace("hhh", "%s.txt"%str(i))
        print(c)
        p = os.popen(c)


def check_file():
    fault = []
    success = []
    for i in range(ip_range[0], ip_range[1]):
        ip = ip_24 + str(i)
        b = l_cmd.replace("hostIP", ip)
        p = os.popen(b)
        #        print p.read()
        if ".xls" in p.read():
            print(" %s file check success." % ip)
            success.append(ip)
        else:
            fault.append(ip)
    print("\n".join(fault))
    print("fault: %s" % str(len(fault)))
    print("success: %s" % str(len(success)))
    return len(success)


if __name__ == "__main__":
    if sys.argv[1] == "test":
        test_connection()
    elif sys.argv[1] == "start":
        send_cmd()
    elif sys.argv[1] == "get":
        get_file()
    elif sys.argv[1] == "delete":
        delete_file()
    elif sys.argv[1] == "check":
        for i in range(30):
            print("%s th check... " % str(i))
            num = check_file()
            if num == 50:
                print("done !!!!!!!!!!")
                break
            time.sleep(60)
