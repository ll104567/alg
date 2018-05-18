import os

def walk(path):
	for i in os.listdir(path):
		full_path = os.path.sep.join((path,i))
		if os.path.isdir(full_path):
			walk(full_path)
		else:
			if i.endswith('.py'):
				print full_path

walk('/root/pwb')
