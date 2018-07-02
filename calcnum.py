from collections import Counter

def readfile(filex):
	
	xxoo = {}
	xx = []
	f = open(filex)
	for i in f:
		if i.strip() not in xxoo:
			xxoo[i.strip()] = 1
	for i in xxoo.keys():
		f1,f2 = i.strip().split()
		xx.append([f1,f2])
	return xx

def calc(xxoo):

	key_list = []
	for i in xxoo:
		key_list.append(i[0])
	a = Counter(key_list)
	return a

a = readfile('file')
print(calc(a))
