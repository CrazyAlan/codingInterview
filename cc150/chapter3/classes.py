from random import randint

def randArray(num, min, max):
	array = [0]*num	
	for x in xrange(0,num):
		array[x] = randint(min, max)
	return array

if __name__ == '__main__':
	print randArray(10, 1,10)