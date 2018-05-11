
class Example:
	
	def init(self, name):
		self.name = name	
		return self
	def xxoo(self):
		return self.name

a = Example()
print(a.init('Dashazi').xxoo())

