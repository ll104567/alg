
def fact(n):
	
	if n == 1:
		return 1
	else:
		return n * fact(n-1)

def tailfact(n,result=1):
	
	if n == 1:
		return result
	else:
		return tailfact(n-1,n*result)


if __name__ == '__main__':
	
	print(fact(999))
	print(tailfact(999))
