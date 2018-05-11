class X:
	xxoo = 0
	def __init__(self,name,number):
		self.name = name
		self.number = number
	
	def __eq__(self,other):
		return self.number == other.number
	def __str__(self):
		return '[+] Name:{} Age:{}'.format(self.name,self.number)
class Y(X):
	xxoo = 1

a = X('Dashazi',12)
b = X('XXoo',12)
c = Y('dashazi',12)
print(a==c)
print(c.xxoo)
print(a.xxoo)
