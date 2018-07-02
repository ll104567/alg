import sys

def get_max_length(l):
	'''
	input : list
	output: int
	'''
	
	max = 0
	for i in l:
		if len(i) > max:
			max = len(i)
	return max

def jiexi(s):
	'''
	input : string
	output: list of str
	'''
	
	result = []
	ab = s.split('-')
	max_length = get_max_length(ab)
	for i in range(int(ab[0]),int(ab[-1])+1):
		if len(str(i)) < max_length:
			i = '0'*(max_length-len(str(i)))+str(i)
		result.append(str(i))
	return result 

if __name__ == '__main__':
	a = jiexi(sys.argv[1])
	print(a)
