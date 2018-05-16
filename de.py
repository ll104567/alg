import time

def timeis(f):
	def xx(*a,**b):
		c = time.time()
		d = f(*a,**b)
		print('Used Time:{}'.format(time.time()-c))
	return xx

@timeis
def test_timeis(a='hello'):
	time.sleep(1)
	print('test')
	return 'test'

test_timeis(123)
