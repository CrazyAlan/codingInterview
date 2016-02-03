'''
1. First implementation, simply divide the array to 3 pieces, use a stack pointer to track the top element
2. Use a stack node as element in each array, it has previous element's index and current value
the stack node need to keep track of previous element's index
'''
from classes import *
class stack1():
	"""docstring for stack1"""
	def __init__(self):
		self.stackSize = 100
		self.arraySize = self.stackSize*3
		self.array = [0]*self.arraySize
		self.stackPointer = [0, 0, 0]

	def push(self, stackID, value):
		index = stackID*self.stackSize + self.stackPointer[stackID]
		self.array[index] = value
		self.stackPointer[stackID] += 1

	def pop(self, stackID):

		if self.stackPointer[stackID] <= 0:
			return None

		index = stackID*self.stackSize + self.stackPointer[stackID] - 1
		value = self.array[index]
		self.array[index] = 0
		self.stackPointer[stackID] -= 1
		return value

class stackNode():
	"""docstring for stackNode"""
	def __init__(self, p, value):
		self.previous = p	
		self.value = value	

class stack2():
	"""docstring for stack2"""
	def __init__(self):
		self.arraySize = 300
		self.freeList = range(0, self.arraySize)
		self.stackPointer = [-1, -1, -1]

	def push(self, value):
		
		

if __name__ == '__main__':
	testStack = stack1()
	testArray = randArray(19,1,10)
	print testArray
	for i in range(0,len(testArray)):
		testStack.push(1, testArray[i])

	for i in range(0,len(testArray)):
		print testStack.pop(1)
 


		
