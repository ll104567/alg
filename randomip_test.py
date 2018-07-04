#!/usr/bin/python
# coding:utf-8

import random

a = str(random.randint(0,255))
b = str(random.randint(0,255))
c = str(random.randint(0,255))
d = str(random.randint(0,255))


print(a+'.'+b+'.'+c+'.'+d)
print('.'.join([a,b,c,d]))
