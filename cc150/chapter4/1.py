import random

#binary tree python
class BinaryTree:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None
        #-1 means the depth has not been calculated yet.
        self.depth = -1

    def __str__(self):
        return "( " + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

    def maxDepth(self):
       		return 1 + max(self.left.maxDepth() if self.left else 0, self.right.maxDepth() if self.right else 0)
    def minDepth(self):
      		return 1 + min(self.left.minDepth() if self.left else 0, self.right.minDepth() if self.right else 0)


if __name__ == '__main__':
	bt = BinaryTree(random.randint(0, 100))
	for c1 in xrange(0,6):
	    bt2 = BinaryTree(random.randint(0, 100))
	    bt2.left = bt
	    bt=bt2
	print bt

	def makeRandomTree(depth):
		if depth > 0 :
			tree = BinaryTree(random.randint(0,100))
			tree.left = makeRandomTree(depth - 1)
			tree.right = makeRandomTree(depth - 1)
			return tree
		else:
			return None

	testTree =  makeRandomTree(4)
	print testTree
	print bt.maxDepth()
	print bt.minDepth()
#In order to determine whether it is balanced tree, just compare the difference between
#max depth and min depth is within 1


