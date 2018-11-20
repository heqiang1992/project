import sys
import traceback
d = ["dddd","ooo",3333]
print(d[1])
try:
    print(d[3])
except Exception as e :
    print(e)
print("继续run1")
try:
    s
except Exception as a :
    print(a)
print("继续run2")
try:
    print(d[3])
except Exception as d :
    print("OS error: {0}".format(d))
else:
    print("正确")
print("继续run3")
try:
    raise NameError('HiThere')
except:
     traceback.print_exc()




# import math
# print(math.asin(math.pi/8))
# import  random
# print(random.randrange(1,10))
# import os
# os.chdir('D:\heqiang\pythonstudy\基础')
# print(os.getcwd())
# # print(dir(math))
# import sys
# print(sys.argv)
#argv列表包含了传入脚本的所有参数


