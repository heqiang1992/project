# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# if a > b :
#     print(a)
# else:
#     print(b)
# print("第二题：")
# if a > b and b > 20 :
#     print(a+b)
# elif a < b or a< 0 :
#     print(a-b)
# else:
#     print(a*b)
#输入一个字符，如果它是一个大写字母,则把它变成小写输出,如果是小写,则变成大写输出,其他字符不变输出。
# str = str(input("请输入一个字母："))
# if len(str) == 1 and str.isalpha():
#     if str.islower():
#         print("第一个：", str.upper())
#     elif str.isupper():
#         print("第二个：",str.lower())
# else:
#     print(str)
#     print("请输入单个字母")
#分别输入年、月、日，判断此日期是当年的第几天。
# y = int(input("输入年:"))
# m = int(input("输入月:"))
# d = int(input("输入日:"))
# mm = (0,31,59,70,100,131,161,192,213,243,274,304)
# if y in range(1900,2060) and m in (1,3,5,7,8,10,12) and d in range(1,32):
#     if y % 4 != 0 or y % 100 == 0 :
#         sum = d + mm[m-1]
#         print("第%d天"%sum)
#     elif m < 2 :
#         sum = d + mm[m-1]
#         print("闰年第%d天"%sum)
#     else:
#         sum = d + mm[m-1]
#         sum = sum + 1
#         print("闰年第%d天"%sum)
# elif y in range(1900,2060) and m in (4,6,9,11) and d in range(1,31):
#     if y % 4 != 0 or y % 100 == 0 :
#         sum = d + mm[m-1]
#         print("第%d天"%sum)
#     else:
#         sum = d + mm[m-1]
#         sum = sum + 1
#         print("闰年第%d天"%sum)
# elif y in range(1900,2060) and m ==2 and d in range(1,29):
#     if y % 4 != 0 or y % 100 == 0 and d in range(1,28):
#         sum = d + mm[m-1]
#         print("第%d天"%sum)
#     elif y % 4 == 0 or y % 100 != 0 :
#         sum = d + mm[m-1]
#         print("闰年第%d天"%sum)
#     else:
#         print("没有这一天")
# else:
#     print("不正确的日期！")
#1.打印99乘法表。
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,"   ",end="")
#     print(end="\n")
#2.一个10000以内整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？（提示：用到math模块）
# import math
# i = 0
# while i < 10000 :
#     t1 = i+100
#     t2 = i+268
#     s1 = math.sqrt(t1)
#     s2 = math.sqrt(t2)
#     if s1 % 1 == 0 and s2 % 1 == 0:
#         print(i)
#     i = i + 1
#3.输入三个整数x,y,z，请把这三个数由小到大输出。
# a = int(input("第一个数："))
# b = int(input("第二个数："))
# c = int(input("第三个数："))
# list = [a,b,c]
# new = []
# min = list[0]
# while len(list) > 0:
#     for i in range(0,len(list)):
#         if min > list[i]:
#             min = list[i]
#     s = list.index(min)
#     list.pop(s)
#     new[0] = min
# 4.求1000以内的水仙花数。
# 提示：如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
# i = 100
# while 100<= i < 1000 :
#     f = i % 10
#     s = ((i-f) % 100)/10
#     t = (i-s*10-f)/100
#     if i == pow(f,3)+pow(s,3)+pow(t,3):
#         print(i)
#     i = i+1
# 5.对3、65、22、102、4进行升序排序
list = [3,65,22,102,4]
# new = []
# j = 0
# for i in range(0,len(list)):
#     ob = list.index(min(list))
#     bd = min(list)
#     new.append(bd)
#     list.pop(ob)
#     j = + 1
# print(new)
#冒泡算法：
# for i in range(0,len(list)):
#     for j in range(0,len(list)-1-i):
#         if list[j] > list[j+1]:
#             t = list[j]
#             list[j] = list[j+1]
#             list[j+1] = t
# print(list)
#         求素数。
# for i in range(2,200):
#     sum = 0
#     for j in range(2,i):
#         if i % j == 0:
#             break
#         else:
#             sum = sum+1
# 6.猜数字游戏，系统随机生成一个1000以内的数字，用户输入一个数字，
# 如果输入数字大于系统数字则提示‘大了’，反之提示‘小了’，直到相等游戏结束，提示‘通关’
# 并输出猜测次数。（提示：用到random模块）
# import random
# r = random.randint(0,1000)
# i = int(input("请输入数字:"))
#     if sum == i-2:
#         print(i)
# while 1==1:
#     if i <0 or i >=1000 :
#         print("数字错误")
#         i = int(input("请输入数字:"))
#         continue
#     elif r > i :
#         print("小了")
#         i = int(input("请输入数字:"))
#         continue
#     elif r < i :
#         print("大了")
#         i = int(input("请输入数字:"))
#         continue
#     else:
#         print("通关")
#         break
s = str(input("请输入："))
a =""
for i in range(0,len(s)):
    a = s[i] + a
print(a)