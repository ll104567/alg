#!/usr/bin/python
# coding:utf-8

import sys
import random

def get_choice():
	choice = ''
	count = 0
	while not choice:
		print('1 -> 石头 2-> 剪刀 3-> 布')
		choice = raw_input('Plz input: ')

		count += 1
		if count > 5:
			sys.exit()

	return choice

def verify_choice(choice):
	
	if choice not in '123':
		return None
	else:
		return choice

def random_init():

	ai_dict = {'1':'石头','2':'剪刀','3':'布'}
	ai_choice =  random.choice('123')
	print('Ai puts {}'.format(ai_dict[ai_choice]))

	return ai_choice 

def who_win(ai,other):
	'''
		return 1 ai win ; return 0 other win ;return 2 tie
	'''
	if ai == other:
		return 2
	if (ai,other) in [('1','2'),('2','3'),('3','1')]:
		return 1
	else:
		return 0

def print_result(code):
	if code == 0:
		print('You win')
		return 0
	if code == 1:
		print('Ai  win')
	else:
		print('No one wins')

	
a = verify_choice(get_choice())
if a:
	print_result(who_win(random_init(),a))	
