#!/urs/bin/python
def printmax(x,y):
	'''prints the maximum of two numbers.
	the two value must be integer.'''
	x=int(x)
	y=int(y)
	if x>y:
		print x,'is maximum.'
	else:
		print y,'is maximum.'
printmax(3,5)
print printmax.__doc__