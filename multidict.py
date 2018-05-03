#!/usr/bin/python3
# coding:utf-8

''' 
	怎样实现一个键对应多个值的字典
'''
from pprint import pprint
from collections import defaultdict

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

d1 = defaultdict(list)
d1['a'].append(1)
d1['a'].append(2)
d1['b'].append(4)

e1 = defaultdict(set)
e1['a'].add(1)
e1['a'].add(2)
e1['b'].add(4)

pprint(d)
pprint(e)

pprint(d1)
pprint(e1)
