class xx:
	
	def __init__(self,a):
		self.a = a
	
	@property
	def power(self):
		return self.a ** 2

a = xx(10)
print(a.power)
