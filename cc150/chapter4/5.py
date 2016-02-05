'''
1. If X has right child, then it successor need to be it's right child's most left child
2. If X is the left child, then it's parent is the successor, otherwise, we are going
to find it's parent's successor
'''


from Classes3 import *

class TreeNodeWithParent(TreeNode):
	"""docstring for TreeNodeWithParent"""
	def __init__(self, value):
		super(TreeNodeWithParent, self).__init__(value)
		self.parent = None
		

def leftMostChild(leftChild):
	if leftChild is None:
		return None
	else:
		while leftChild.left is not None:
			leftChild = leftChild.left

	return leftChild

def inorderSuccessor(x):
	if x.right is not None:
		return leftMostChild(x.right)
	else:
		while x.parent is not None:
			p = x.parent
			if x == p.left:
				return p
			else:
				x = p

	return None


if __name__ == '__main__':
	testArr = range(0,4)
	print testArr
	a = AddToTree(testArr, 0, len(testArr)-1)
	

		