'''
How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time
1. Use tuple to store value and min, so each time peek would return that tuple, so as the min value
2. Use another stack to keep track of the minimum number, if the value is as low as the min number, then we need to put into stack
3. Need to keep in mind that stack might be empty
4. When pop out, need to compare the value with the min, get the min is self.min[-1]
'''
from classes import *
class stackWithMin():
	"""docstring for stackWithMin"""
	def __init__(self):
		self.data = []

	def push(self, value):
		if not len(self.data) or self.data[-1][1] > value:
			self.data.append((value, value))
		else:
			self.data.append((value, self.data[-1][1]))

	def pop(self):
		return self.data.pop()[0]

	def getTop(self):
		if len(self.data) == 0:
			return None
		else:
			return self.data[-1][0]
	def getMin(self):
		if len(self.data) == 0:
			return None
		else:
			return self.data[-1][1]

class stackWithMin2():
	def __init__(self):
		self.data = []
		self.min = []

	def push(self, value):
		if not len(self.data) or value <= self.min[-1]:
			self.data.append(value)
			self.min.append(value)
		else:
			self.data.append(value)

	def pop(self):
		if not len(self.data):
			pass
		value = self.data.pop()
		if value == self.min[-1]:
			self.min.pop()
		return value

	def getMin(self):
		if not len(self.min): #need to keep track that stack might be empty 
			return None
		return self.min[-1]	




if __name__ == '__main__':
	testArray = randArray(6,1,10)
	testStack = stackWithMin()
	testStack2 = stackWithMin2()

	for x in xrange(0,len(testArray)):
		testStack.push(testArray[x])
		testStack2.push(testArray[x])

	print testArray
	testStack.pop()
	testStack2.pop()
	testStack.pop()
	testStack2.pop()
	print testStack.getMin()
	print testStack2.getMin()

	




