import sys
import re
import click

def read_file(f):
	''' from handle get data return list'''
	str_list = []
	temp_str = ''

	for i in f:
		if i != '\n':
			temp_str += i
		else:
			str_list.append(temp_str)
			temp_str = ''
	
	return str_list

def search(str_list,searchx = 'xxoo' ,only=True):
	for i in str_list:
		if searchx in i:
			print(i)
			if only:
				break

def re_search(str_list,re_searchx = '^h',only = True):
	
	re_xx = re.compile(re_searchx)
	for i in str_list:
		if re_xx.search(i):
			print(i)
			if only:
				break
@click.command()
@click.argument('filex')
@click.argument('searchx')
def main(filex,searchx):
	
	try:	
		f = open(filex)
	except IOError:
		print('')
		print('''   Usage:xx.py <file> <search>   ''')
		print('')
		sys.exit(2)

	b = read_file(f)
	re_search(b,searchx)

main()
