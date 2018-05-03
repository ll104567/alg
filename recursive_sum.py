#!/usr/bin/python3
# coding:utf-8

import sys
from collections import Iterable

class DashaziError(Exception):	
	pass

def check_iterable(items):
	'''return 1/0'''
	
	return isinstance(items,Iterable)

def sumx(items):
	'''items require a list'''
	
	if not check_iterable(items):
		raise DashaziError('Need a list')
		sys.exit()

	head,*tail = items

	if tail:
		return head + sum(tail)
	else:
		return head

if __name__ == '__main__':
	
#	print(sumx(100))
	print(sumx([1,2,3,1,3]))
	print(sumx(range(10)))
	
