#!/usr/bin/python
# coding:utf-8

import time

def time_is(function):
	def wrapper(*a,**b):
		start_time = time.time()
		result = function(*a,**b)
		used_time = time.time() - start_time
		print('Used Time: {}'.format(used_time))
		return result
	return wrapper

@time_is
def sleep_nothing():
	time.sleep(2)
	return 1


a = sleep_nothing()
print(a)
