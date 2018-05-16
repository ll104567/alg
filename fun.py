
def hello(name='xx'):
	
	def xx():
		print('hello xx')
	
	def oo():
		print('hello oo')
	
	def other():
		print('hello')

	if name == 'xx':
		return xx
	elif name == 'oo':
		return oo
	else:
		return other

a = hello('oo')
a()
