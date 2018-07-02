class dict2:

	def __init__(self):	
		self._data = {}

	def __getitem__(self,key):
		print(self._data.get(key))
	
	def __setitem__(self,key,value):
		self._data[key] = value
		print('[{}] -> [{}]'.format(key,value))
	
	def __delitem__(self,key):
		del self._data[key]

a = dict2()
a['a'] = 1
a['b'] = 2
a['a']
del a['b']
a['b']
