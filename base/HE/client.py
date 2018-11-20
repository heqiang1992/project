#接受服务器消息
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # host = socket.gethostname()
# port=9999
# s.connect(("192.168.0.101",port))
# msg = s.recv(1024)
# s.close()
# print(msg.decode("utf-8"))
#向服务器发送信息
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# port=9999
# s.connect(("192.168.0.11",9999))
# while True:
#     str = input("发送信息：")
#     s.send(str.encode("utf-8"))
#     if str == "quit":
#         s.close()
#         quit("quiting...")
#         break
#互相发送信息
import threading
