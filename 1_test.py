#!/usr/bin/python
# coding:utf-8

import random
import string

def generate_n_code2(n=20):
	'''
	output: str
	'''
	random_code_str = ''
	for i in range(n):
		random_code_str += random.choice(string.digits + string.ascii_uppercase)
	return random_code_str 

def generate_n_code(n=20):
	'''
	output: str
	'''
	random_code = []
	for i in range(n):
		random_code.append(random.choice(string.digits + string.ascii_uppercase))
	return ''.join(random_code)

def generate_how_many(n=200):
	'''
	output: list
	'''
	total_code = []
	for i in range(n):
		total_code.append(generate_n_code2())
	
	return total_code

def write_to_file(filename='code.txt'):
	
	f = open(filename,'w')
	for i in generate_how_many():
		f.write(i+'\n')
	f.close()


if __name__ == '__main__':

	write_to_file()



