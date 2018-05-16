
def fibon(n):
	a = 1
	b = 1
	for i in range(n):
		yield(a)
		a, b = b, a+b

def get_list(n):
	x = []
	for i in fibon(n):
		x.append(i)
	return x

