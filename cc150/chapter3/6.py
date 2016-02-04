'''
1. Sort stack into ascending order
2. Simply create a new stack to store the result
3. If the pop item is larger than the stacked items, pop out all other items, then push the new popped out item
'''



def sortStack(inputStack):
	sortedStack = []
	while inputStack:
		tmp = inputStack.pop()

		if sortedStack and sortedStack[-1] > tmp:
			sortedStack.append(tmp)
		else:
			while sortedStack:
				inputStack.append(sortedStack.pop())
			sortedStack.append(tmp)

	return sortedStack

if __name__ == '__main__':
	testStack = []
	for x in xrange(1,10):
		testStack.append(x)

	testStack[3] = 11

	print testStack
	print sortStack(testStack)
				