#创建一个相加函数
# def add(a,b):
#     return a+b
# print(add(4,8))
#1+2+...+n的和
# def addNum():
#     n = int(input("输入一个数："))
#     i = 1
#     sum = 0
#     while i <= n :     #for i in (1,n+1):
#         sum = sum + i
#         i += 1
#     return sum
#
# print(addNum())
# 1.实现一个函数count(str,substr,[begin=0],[end=0]),
# 查找str中有多少个substr。只以字符串为例。
# def count(all,substr,begin,end):
#     str = all[begin:end]
#     num = str.split(substr)
#     return len(num)-1
# print(count("adabbagkg","a",0,7))

# all = input("请输入字符串：")
# def count(sub,begin=0,end=len(all)):
#     num = all.count(sub,begin,end)
#     return num
# print(count("a",2,7))
# 2.实现一个函数，支持传入任意多个整数进行加法运算，并返回结果。
# def sum(*var_tuple):
#     sum = 0
#     for i in var_tuple:
#         sum = sum +i
#     return sum
# a = sum(2,4,76,9,0,6)
# print(a)
#
# 3.实现一个简易计算器，根据用户输入执行相应的加、减、乘、除运算
# 例如用户输入'9 / 3',得出结果。每种运算请用单独的函数处理。
'''
str = str(input("输入算式："))
def divide():
    list1 = str.split("/",1)
    result = int(list1[0])/int(list1[1])
    return result
def mult():
    list1 = str.split("*",1)
    result = int(list1[0])*int(list1[1])
    return result
def minus():
    list1 = str.split("-",1)
    result = int(list1[0])-int(list1[1])
    return result
def add():
    list1 = str.split("+",1)
    result = int(list1[0])+int(list1[1])
    return result
if "/" in str :
    print(divide())
elif "*" in str:
    print(mult())
elif "+" in str:
    print(add())
elif "-" in str:
    print(minus())
'''
#用户在屏幕上循环输入，每输入一次，就以字符串的形式添加到列表中，当用户输入'quit'时，结束输入，打印整个列表。
#要求：添加列表元素的功能必须封装到一个函数中，用全局变量和局部变量各实现一次。
# def type_in():
#     list =[]
#     while True:
#         str = input("请输入信息：")
#         if str == "quit":
#             break
#         else:
#             list.append(str)
#             continue
#     for i in range(0,len(list)):
#         print("第",i+1,"次录入为：",list[i])
# type_in()
#全局变量
# def type_in2():
#     global list
#     list = []
#     while True:
#         str = input("请输入信息：")
#         if str == "quit":
#             break
#         else:
#             list.append(str)
#             continue
#     for i in range(0,len(list)):
#         print("第",i+1,"次录入为：",list[i])
# type_in2()
# print(list)
# def judge():
#     str = input()
#
# for i in range(0,len(str)):
#     if ord(str[i]) not in range(48,58):
#         if ord(str[i]) in (42,43,45,47):
#             if ord(str[i+1]) in (42,43,45,47):
#                 print("运算符号后只能接数字")
#                 str = input()

#建立lambda计算x的y次方。
# lam_1 = lambda x,y: pow(x,y)
# print(lam_1(3,3))
#2.实现一个函数，传入一个list后排序，并返回排序后的新list。
# def sort(*var_tuple):
#     '''
#     这是一个关于列表排序的函数
#     数值类型必须相同
#     '''
#     list1 = list(var_tuple)
#     list1.sort()
#     return list1
# print(sort(2,3,7,12,0,89,101))
# 编写一个函数，在函数内部对参数进行操作后打印值，同时在函数外也打印该参数的值。要求如下：
# 1.如果传入的是数字，则在函数内加1。
# 2.如果传入的是字符串，则在字符串后加‘1’。
# 3.如果传入的是列表，则在后加一个元素1。
def judge(sub):
    if type(sub) == list:
        new_list=[]
        new_list.extend(sub)
        new_list.append(1)
        print(new_list)
    elif isinstance(sub,int):
        sub = sub +1
        print(sub)
    else:
        sub = sub+"1"
        print(sub)
judge("gtr")