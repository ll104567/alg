#!/usr/bin/python3
# coding:utf-8

from collections import Counter

a = 'shdlfhalisfhgalsfhjasf'
b = 'asohfpasjuf[pajsfgaskdfp'

c = Counter(a)
d = Counter(b)

print((c+d).most_common(3))
