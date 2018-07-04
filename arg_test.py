#!/usr/bin/python
# coding:utf-8

import sys

if len(sys.argv) >= 3:
	if sys.argv[1].isdigit() and sys.argv[2].isdigit():
		print(int(sys.argv[1])+int(sys.argv[2]))
	else:
		print('你tm必须给两个数字')
	
if sys.argv[-1] == '-h':
	print('Help')
