import cai
import jiexi
import sys

debug = False
if sys.argv[-1] == '-d':
	debug = True

def get_vaild_data(s):
	'''
	input : string
	output: Bool
	'''
	if len(s) < 4:
		return False
	if len(set(list(s))) < 4:
		return False
	return True

if debug:
	print(get_vaild_data(sys.argv[1]))
	sys.exit(1)

def define():
	count = 0
	num_list = jiexi.jiexi(sys.argv[1])
	for i in num_list:
		if get_vaild_data(i):
			count += 1
			i = int(i)
			print('Number:[{}]'.format(i))
			cai.fact_solve(i)
	return count

if __name__ == '__main__':
	define()
