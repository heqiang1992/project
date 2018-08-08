# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class user_info(models.Model):
    user = models.ForeignKey(User,
                             related_name='user_info_user',)
    safe_question = models.CharField(max_length=60)
    answer = models.CharField(max_length=60)
    tel = models.CharField(max_length=20)
    info = models.URLField(blank=True, max_length=100)

    def __unicode__(self):
        return self.name


class case(models.Model):
    caseName = models.CharField(max_length=100)
    caseID = models.CharField(max_length=100)
    # authors = models.ManyToManyField(Author)
    # creater = models.ForeignKey(user)
    publication_date = models.DateField(blank=True)


class case_report(models.Model):
    id_case_report = models.ForeignKey(case)
    # authors = models.ManyToManyField(user)
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

@删除对象
只需调用查询对象的delete()方法
>>> p = Publisher.objects.get(name="O'Reilly")
>>> p.delete()

>>> Publisher.objects.filter(country='USA').delete()

@访问外键(Foreign Key)值
>>> b = case.objects.get(id=50)
>>> b.user   
<Publisher: Apress Publishing>
>>> b.publisher.website
u'http://www.apress.com/'
在关系的另一端也能反向的追溯回来
>>> p = user.objects.get(name='Apress Publishing')
>>> p.case_set.all()
[<Book: The Django Book>, <Book: Dive Into Python>, ...]
case_set 只是一个 QuerySet

@访问多对多值(Many-to-Many Values)
多对多和外键工作方式相同，只不过我们处理的是QuerySet而不是模型实例
>>> b = Book.objects.get(id=50)
>>> b.authors.all()
[<Author: Adrian Holovaty>, <Author: Jacob Kaplan-Moss>]
>>> b.authors.filter(first_name='Adrian')
[<Author: Adrian Holovaty>]
>>> b.authors.filter(first_name='Adam')
[]

>>> a = Author.objects.get(first_name='Adrian', last_name='Holovaty')
>>> a.book_set.all()
[<Book: The Django Book>, <Book: Adrian's Other Book>]
"""
