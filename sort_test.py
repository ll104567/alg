#!/usr/bin/python
# coding:utf-8

import sys

def big_to_small_number(n):
	'''
	input : str
	output: str
	'''
	list_number = list(n)
	sort_list_number = sorted(list_number,reverse=1)
	
	return ''.join(sort_list_number)

def small_to_big_number(n):
	'''
	input : str
	output: str
	'''
	list_number = list(number)
	sort_list_number = sorted(list_number)
	return ''.join(sort_list_number)

for i in sys.argv:
	print(i)
