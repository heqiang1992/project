# -*- coding:utf-8 -*-
__autthor__ = "heqiang"

import paramiko, socket, telnetlib, ftplib
import time, os, re, sys, datetime

waitList = [":~ #", ":/>"]


class Connection(object):

    def __init__(self, host, username, password, port=22):
        pass
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.channel = self.__createChannel()

    def __createChannel(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))  # tuple
        self.ssh = paramiko.Transport(sock)
        self.ssh.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.ssh)

        channel = self.ssh.open_session()
        channel.get_pty(width=200, height=200)
        channel.invoke_shell()
        channel.settimeout(5)
        self.__receive(channel)
        return channel

    def __send(self, channel, cmd):
        if not channel.active:
            raise Exception("CONNECT CLOSED")
        return channel.send(cmd + "\n")

    def __receive(self, channel):
        info = []
        while True:
            try:
                res = channel.recv(1024)
            except Exception as e:
                print(e)
                break
            res = res.decode("utf-8")
            info.append(res)
            for waitStr in waitList:
                if re.search(waitStr, res):
                    break
        p = "".join(info)
        print(p)
        # self.log.info(p)

    def exe_cmd(self, cmd):
        self.__send(self.channel, cmd)
        self.__receive(self.channel)

    def sftp_get(self, server_path, local_path):
        self.sftp.get(server_path, local_path)


if __name__ == "__main__":
    ip = input("输入IP：")
    user = "root"
    password = "daemon"
    TIMESTAMP = datetime.datetime.fromtimestamp(time.time())
    DATE = datetime.datetime.strftime(TIMESTAMP, "%Y%m%d%H%M%S")
    DATE = str(DATE).replace(" ", "_")
    print("选择获取日志：\n1.打包所有日志。\n2.cinder-volume\n3.nova-comupte\n4.hyhive-lib\n5.messages\n6.自定义")
    select = input("choose:")
    if select == "1":
        FILENAME = ip.replace(".", "_") + "-" + DATE + ".tgz"
        FILEPATH = os.path.dirname(__file__) + os.sep + FILENAME  # 本地位置
        cmd = 'tar -czf /root/%s /var/log/ --exclude=/var/log/ceph --exclude=/var/log/infinity --exclude=/var/log/httpd --exclude=/var/log/*.gz --exclude=/var/log/hyhive/*.log.* --exclude=/var/log/audit --exclude=/var/log/sa --exclude=/var/log/keystone --exclude=/var/log/cluster --exclude=/var/log/nova/*.gz --exclude=/var/log/neutron/*.gz ' % (
            FILENAME)
        i = Connection(ip, user, password, 22)
        i.exe_cmd(cmd)
        time.sleep(5)
    elif select == "2":
        FILENAME = "cinder-volume"+"_" + ip.replace(".", "_") + "-" + DATE + ".log"
        FILEPATH = os.path.dirname(__file__) + os.sep + FILENAME
        cmd = 'cp /var/log/cinder/volume.log  /root/%s' % (FILENAME)
        i = Connection(ip, user, password, 22)
        i.exe_cmd(cmd)
        time.sleep(3)
    elif select == "3":
        FILENAME = "nova-comupte"+"_" + ip.replace(".", "_") + "-" + DATE + ".log"
        FILEPATH = os.path.dirname(__file__) + os.sep + FILENAME
        cmd = 'cp /var/log/nova/nova-compute.log  /root/%s' % (FILENAME)
        i = Connection(ip, user, password, 22)
        i.exe_cmd(cmd)
        time.sleep(3)
    elif select == "4":
        FILENAME = "hyhive-lib"+"_" + ip.replace(".", "_") + "-" + DATE + ".log"
        FILEPATH = os.path.dirname(__file__) + os.sep + FILENAME
        cmd = 'cp /var/log/hyhive/hyhive-lib.log  /root/%s' % (FILENAME)
        i = Connection(ip, user, password, 22)
        i.exe_cmd(cmd)
        time.sleep(3)
    elif select == "5":
        FILENAME = "messages"+"_" + ip.replace(".", "_") + "-" + DATE + ".log"
        FILEPATH = os.path.dirname(__file__) + os.sep + FILENAME
        cmd = 'cp /var/log/messages  /root/%s' % (FILENAME)
        i = Connection(ip, user, password, 22)
        i.exe_cmd(cmd)
        time.sleep(3)
    elif select == "6":
        dir = input("/var/log/:")
        FILENAME = dir.split("/")[-1]+"_" + ip.replace(".", "_") + "-" + DATE + ".log"
        FILEPATH = os.path.dirname(__file__) + os.sep + FILENAME
        cmd = 'cp /var/log/%s  /root/%s' % (dir,FILENAME)
        i = Connection(ip, user, password, 22)
        i.exe_cmd(cmd)
        time.sleep(3)
    else:
        raise Exception("wrong input !@#$%^&*")

    print("获取文件到：%s" % FILEPATH)
    i.sftp_get('/root/%s' % (FILENAME), FILEPATH)
    i.exe_cmd("rm -f %s"%(FILENAME))
    print("\ndone !!!")
    time.sleep(3)
