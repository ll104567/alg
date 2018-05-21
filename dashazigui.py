import time
import os
import pyfiglet

def clear():
	os.system('clear')

string = 'D4sh4zi'
a = pyfiglet.Figlet()
for i in range(len(string)+1):
	clear()
	print(a.renderText(string[:i]))
	time.sleep(0.5)

for i in range(5):
	clear()
	print(a.renderText('*'*(len(string)-1)))
	time.sleep(0.3)
	clear()
	print(a.renderText(string))
	time.sleep(0.3)

