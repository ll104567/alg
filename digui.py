
def xxoo(n):
	if n == 1:
		return n
	else:
		return n * xxoo(n-1)

print(xxoo(3))
