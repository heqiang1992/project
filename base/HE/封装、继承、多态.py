#封装：就是隐藏对象的属性和实现细节，封装于类中，仅对外公开接口。
#计算器封装
'''
class calculate:
    def __init__(self):
        str = input("输入算式：")
        list = str.split(" ")
        self.first = int(list[0])
        self.operation = list[1]
        self.second = int(list[2])
        if self.operation == "+" :  #加
            print(self.__add())
        elif self.operation == "-" : #减
            print( self.__minus())
        elif self.operation == "*" : #乘
            print( self.__multi())
        elif self.operation == "/" and self.second != 0: #除
            print( self.__divide())
        else:
            print("错误")
    def __add(self):
        return self.first+self.second
    def __minus(self):
        return self.first-self.second
    def __multi(self):
        return self.first*self.second
    def __divide(self):
        return self.first/self.second
a = calculate()
'''
# 1.什么是继承，有何作用？
#继承：就是一个类继承另一个类的属性与方法。
#作用：减少重复的代码、提高类的耦合度。提高代码重用性，减少冗余。
# 2.编写三个类：person、teacher、student，
# teacher和student需继承于person，student需重写person中的make_money方法。
# class person:
#     def __init__(self,name):
#         self.name = name
#         # self.age = age
#     def make_money(self):
#         print("工资：很高")
# class teacher(person):
#     def career(self):
#         print("I am a teacher !")
# class student(person):
#     def career(self):
#         print("I am a student !")
#     def make_money(self):
#         print("工资：没有")
# a = teacher("haha")
# a.make_money()
# a.career()
# b = student("haha")
# b.make_money()
# b.career()
# 3.在上面的例子中另外再创建一个类class_room, class_room中有成员teacher和student对象，还有teach方法。（组合）
# T = teacher("老师一号")
# class class_room:
#     def __init__(self,t):
#         self.t = t
#         self.s = student("学生一号")
#         self.n = teacher("老师2号").name
#     def test(self):
#         self.s.career()
#         self.s.make_money()
#         print(self.n)
#         self.t.career()
#         self.t.make_money()
#         print(self.s.name)
#         print(self.t.career())
#         print(self.n)
# c = class_room(T)
# c.test()
# fil = open(".py")
# print(fil.name)
# str = fil.read(10)
# print(str)
# 1.对于多态的理解，举几个相关的例子说明具体哪些点展现了多态？
#多态：就是同一个接口，用不同的实例实现不同的功能。
#作用：好处在于提供系统的弹性，避免代码的僵化。
#1、+
#2、不定长参数，多态参数
#3、继承中方法重写
#4、
# 2.将一个数字反序输出，如123反序输出为321，类型不能改变。
# class num_trans:
#     def __init__(self):
#         self.num = int(input("输入一个数字："))
#     def transform(self):
#         str1 = str(self.num)
#         new_str = ""
#         for i in range(0,len(str1)):
#             new_str = str1[i] + new_str
#         print(int(new_str))
# k = num_trans()
# k.transform()
# 3.上例中，实现一个多态函数为data_reverse(data),支持将数字、字符串、列表
# 反序输出，要求不能使用reverse，sort等方法。
# def data_reverse(data):
#     # data = input("请输入：")
#     print("开始判断")
#     if isinstance(data,int):
#         trans_str = str(data)
#         print(int(trans_str[::-1]))
#     elif isinstance(data,str):
#         print(data[::-1])
#     elif isinstance(data,list):
#         print(data[::-1])
#     else:
#         pass
# data_reverse("abc")
class data_reverse:
    def __init__(self,data):
        self.data = data
    def judge(self):
        if isinstance(self.data,int):
            trans_str = str(self.data)
            print(int(trans_str[::-1]))
        elif isinstance(self.data,str):
            print(self.data[::-1])
        elif isinstance(self.data,list):
            print(self.data[::-1])
        else:
            pass
a = data_reverse([4,7,32,2,0])
a.judge()
# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
import selenium