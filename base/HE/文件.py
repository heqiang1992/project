# f = open('d:\\a.txt',"a+")
# f.write("test aaa")
# f.seek(0,0)
# print(f.read())

# f = open('d:\\a.txt',"a+")
# f.write("test aaa\n")
# # print(f.tell())
# # f.seek(0,0)
# # print(f.tell())
# # print(f.read())
# f.seek(0,0)
# line = f.readline()
# print(line)
# 1.对xampp中的apache日志文件（即所有.log结尾的文件）进行读取，筛选出其中的错误信息，
# 并全部输出到另一个文件new.log中。
#查找文件
# import os
# new_list = []
# address_list = os.listdir('C:\\Xampp\\apache\\logs')
# file_list = []
# for i in address_list:
#     if i.endswith('.log'):
#         file_list.append(i)
# #读取文件
# for name in file_list:
#     address_name = "C:\\Xampp\\apache\\logs\\"+name
#     this = open(address_name,'r+')
#     # print(this.readline())
# #转成字符串判断录入
#     for i in this.readlines():
#         if "error" in i :
#             new_list.append(i)
#     this.close()
# print(new_list)
# f = open("C:\\Xampp\\apache\\logs\\new_log","a+")
# for i in new_list:
#     f.write(i)
# f.close()
#类的写法:
# class find:
#     def __init__(self,address,suffix):
#         self.address =address
#         self.suffix =suffix
#         self.file_list=[]
#     def find(self):
#         import os
#         address_list = os.listdir(self.address)
#         for i in address_list:
#             if i.endswith(self.suffix):
#                 self.file_list.append(i)
#     def read(self):
#         for name in self.file_list:
#             address_name = self.address+"\\"+name
#             this = open(address_name,'r+')
#     def match(self):
#         for i in this.readlines():
#             if "error" in i :
#                 new_list.append(i)
#         this.close()
#     print(new_list)
#     f = open("C:\\Xampp\\apache\\logs\\new_log","a+")
#     for i in new_list:
#         f.write(i)
#     f.close()

# 2.编写一个函数read_file(name, begin_line,end_line),name为文件名，begin_line和end_line为默认值参数，
# 可以填写来控制读取的行数，最后结果需要返回一个列表，存放需要获取的所有行。
# def read_file(name,begin_line=0,end_line=0):
#     f = open(name,'r+')
#     if end_line ==0 or end_line > len(f.readlines()):
#         end_line = len(f.readlines())
#     list = []
#     f.seek(0,0)
#     for i in f.readlines():
#         list.append(i)
#     target_list = list[begin_line:end_line]
#     print(target_list)
# read_file("d:\\a.txt")
# 3.写一个程序，启动后有支持三种命令（WRITE\READ\QUIT），输入WRITE后可以不停的对文件进行写入操作，
# 输入READ可以获取文件所有内容，输入QUIT则退出程序
# def WRQ():
#     while True:
#         str = input("请输入：")
#         if str == "write":
#             file = open("d:\\a.txt",'a+')
#             continue
#         elif str == "read":
#             file.seek(0,0)
#             print(file.readlines())
#         elif str == "quit":
#             break
#         else:
#             file.write(str)
# WRQ()
# def WRQ2():
#     file = open("d:\\a.txt",'a+')
#     while True:
#         str = input("请输入：")
#         if str == "read":
#             file.seek(0,0)
#             print(file.readlines())
#         elif str == "quit":
#             break
#         else:
#             file.write(str)
#     file.close()
# def WRQ():
#     while True:
#         str = input("请输入：")
#         if str == "write":
#             break
#         else:
#             print("没有开始写入")
#     WRQ2()
# WRQ()
#将文件record.txt中的数据进行分割并按照以下规律保存：
#小甲鱼的会话保存到boy_*.txt
#小客服的会话保存到girl_*.txt
file = open("d:\\record.txt","r")
boy = open("d:\\boy.txt","a+")
girl = open("d:\\girl.txt","a+")
for line in file.readlines():
    if "小甲鱼" in line:
        boy.write(line)
    elif "小客服" in line:
        girl.write(line)
file.close()
boy.close()
girl.close()
