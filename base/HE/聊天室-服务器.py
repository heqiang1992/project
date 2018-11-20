import socket
import threading
#
# chat_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# port = 9999
# chat_server.bind(("127.0.0.1",port))
# chat_server.listen(5)
# connection_list = []
# def send():
#     for i in connection_list:
#         i[0].send(data_msg.encode("utf-8"))
# def chat_line(client_s):
#     global data_msg
#     while True:
#         msg = client_s.recv(1024)
#         for i in connection_list:
#             if client_s in i:
#                 num = connection_list.index(i)
#         print(msg.decode())
#         data_msg = str(connection_list[num][1])+":"+msg.decode()
#         send()
#         if msg.decode() == "quit":
#             client_s.close()
#             break
# while True:
#     client_s,addr = chat_server.accept()
#     print("连接地址为：%s"%str(addr))
#     #接受并返回信息
#     connection_list.append([client_s,addr])
#     threading.Thread(target=chat_line,args=(client_s,)).start()
import HE.日志记录与数据库存储
class server :
    def __init__(self,server_addr,server_port):
        self.__server_addr = server_addr
        self.__server_port = server_port
        self.__chat_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__chat_server.bind((self.__server_addr,self.__server_port))
        self.__chat_server.listen(5)
        self.__connection_list = []
        HE.日志记录与数据库存储.create_table()
        self.__accept_socket()
    def __send(self):
        for i in self.__connection_list:
            i[0].send(data_msg.encode("utf-8"))
    def __chat_line(self,client_s):
        global data_msg
        while True:
            msg = client_s.recv(1024)
            for i in self.__connection_list:
                if client_s in i:
                    num = self.__connection_list.index(i)
            if msg.decode() == "bye bye":
                HE.日志记录与数据库存储.log_in("%s leave"
                                     % str(self.__connection_list[num][1]), type="disconnect")
                client_s.close()
                break
            HE.日志记录与数据库存储.db_chat(str(self.__connection_list[num][1]),msg.decode())
            data_msg = str(self.__connection_list[num][1])+":"+msg.decode()
            HE.日志记录与数据库存储.log_in("said from:%s msg:%s"
                                 % (str(self.__connection_list[num][1]), msg.decode()), type ="receive", )
            self.__send()
    def __accept_socket(self):
        while True:
            client_s,addr = self.__chat_server.accept()
            HE.日志记录与数据库存储.log_in("connect_client :%s" % str(addr), type ="connect")
            print("有用户连接进：%s"%str(addr))
            #接受并返回信息
            self.__connection_list.append([client_s,addr])
            threading.Thread(target=self.__chat_line,args=(client_s,)).start()
chat_room = server("127.0.0.1",9999)
