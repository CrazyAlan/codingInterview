'''
1. A sorted array, chose left sub as the left tree and right sub as the right tree, and middle number as the node
'''


class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.value)

def AddToTree(arr, start, end): #return a tree node
	if start > end:
		return None
	midIndex = (start+end)/2
	midNode = TreeNode(arr[midIndex])
	midNode.left = AddToTree(arr, start, midIndex-1)
	midNode.right = AddToTree(arr, midIndex+1, end)

	return midNode


if __name__ == '__main__':
	testArr = range(0,4)
	print testArr
	a = AddToTree(testArr, 0, len(testArr)-1)

	print a.right.right 
