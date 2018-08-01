#!/usr/bin/python
# coding:utf-8

import time
import functools

def _time_is(someword='xxoo'):
	def decorator(function):
		@functools.wraps(function)
		def wrapper(*a,**b):
			start_time = time.time()
			result = function(*a,**b)
			used_time = time.time() - start_time
			print('Used Time: {}/{}'.format(used_time,someword))
			return result
		return wrapper
	return decorator

def _time_is2():
	def decorator(function):
		@functools.wraps(function)
		def wrapper(*a,**b):
			start_time = time.time()
			result = function(*a,**b)
			used_time = time.time() - start_time
			print('Used Time: {}'.format(used_time))
			return result
		return wrapper
	return decorator


@_time_is('a')
def sleep_nothing():
	time.sleep(2)
	return 1


a = sleep_nothing()
print(a)
