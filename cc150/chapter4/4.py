'''
1. For each layer, have a result variable to store all data, then have a list for
each layer, then loop through that list and new a list to store all it's left and right 
child, finally check if the list is empty, if it is, then jump out, otherwise loop again
2. Append is wrong, need to append the left or right node
''' 
from Classes3 import *


def bfsTraverse(root):
	result = []
	rstList = []
	rstList.append(root)
	result.append(rstList)
	level = 0

	while True :
		newList = []
		for node in result[level] :
		#	print "node " + str(node)
			if node.left:
				#print "left node %d"%node.left
				newList.append(node.left)
			if node.right:
				newList.append(node.right)

		if not newList:
			break

		result.append(newList)
		
		level += 1

	return result


if __name__ == '__main__':
	testArr = range(0,8)
	print testArr
	a = AddToTree(testArr, 0, len(testArr)-1)
#	print a.right 
	rst = bfsTraverse(a)

	print len(rst) 


