#!/usr/bin/python

class X:
	def __init__(self,name):
		
		self.name = name

	def __len__(self):
		
		return 5

a = X('dashazi')
print(len(a))
