'''
1. if we go start from the root, once we find the particular path sum equal to 
the given value, we couldn't stop as the following may still give the path to that value
2. If we could start at any point, then we could look up to see if there is that sum
'''


from Classes3 import *
import copy

def findSum(givenSum, level, node, bufferNodes):
	if node is None:
		return 

	tmp = givenSum
	bufferNodes.append(node.value)

	for i in range(level-1, -1, -1): #From high level to low level
		tmp -= bufferNodes[i]
		if tmp == 0:
			printBuffer(i, level, bufferNodes)

	level += 1		
	buffer1 = copy.deepcopy(bufferNodes)
	buffer2 = copy.deepcopy(bufferNodes)

	findSum(givenSum, level, node.left, buffer1)
	findSum(givenSum, level, node.right, buffer2)

def printBuffer(i, level, bufferNodes):
	a = "Path " + "level " + str(level) + " value is "
	for i in range(i, level):
		a = a + " " +  str(bufferNodes[i])

	print a


if __name__ == '__main__':
	testArr = range(0,5)
	print testArr
	treeChain = AddToTree(testArr, 0, len(testArr)-1)
	print treeChain.left.right
	bufferInit = []

	findSum(3, 1, treeChain, bufferInit)
	 
		