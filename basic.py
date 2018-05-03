import sys
from collections import Iterable

class DashaziError(Exception):	
	pass

def check_iterable(items):
	'''return 1/0'''
	
	return isinstance(items,Iterable)
