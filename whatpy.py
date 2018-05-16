#!/usr/bin/python
# coding:utf-8
"""	
	email : ll104567@163.com
	author: Hu Shuai
"""
import xpinyin
import sys

usage='''
	Usage: whatpy.py + <words>
'''
def get_argv1():
	if len(sys.argv) == 2:
		char = sys.argv[1]
		return char.decode('utf-8')
	else:
		print(usage)
		sys.exit(1)

def get_pinyin(char):
	py = xpinyin.Pinyin()
	py_of_char = py.get_pinyin(char)
	return py_of_char 

def get_pinyin2(char):
	py = xpinyin.Pinyin()
	py_of_char = py.get_pinyin(char,show_tone_marks=True)
	return py_of_char 

def main():
	print(get_pinyin2(get_argv1()))

if __name__ == '__main__':
	main()
