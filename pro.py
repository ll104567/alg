
class Student(object):

	_score = 0

	@property
	def score(self):

		return self._score
	
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('Score must be int')
		if value < 0 or value > 100:
			raise ValueError('Score invaild')

		self._score = value

s = Student()
s.score = 1002
print(s.score)
