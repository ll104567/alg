from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

'''
for i in d:
	print (i,d[i])
'''

print(json.dumps(d))
