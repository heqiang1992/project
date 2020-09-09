#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import datetime


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

    #id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    username = Column(String(32), primary_key=True)
    fanli = Column(Integer)
    createtime = Column(String(32))


def create_table():
    base.metadata.create_all(engine, checkfirst=True)


def add_user(username,fanli=0):
    now_time = datetime.datetime.now()
    now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
    new_user = UserRecord(username=username, fanli=fanli, createtime=now_time)
    session.add(new_user)
    session.commit()

def add_tkl_record(username, re_time, tkl):
    add_tkl = TklRecord(username=username, time=re_time, tkl=tkl)
    session.add(add_tkl)
    session.commit()


def get_user_fanli():
    pass

def check_user(username):
    user = session.query(UserRecord).filter_by(username=username).first()




if __name__ == "__main__":
    # create_table()
    # add_user(username="test")
    # add_user(username="test1")
    # add_user(username="test2")
    # add_user(username="test3")
    a = check_user(username="0")
    print(a)