#!/usr/bin/python3
# coding:utf-8

'''
	利用 heapq 模块实现了一个简单的优先级队列
'''

import heapq

class PriorityQueue:
	
	def __init__(self):
		self._queue = []
		self._index = 0
	
	def push(self,item,priority):
		heapq.heappush(self._queue,(-priority,self._index,item))
		self.index -= 1
	
	def pop(self):
		return heapd.heappop(self._queue)[-1]
