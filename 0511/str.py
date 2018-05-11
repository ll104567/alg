class X:
	
	def __init__(self,name,age):
		self.name = name
		self.age = age
	
	def __str__(self):
		return '[+] Name:{} Age:{}'.format(self.name,self.age)

a = X('Dashazi',18)
print(a)
