# import time
# import datetime
# import 基础.函数
# import pprint
# #查询但前时间是今年的第几个小时
# ticks1 = time.time()
# print("当前时间戳为：",ticks1)
# localtime = time.localtime(time.time())
# print(localtime)
# local_time = time.asctime(localtime)
# print(local_time)
# 基础.函数.judge("haha")
# local_time2 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# print(local_time2)
# day = time.strftime("%j",time.localtime())
# hour = time.strftime("%H",time.localtime())
# sum = (int(day)-1)*24 + int(hour)
# print(sum)
# #2.时钟
# while True:
#     time.sleep(1)
#     local_time2 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#     print("\r%s"%local_time2,end="")
# import HE.封装与继承
# A = HE.封装与继承.calculate("5 / 2")
# A.calculation()