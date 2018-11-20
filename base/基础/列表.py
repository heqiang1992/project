'''
list = ["a1","a2","a3","a4"]
#list.append(obj) 在列表末尾添加新的对象
list.append("new")
print(list)
#list.count(obj) 统计某个元素在列表中出现的次数
sum = list.count("ddd")
print(sum)
#list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
list1 = [0,7,"哇"]
list.extend(list1)
print(list)
#list.index(obj) 从列表中找出某个值第一个匹配项的索引位置，索引从0开始
num = list.index(0,0,len(list))
print(num)
#list.insert(index, obj) 将对象插入列表
list.insert(2,"87v5")
print(list)
#list.pop(obj=list[-1]) 移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
list.pop(-2)
print(list)
#list.remove(obj) 移除列表中某个值的第一个匹配项
list.remove("b")
print(list)
#list.reverse() 反向列表中元素，倒转
list.reverse()
print(list)
#list.sort([func]) 对原列表进行排序
list.sort(key=lambda a:(a[1]))
'''
a = [23,56,89,"vv","tew","rr073"]
#1.创建一个包含字符串和数字的列表，打印出第3到5个元素，倒数第3个元素。
print(a[2],a[4])
#2.创建一个列表，将第3个元素更改为‘third’，输出整个列表。
a[2] = "third"
print(a)
#3.创建两个列表，将其连接后，打印出第倒数第3和倒数第2两个元素，并将其与一个新的列表相加后输出。
print(a[-3],a[-2])
list1 = [1,1,5]
list2 = [3,7,9]
list1.extend(list2)
a.append(list1[-3])
a.append(list1[-2])
print(a)
#4.创建一个列表，内部嵌套了3个列表
#a=['xiaoming','student',10],
#b=['xiaohong','coder',23],
#c=['xiaohuang','boss',35]，
#打印第2个列表的第1个元素，打印第3个列表的所有数据，删除第2个列表，打印整个大列表数据。
a=['xiaoming','student',10]
b=['xiaohong','coder',10]
c=['xiaohuang','boss',10]
list = [a,b,c]
print(list[1][0])
print(list[2])
del list[1]
print(list)
#5.将第4题中的大列表的末尾添加一个元素10。
#a) 将添加的元素通过列表打印出来。
#b）输出大列表中出现10这个元素的次数。
#c）输出第1个子列表中出现第一个元素‘10’的位置。
#d）对此列表进行反序输出。
#e）移除第2个子列表中的第3个元素，输出整个列表。
#f）移除整个列表中所有出现‘10’的元素并输出。
list.append(10)
print(list[-1])
num =list.count(10)
print(num)
num = list[0].index(10)
print(num)
list.reverse()
print(list)
list[2].remove(list[2][2])
print(list[2])
list[0] = 10
print(list)
for i in range(0,len(list)-1):
    if 10 == list[i]:
        list.remove(10)
for i in range(0,len(list)-1):
    if 10 in list[i]:
        list[i].remove(10)
print(list)