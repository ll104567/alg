
def threenum(x):
	
	result = []
	for i in range(len(x)):
		for j in range(i):
			for k in range(j):
				if x[i]+x[j]+x[k] == 0:
					xxoo = [x[i],x[j],x[k]]
					if xxoo not in result:
						result.append(xxoo)
	


	return result

a = [-1, 0, 1, 2, -1, -4]
print(threenum(a))
