#!/usr/bin/python
# coding:utf-8
"""	
	email  : ll104567@163.com
	author : Hu Shuai
	version: 0.02
"""
import xpinyin
import sys
import click

usage='''
	Usage: whatpy.py + <words>
'''

def get_pinyin(char):
	py = xpinyin.Pinyin()
	py_of_char = py.get_pinyin(char)
	return py_of_char 

def get_pinyin2(char):
	py = xpinyin.Pinyin()
	py_of_char = py.get_pinyin(char,show_tone_marks=True)
	return py_of_char 

@click.command()
@click.option('-n','--notone',help='show tone or not',is_flag=True)
@click.argument('char')
def main(char,notone):
	if notone:
		get_pinyin_func = get_pinyin
	else:
		get_pinyin_func = get_pinyin2
	
	print(get_pinyin_func(char))

if __name__ == '__main__':
	main()
