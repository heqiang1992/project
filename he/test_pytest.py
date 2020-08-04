#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest


def func(x):
    return x + 1


def test_func1():
    assert func(4) == 5  # 成功示例


def test_func2():
    assert func(3) == 5, "num is %s" % str(func(3))  # 失败示例


def test_func3():
    assert True, "hello "


def test_func4():
    raise Exception("******")


if __name__ == "__main__":
    pytest.main(["--html=report.html", "D:\\code\\pj\\he\\"])

pytest.main()  # 遍历相同目录下的所以test开头的用例
pytest.main("-q test_main.py")  # 指定测试文件
pytest.main("/root/Documents/python3_1000/1000/python3_pytest")  # 指定测试目录
#还可添加很多测试参数例如：
#--junitxml=results.xml 成xml文件结果 ，--resultlog=report\log.txt ，--html=report\test_one_func.html
