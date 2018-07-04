#!/usr/bin/python
# coding:utf-8

import colorama

user_input = raw_input('Plz input (Yes/[N]o):')

if user_input.lower().startswith('y'):
	print(colorama.Fore.GREEN + user_input)
else:
	print('no')
