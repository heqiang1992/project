#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('sqlite:///sqlite.db')
# Windows
# engine = create_engine('sqlite:///C:\\path\\to\\foo.db')
# format 1   sqlite可以创建内存数据库（其他数据库不可以）
# engine = create_engine('sqlite://')
# format 2
# engine = create_engine('sqlite:///:memory:', echo=True)

base = declarative_base()

from sqlalchemy import Column, Integer, String


class TklRecord(base):
    # 指定本类映射到users表
    __tablename__ = 'TklRecord'
    # 如果有多个类指向同一张表，那么在后边的类需要把extend_existing设为True，表示在已有列基础上进行扩展
    # 或者换句话说，sqlalchemy允许类是表的字集
    # __table_args__ = {'extend_existing': True}
    # 如果表在同一个数据库服务（datebase）的不同数据库中（schema），可使用schema参数进一步指定数据库
    # __table_args__ = {'schema': 'test_database'}

    # 各变量名一定要与表的各字段名一样，因为相同的名字是他们之间的唯一关联关系
    # 从语法上说，各变量类型和表的类型可以不完全一致，如表字段是String(64)，但我就定义成String(32)
    # 但为了避免造成不必要的错误，变量的类型和其对应的表的字段的类型还是要相一致
    # sqlalchemy强制要求必须要有主键字段不然会报错，如果要映射一张已存在且没有主键的表，那么可行的做法是将所有字段都设为primary_key=True
    # 不要看随便将一个非主键字段设为primary_key，然后似乎就没报错就能使用了，sqlalchemy在接收到查询结果后还会自己根据主键进行一次去重
    # 指定id映射到id字段; id字段为整型，为主键，自动增长（其实整型主键默认就自动增长）
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    username = Column(String(32))
    time = Column(String(32))
    tkl = Column(String(32))

# 创建数据表。一方面通过engine来连接数据库，另一方面根据哪些类继承了Base来决定创建哪些表
# checkfirst=True，表示创建表前先检查该表是否存在，如同名表已存在则不再创建。其实默认就是True
#base.metadata.create_all(engine, checkfirst=True)
# 此时可以通过tables参数指定方式，指示仅创建哪些表
# Base.metadata.create_all(engine,tables=[Base.metadata.tables['users']],checkfirst=True)
# 在项目中由于model经常在别的文件定义，没主动加载时上边的写法可能写导致报错，可使用下边这种更明确的写法
TklRecord.__table__.create(engine, checkfirst=True)

#建立会话
#增查改删（CRUD）操作需要使用session进行操作
from sqlalchemy.orm import sessionmaker

# engine是2.2中创建的连接
Session = sessionmaker(bind=engine)

# 创建Session类实例
session = Session()

#增
# 创建User类实例
ed_user = TklRecord(username='ed', time='Ed Jones', tkl='edspassword')

# 将该实例插入到users表
session.add(ed_user)

# 一次插入多条记录形式
# session.add_all(
#     [TklRecord(name='wendy', fullname='Wendy Williams', password='foobar'),
#      TklRecord(name='mary', fullname='Mary Contrary', password='xxg527'),
#      TklRecord(name='fred', fullname='Fred Flinstone', password='blah')]
# )

# 当前更改只是在session中，需要使用commit确认更改才会写入数据库
session.commit()