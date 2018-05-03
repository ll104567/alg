#!/usr/bin/python3
# coding:utf-8
'''
	怎样从一个集合中获得最大或者最小的 N 个元素列表？
'''

import heapq
from pprint import pprint


def headn(l, n=1):

    return heapq.nlargest(n, l)


def tailn(l, n=1):

    return heapq.nsmallest(n, l)


def head_for_dict(d, key, n=1):

    return heapq.nlargest(n, d, key)


if __name__ == '__main__':

    xx = [2, 3, 52, 45, 12, 321, 4, 2, 4, 2, 7, 3, 56, 7]
    print(headn(xx, 3))
    print(tailn(xx, 2))

    oo = [
        {'name': 'll', 'grade': 98},
        {'name': 'ls', 'grade': 78},
        {'name': 'lx', 'grade': 88},
        {'name': 'lf', 'grade': 68},
        {'name': 'lh', 'grade': 95},
        {'name': 'lg', 'grade': 38},
    ]

    pprint(head_for_dict(oo, lambda s: s['grade'], 3))
