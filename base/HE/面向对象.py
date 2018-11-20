# 1.面向对象概念，和面向过程区别。
#面向过程：将目的实现的过程一步一步划分步骤化的编程过程
#面向对象：将属性及其操作封装于类中，对象通过实例化继承类。特点：封装，集成，类
def add(a,b):           #面向过程
    return a+b
def minus(a,b):
    return a-b
print(add(5,2))
print(minus(5,2))

class operation():       #面向对象
    def __init__(self,a,b):
        self.first = a
        self.second = b
    def add(self):
        result = self.first+self.second
        print(result)
    def minus(self):
        result = self.first-self.second
        print(result)
f = operation(5,7)
f.add()
f.minus()
# 2.类和对象。
#类：包含对象相同的属性和方法的集合。 模板
#对象：继承类的属性和方法的实例。     实体
# 3.定义一个类。类成员有哪些？
class define_class:
    A = "类变量"
    def __init__(self):  #构造方法
        self.a = "成员变量"
    def other(self):   #成员方法
        b = "局部变量"
        self.c= "不是成员变量"
#   ...
    #类成员包括：变量和方法 （属性和行为）
# 4.实例化、调用成员的语句。
#a = define_class()  # 实例化 a
#a.other()  #调用成员方法
# 5.什么是构造方法，用法，作用。
#构造方法：初始化对象
#构造方法的作用：在构造方法中初始化成员变量，将共同属性集中变现。
'''
class test:
    def __init__(self,a):
        self.name = a
# 6.类的静态方法。
#参数列表内没有self的方法
class test:
    def __init__(self,a):
        pass
    def static():
        pass
'''
# 7.self的用法和意义。
    #self指对象本身
    #self.属性
# 8.成员私有化。
    #加双下滑线
    #只能在类的内部使用，对外隐藏。
# 9.和普通函数的比较。
    #类方法就是封装在类中的函数。
    #访问时：1、类名.方法名     2、函数名

# 定义一个学生类。有下面的类属性：
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高分数的课程。get_course()
# 4 返回该学生的平均成绩get_avg()
class student:
    def __init__(self,name,age,chinese,math,english):
        self.__name = name
        self.__age = int(age)
        self.__chinese = int(chinese)
        self.__math = int(math)
        self.__english = int(english)
    def get_name(self):
        print(self.__name)
    def get_age(self):
        print(self.__age)
    def get_course(self):
        if self.__chinese > self.__math and self.__chinese > self.__english:
            print("分数最高的是语文",self.__chinese,"分")
        elif self.__math > self.__chinese and self.__math > self.__english:
            print("分数最高的是数学",self.__math,"分")
        else:
            print("分数最高的是英语",self.__english,"分")
    def get_avg(self):
        avg = (self.__math+self.__english+self.__chinese)/3
        print(avg)
a = student("a",24,76,45,90)
a.get_age()
a.get_course()
a.get_avg()
class student2:
    def __init__(self,*info):
        self.dic = {"语文":info[2],"数学":info[3],"外语":info[4]}

    def get_max(self):
        str = max(self.dic,key=self.dic.get)
        print(str)
    def get_avg(self):
        avg =(self.dic["语文"]+self.dic["数学"]+self.dic["外语"])/3
        print(avg)
a = student2("张三",24,65,33,21)
a.get_max()
a.get_avg()
