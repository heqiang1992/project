'''
r = input("请输入半径：")
R = float(r)
long =3.1415926*2*R
area =pow(R,2)*3.1415926
print("周长为：%s"%long)
print("面积为：%s"%area)

a = int(input("请输入数字a："))
b = int(input("请输入数字b："))
c = (a+b)*(a-b)
print(c)

d = pow(a,b)/b
D = int(d)
print(D)
'''
'''
var1 = 'yo,man!'
var2 = 'wawawa!'
var3 = len(var1)
print(var3)
var3 = var2.count("a",0,len(var2))
print(var3)
'''
#字符串内建函数
'''
var3 = var2.capitalize()#大写首字母
print(var3)
var3 = var2.center(20,"=")#居中并筹齐字符长度
print(var3)
var3 = var1.find(",", 0 , len(var1))#查找字符中的位置
print(var3)
var3 = var1.replace(",","yoyo",1)#替换
print(var3)
var3 = var2.split("a",1)#分开
print(var3)
'''
var ='yo,man!what`s up!yo,man!what`s up!'
result = var.count("what",0,len(var)) #统计出现次数
print(result)
result = var.split("ha",2)#以ha为准分开两边，2次
print(result)
result = var[2:12]
Result = result.isdigit()#判断是否有数字
print(Result)
print('hello'+ result)
result = max(var)
print("nihao   "+result)
result = var.find("w",8,len(var))
print (result)
print("\"")