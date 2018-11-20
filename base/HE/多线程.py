# import threading
# import time
# def print_info(name,delay):
#     for i in range(5):
#         print("I am",name)
#         time.sleep(delay)
# t1 = threading.Thread(target=print_info,args=("treading1",2))
# t2 = threading.Thread(target=print_info,args=("同时进行的treading2",3))
# t1.start()
# t2.start()
# 1.打开一个文件，对一个文件循环写入1000次，每次1条数据，统计所用时间。
# import threading
# class deal_file:
#     def __init__(self):
#         pass
#     def write(self):
#         import time
#         begin = time.time()
#         op_file = open("D:\\a.txt","a+")
#         for i in range(50):
#             op_file.write("hello!   ")
#             print("正在写入。。。")
#             time.sleep(1)
#         op_file.close()
#         end = time.time()
#         time = begin - end
#         print("这个写入线程耗时",time)
#     def write2(self):
#         import time
#         begin = time.time()
#         op_file = open("D:\\a.txt","a+")
#         for i in range(50):
#             op_file.write("BYE !   ")
#             print("正在写入BYE")
#             time.sleep(1)
#         op_file.close()
#         end = time.time()
#         time = begin - end
#         print("这个写入线程耗时",time)
#     def thread_run(self):
#         t1=threading.Thread(target=self.write())
#         t1.start()
#         t2=threading.Thread(target=self.write2())
#         t2.start()
# T1 = threading.Thread(target=deal_file().write())
# T1.start()
# T2 = threading.Thread(target=deal_file().write2())
# T2.start()
# 2.对上面的例子，开启10个线程，每个线程分别写100次，每次1条数据，统计时间后和上面的例子对比。

import threading
class deal_file:
    def __init__(self):
        pass
    def write(self):
        import time
        begin = time.time()
        op_file = open("D:\\b.txt","a+")
        for i in range(5):
            op_file.write("这是第%s行"%i+"\n")
            time.sleep(1)
            print(i)
        op_file.close()
        end = time.time()
        time = begin - end
        print("这个写入线程耗时",time)
    def threading(self):
        for i in range(10):
            threading.Thread(target=self.write).start()
a = deal_file()
a.threading()
    # def write2(self):
    #     import time
    #     begin = time.time()
    #     op_file = open("D:\\a.txt","a+")
    #     for i in range(5):
    #         op_file.write("BYE !   ")
    #         time.sleep(1)
    #         print(i)
    #     op_file.close()
    #     end = time.time()
    #     time = begin - end
    #     print("这个写入线程耗时",time)

# a = deal_file()
# T1 = threading.Thread(target=a.write).start()
# T2 = threading.Thread(target=a.write).start()
'''
def write(delay):
        import time
        begin = time.time()
        op_file = open("D:\\b.txt","a+")
        for i in range(5):
            op_file.write("hello!   ")
            time.sleep(delay)
            print(i)
        op_file.close()
        end = time.time()
        time = begin - end
        print("这个写入线程耗时",time)
T3 = threading.Thread(target=write,args=(1,)).start()
T4 = threading.Thread(target=write,args=(2,)).start()
# arg是跟的一个元组，单个参数后需接个“，”。
'''
# import time
# import  threading
# class deal_file:
#     def __init__(self,name):
#         self.name=name
#     def threading_file(self):
#         T1=time.time()
#         f=open(self.name,"a+")
#         for i in range(10):
#             threading.Thread(target=self.write_file,args=(f,)).start()
#         f.close()
#         T2=time.time()
#         return (T2-T1)
#     def write_file(self,f):
#         for i in range(100):
#             f.write("这是第%d行"%i+"\n")
# f=deal_file("d:\\c.txt")
# print(f.threading_file())


