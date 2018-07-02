import sys

debug = False
if sys.argv[-1] == '-d':
	debug = True


def big_small(n):
	'''
	input:  int
	output: int
	'''
	list_n = list(str(n))
	return int(''.join(sorted(list_n,reverse=True)))

def small_big(n):
	'''
	input : int
	output: int
	'''
	list_n = list(str(n))
	return int(''.join(sorted(list_n)))

if debug:
	print(big_small(int(sys.argv[1])))
	print(small_big(int(sys.argv[1])))

def fact_solve(n):

	if n == 6174:
		print('Found:[{}]'.format(6174))
		return 1 
	else:
		print('[{}] - [{}]'.format(big_small(n),small_big(n)))
		fact_solve(big_small(n)-small_big(n))

if debug:
	fact_solve(int(sys.argv[1]))

