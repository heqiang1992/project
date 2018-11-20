# -*- coding: utf-8 -*-

a = 5
assert 1 < a < 10, 'echo！'
item = [x * x for x in range(10) if x % 3 == 0]
exec ("b='sb'")
b = 5
eval(a * b)


class MyException(ImportError):
    pass


class fibs():

    def next(self):
        pass

    def __iter__(self):
        return self


def flatten(r):
    for sublist in r:
        for element in sublist:
            yield element


for num in flatten(item):
    print(num)

import sys
args = sys.argv[1:]
import fileinput