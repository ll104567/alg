#!/usr/bin/python3
# coding:utf-8

from fnmatch import fnmatch,fnmatchcase

def test(a,b):
	''' like linux command test'''

	return fnmatch(a,b)


if __name__ == '__main__':
	
	print(test('a.txt','*txt'))
	print(test('a.tx','*txt'))
