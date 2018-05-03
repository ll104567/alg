#!/usr/bin/python3
# coding:utf-8

from collections import deque
from pprint import pprint
from basic import DashaziError,check_iterable

def searchx(lines,pattern,history=5):
	
	last_lines = deque(maxlen=history)
	for i in lines:
		if pattern in i:
			last_lines.append(i)
	return last_lines

def remove_enter(items):
	if not check_iterable(items):
		raise DashaziError('Some Error happened.')
		sys.exit()
	tmp = []
	for i in items:
		i = i.strip()
		tmp.append(i)
	return tmp
def remove_enter2(items):
	
	return [i.strip() for i in items]

if __name__ == '__main__':
	
	filex = 'test.txt'
	with open(filex) as f:
		xx = searchx(f,'10',5)
		pprint(remove_enter(list(xx)))
		pprint(remove_enter2(list(xx)))
