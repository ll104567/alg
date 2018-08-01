
def myabs(x):
	
	if not isinstance(x,(int,float)):
		return None
	if x < 0:
		x = -x
	
	return x


if __name__ == '__main__':
	
	print(myabs(12))
	print(myabs('12'))
	print(myabs(-12))
