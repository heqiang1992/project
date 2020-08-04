#-*- coding:utf-8 -*-
__autthor__="heqiang"

import paramiko,socket,telnetlib,ftplib
import threading,os,re,sys
from log import log





class Client(object):

    def __init__(self):
        pass


        """
        # 另一个建立链接的方法，暂时放在这里先不写。
        ssh = paramiko.SSHClient()
        # 允许链接不在know_host文件中的主机
        ssh.connect(hostname="",port=22,username="",password="",timeout=5)
        cmd="who"
        stdin,stdout,stderr = ssh.exec_command(cmd)
        print(type(stdout))
        print(stdout.read())
        ssh.close()
        """



waitList = [":~ #",":/>"]

cmd=input("please input conmand :")

class Connection(object):

    log = log("c:\\log","test")

    def __init__(self,host,username,password,port=22):
        pass
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.channel = self.__createChannel()

    def __createChannel(self):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((self.host,self.port))  #tuple
        ssh = paramiko.Transport(sock)
        ssh.connect(username=self.username,password=self.password)

        channel = ssh.open_sesssion()
        channel.get_pty(width=200 ,height=200)
        channel.invoke_shell()
        channel.settimeout(10)
        self.__receive(channel)
        return  channel

    def __send(self,channel,cmd):
        if not channel.active:
            raise Exception("CONNECT CLOSED")
        return channel.send(cmd+"\n")
    def __receive(self,channel):
        info=[]
        while True :
            try:
                res = channel.recv(1024)
            except Exception as e:
                print (e)
                break
            info.append(re.decode("utf-8"))
            for waitStr in waitList:
                if re.search(waitStr,res):
                    break
        p = "".join(info)
        print(p)
        self.log.info(p)
        return p

    def exe_cmd(self,cmd):
        self.__send(self.channel,cmd)
        res = self.__receive(self.channel)
        return res


if __name__ == "__main__":
    cmd = raw_input("please input command :")
    i = Connection("8.46.11.22","22","root","huawei@123")
    i.exe_cmd("cmd")