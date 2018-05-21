#!/usr/bin/python
# coding:utf-8
"""	
	email  : ll104567@163.com
	author : Hu Shuai
	version: 0.03
"""
import xpinyin
import sys
import click
import time
import os
import pyfiglet

usage='''
	Usage: whatpy.py + <words>
'''
def clear():
	os.system('clear')

def get_pinyin(char):
	py = xpinyin.Pinyin()
	py_of_char = py.get_pinyin(char,splitter=' ')
	return py_of_char 

def get_pinyin2(char):
	py = xpinyin.Pinyin()
	py_of_char = py.get_pinyin(char,show_tone_marks=True,splitter=' ')
	return py_of_char 

def figlet_bling_print(char):
	clear()
	string = char
	a = pyfiglet.Figlet()
	for i in range(len(string)+1):
		clear()
		print(a.renderText(string[:i]))
		time.sleep(0.5)

	for i in range(5):
		clear()
		print(a.renderText('*'*(len(string)-1)))
		time.sleep(0.3)
		clear()
		print(a.renderText(string))
		time.sleep(0.3)
def figlet_print(char):
	clear()
	string = char
	a = pyfiglet.Figlet()
	print(a.renderText(string))

@click.command()
@click.option('-t','--tone',help='show tone or not',is_flag=True)
@click.option('-b','--bling',help='bling or not',is_flag=True)
@click.argument('char')
def main(char,tone,bling):
	if tone:
		get_pinyin_func = get_pinyin2
	else:
		get_pinyin_func = get_pinyin
	
	if bling:
		fig_print = figlet_bling_print
	else:
		fig_print = figlet_print 

	fig_print(get_pinyin_func(char))

if __name__ == '__main__':
	main()
