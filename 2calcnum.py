from collections import Counter

def readfile(filex):
	
	xxoo = {}
	xx = []
	f = open(filex)
	for i in f:
		f1,f2 = i.strip().split()
		xx.append([f1,f2])
	return xx

def calc(xxoo):

	key_list = []
	for i in xxoo:
		key_list.append(i[0])
	a = Counter(key_list)
	return a

def calc2(xxoo):
	
	filex = []
	for i in xxoo:
		filex.append(' '.join(i))
	a = {}
	for i in filex:
		if i not in a:
			a[i] = 1
		else:
			a[i] += 1
	b = []
	for i in a.keys():
		if a[i] > 1:
			for j in range(a[i]-1):
				b.append(i.split()[0])
	c = Counter(b)

	return c

a = readfile('file')
print(calc(a)-calc2(a))
