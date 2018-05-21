def get_answer(n):
	
	str_n = str(n)
	set_n = set(str_n)
	if len(set_n) < 6:
		return False
	for i in range(2,7):
		s = n*i
		if set(str(s)) != set_n:
			return False
	return True

for i in range(100000,200000):
	if get_answer(i):
		print(i)
		print(i*7)
