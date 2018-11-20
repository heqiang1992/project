import socket
import threading
# chat_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# port = 9999
# chat_client.connect(("127.0.0.1",port))
# def receive(chat_client):
#     while True:
#         msg = chat_client.recv(1024)
#         print(msg.decode())
# threading.Thread(target=receive,args=(chat_client,)).start()
# while True:
#     str = input()
#     chat_client.send(str.encode("utf-8"))
import HE.日志记录与数据库存储
class client:
    def __init__(self,client_addr,client_port):
        self.__client_addr = client_addr
        self.__client_port = client_port
        self.__chat_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__chat_client.connect((self.__client_addr,self.__client_port))
        self.__run()
    def __receive(self,client):
        print("start receive....")
        while True:
            msg = client.recv(1024)
            print(msg.decode())
    def __send(self):
        while True:
            str = input()
            self.__chat_client.send(str.encode("utf-8"))
            if str == "bye bye":
                self.__chat_client.close()
                break
            if str == "SHOW":
                HE.日志记录与数据库存储.show_record()
    def __run(self):
        threading.Thread(target=self.__receive,args=(self.__chat_client,)).start()
        threading.Thread(target=self.__send).start()

client1 = client("127.0.0.1",9999)

