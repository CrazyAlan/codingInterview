'''
1. Contains subtree, if go pre-order traverse and in-order traverse, once the result for t2 is a substring of t1, then it is the subtree
2. Contains subtree, using recursive functions
3. Complexity, if T2 root are all in t1, its O(m*n). If t2's root occurance in t1 is k, it should be O(m+k*n)
'''

def containsSubTree(t1, t2):
	if t2 is None:
		return True
	if t1 is None:
		return False

	return subTree(t1, t2)

def subTree(t1, t2):
	if t1 is None:
		return False
	if t1.data == t2.data:
		return matchTree(t1, t2)
	else:
		return subTree(t1.left, t2) | subTree(t1.right, t2)

def matchTree(t1, t2):
	if t1 is None and t2 is None:
		return True
	if t1 is None or t2 is None:
		return False
	if t1.data != t2.data:
		return False
	else:
		return matchTree(t1.left, t2.left) & matchTree(t1.left, t2.left)

