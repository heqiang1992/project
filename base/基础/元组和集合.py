# tuple1 = ("t","u","a")
# print(tuple1.index("u",0,len(tuple1)))
# print(tuple1+(4,8))
# print(len(tuple1))
# print(tuple1[1:6])
#
# tuple2 = (1,16,8,3)
# print(tuple1+tuple2)
# print(max(tuple1),max(tuple2))
#
# list1 = ["f","u","fo"]
# print(tuple1+tuple(list1))
# set1 = {1,5,2,3,4}
# weiya = set([3,5,7,8,8,0])
# print(set1)
# s3 = {4,32,46,11,32}
# s2 = {4,32,46,11,"aa"}
# s1 = {32,5,"c",32,11}
# print(s3)
# print(s2)
# print(s1)
# a = s1|s2
# print("a:",a)
# b = s1^s2
# print("b:",b)
# c = s1&s2
# print("c:",c)
# d = s1-s2
# print("d:",d)
dict1 = {1:4,2:6,6:"ttt",3:"1dd"}
dict1["yoyo"]=4
print(dict1)
del dict1[2]
dict1[6]= "wawawa"
print(dict1)
dic1 = {"name":'zhangsan',"age":25}
dic2 = {"name":'lisi',"age":29}
list = [dic1,dic2]
dic3 = {"name":"wang","age":30}
list.append(dic3)
list[2]["age"] = 24
print(list)
print(list[0].keys())
dic1.update(dict1)
print(dic1)
