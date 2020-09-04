#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine('sqlite:///sqlite.db')

base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class TklRecord(base):
    # 指定本类映射到TklRecord表
    __tablename__ = 'TklRecord'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    username = Column(String(32))
    time = Column(String(32))
    tkl = Column(String(32))


class UserRecord(base):
    # 指定本类映射到TklRecord表
    __tablename__ = 'UserRecord'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    username = Column(String(32), primary_key=True)
    fanli = Column(Integer)
    createtime = Column(String(32))


def create_table():
    base.metadata.create_all(engine, checkfirst=True)


def add_user():
    pass


def add_tkl_record(username, re_time, tkl):
    add_tkl = TklRecord(username=username, time=re_time, tkl=tkl)
    session.add(add_tkl)


def get_user_fanli():
    pass
