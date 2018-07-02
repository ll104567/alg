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

def fact_solve(n):
	if len(str(n)) == 3:
		n *= 10
	if n == 6174:
		print('Found:[{}]'.format(6174))
		return 1 
	else:
		print('[{:4}] - [{:4}] = [{:4}]'.format(big_small(n),small_big(n),big_small(n)-small_big(n)))
		fact_solve(big_small(n)-small_big(n))

if __name__ == '__main__':
	fact_solve(int(sys.argv[1]))

