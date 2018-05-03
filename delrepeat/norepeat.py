#!/usr/bin/python3
# coding:utf-8

from collections import deque
import sys
import os

usage = '''
	python3 norepeat.py <filename>
'''

def get_sys_argv():
	
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		return filename
	else:
		print(usage)
		sys.exit(1)


def get_file_handle(filename):
	
	try:
		f = open(filename)
		return f
	except:
		print('file cannot open')
		sys.exit(2)

def deal_repeat(f_handle):
	
	no_repeat_seq = deque()
	no_repeat = set()
	for i in f_handle:
		if i not in no_repeat:
			no_repeat_seq.append(i)
			no_repeat.add(i)
	return no_repeat_seq

def write_to_file(filename,seq):

	start = 'np_'
	filename = os.path.basename(filename)
	with open(start+filename,'w') as f:
		for i in seq:
			f.write(i)

def main():
	
	filename = get_sys_argv()
	seq = deal_repeat(get_file_handle(filename))
	write_to_file(filename,seq)

if __name__ == '__main__':
	
	main()
