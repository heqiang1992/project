# 建立服务其接受客户端信息，服务器端返回一个欢迎消息即结束。
import socket
import os
import sys
import signal
# def kill(pid):
#     try:
#         a = os.kill(pid, signal)
#         # a = os.kill(pid, signal.9) #　与上等效
#         print('已杀死pid为%s的进程,　返回值是:%s' % (pid, a))
#     except OSError as e:
#         print('没有如此进程!!!')
# kill(9999)
# server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# localhost = socket.gethostname()
# port=9999
# server_socket.bind((localhost,port))
# server_socket.listen(5)
#
# while True:
#     #建立客户端连接
#     client_socket,addr = server_socket.accept()
#     print("连接地址为：%s"%str(addr))
#     msg = "欢饮你！！！"
#     client_socket.send(msg.encode("utf-8"))
#     client_socket.close()
# 客户端现在我们进行优化，需求是客户端可以不停的向服务器发送信息，服务器接收后打印出来，当输入quit时，通信结束。
import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
localhost = socket.gethostname()
port=9999
server_socket.bind((localhost,port))
server_socket.listen(5)
while True:
    #建立客户端连接
    client_socket,addr = server_socket.accept()
    print("连接地址为：%s"%str(addr))
        #接收消息
    while True:
        str = client_socket.recv(1024)
        if str.decode() == "quit":
            print("server quiting......")
            client_socket.close()
            break
        else:
            print(str.decode("utf-8"))
# 另外再思考下，怎么实现互相可以发信息并接收。
# 利用多线程
# import socket
# import threading
# server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# localhost = socket.gethostname()
# port=9999
# server_socket.bind((localhost,port))
# server_socket.listen(5)
# def input():
#     while True:
#         #建立客户端连接
#         print("hello monster")
#         client_socket,addr = server_socket.accept()
#         print("input连接地址为：%s"%str(addr))
#         #接收消息
#         while True:
#             str = client_socket.recv(1024)
#             if str.decode() == "quit":
#                 print("server quiting......")
#                 client_socket.close()
#                 break
#             else:
#                 print(str.decode("utf-8"))
# def output():
#     print("hello stranger")
#     while True:
#         #建立客户端连接
#         client_socket,addr = server_socket.accept()
#         print("output连接地址为：%s"%str(addr))
#         msg = input("发送信息：")
#         client_socket.send(msg.encode("utf-8"))
#         client_socket.close()
#
# receive = threading.Thread(target=input).start()
# send = threading.Thread(target=output).start()
