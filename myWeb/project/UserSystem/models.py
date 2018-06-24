# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class user(models.Model):

    name = models.CharField(max_length=30)
    level = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    website = models.URLField()
    email = models.EmailField()


    def __unicode__(self):
        return self.name

class case(models.Model):

    caseName = models.CharField(max_length=100)
    caseID = models.CharField(max_length=100)
    # authors = models.ManyToManyField(Author)
    creater = models.ForeignKey(user)
    publication_date = models.DateField()

class case_report(models.Model):
    id_case_report = models.ForeignKey(case)
    authors = models.ManyToManyField(user)
    report = models.CharField(max_length=800)
"""
设置字段可选(选填)
blank=True

（DateField、TimeField、DateTimeField）或数字型（IntegerField、DecimalField、FloatField）字段为空，
你需要使用null=True * 和* blank=True。
"""

"""
@插入和更新数据
p = Publisher(name='Apress',
        address='2855 Telegraph Ave.',
        city='Berkeley',
        state_province='CA',
        country='U.S.A.',
        website='http://www.apress.com/')
p.save()
接下来再调用 save() 将不会创建新的记录，而只是修改记录内容（也就是 执行 UPDATE SQL语句，而不是 INSERT 语句）：
>>> p.name = 'Apress Publishing'
>>> p.save()
模型有一个自动增加的主键 id ，所以第一次调用 save() 还多做了一件事： 计算这个主键的值并把它赋值给这个对象实例
>>> p.id
52 

@选择对象
>>> Publisher.objects.all()
[<Publisher: Apress>, <Publisher: O'Reilly>]

@数据过滤
>>> Publisher.objects.filter(country="U.S.A.", state_province="CA")
[<Publisher: Apress>]
filter() 根据关键字参数来转换成 WHERE SQL语句

>>> Publisher.objects.filter(name__contains="press")
[<Publisher: Apress>]
在 name 和 contains 之间有双下划线,contains部分会被Django翻译成LIKE语句：
WHERE name LIKE '%press%';

@获取单个对象
>>> Publisher.objects.get(name="Apress")               #如果结果是多个对象，会导致抛出异常
<Publisher: Apress>

@数据排序
>>> Publisher.objects.order_by("name")                
[<Publisher: Apress>, <Publisher: O'Reilly>] 
#跟前面的 all() 例子差不多，SQL语句里多了指定排序的部分：ORDER BY name

@连锁查询
>>> Publisher.objects.filter(country="U.S.A.").order_by("-name")
[<Publisher: O'Reilly>, <Publisher: Apress>]
WHERE 和 ORDER BY 的组合：
WHERE country = 'U.S.A' ORDER BY name DESC;

注意，不支持Python的负索引(negative slicing)：
>>> Publisher.objects.order_by('name')[-1]

@更新多个对象
Django的save()方法更新了不仅仅是name列的值，还有更新了所有的列。 若name以外的列有可能会被其他的进程所改动的情况下，只更改name列显然是更加明智的。 
更改某一指定的列，我们可以调用结果集（QuerySet）对象的update()方法： 示例如下：

>>> Publisher.objects.filter(id=52).update(name='Apress Publishing')

>>> Publisher.objects.all().update(country='USA')
2                                                             
#update()方法会返回一个整型数值，表示受影响的记录条数。

删除对象
只需调用查询对象的delete()方法
>>> p = Publisher.objects.get(name="O'Reilly")
>>> p.delete()

>>> Publisher.objects.filter(country='USA').delete()
"""