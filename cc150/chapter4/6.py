'''
1. If we have the parent link, we could trace back to the common ancestor
2. If we use a recursive algorithm, just to check if its left or right have both p and q, if not, the root would be the common ancestor
3. 
'''


from Classes3 import *


def commonAcesstor(root, p, q):
	if covers(root.left,p) & covers(root.left, q):
		return commonAcesstor(root.left, p, q)
	elif covers(root.right, p) & covers(root.right, q):
		return commonAcesstor(root.right, p, q)
	else:
		return root

def covers(root, p):
	if root == None:
		return False
	if root == p:
		return True
	return (covers(root.left, p) | covers(root.right, p))



def covers2(root, p, q):
	ret = 0
	if root == None:
		return ret
	if root == p | root == q:
		ret += 1
	ret += covers2(root.left, p, q)
	if ret == 2:
		return ret

	ret += covers2(root.right, p, q)
	return ret

def commonAcesstor2(root, p, q):
	if p==q & (root.left == p | root.right == q):
		return root
	nodesFromLeft = covers2(root.left, p, q)
	if nodesFromLeft == 2:
		if root.left == p | root.left == q:
			return root.left
		else:
			return commonAcesstor2(root.left, p, q)

	elif nodesFromLeft == 1:
		if root == p | root == q:
			return root

	nodesFromRight = covers2(root.right, p, q)
	if nodesFromRight == 2:
		if root.right == p | root.right == q:
			return root.right
		else:
			return commonAcesstor2(root.right, p, q)
	elif nodesFromRight == 1:
		if root == p | root == q:
			return root

	if nodesFromLeft == 1 & nodesFromRight == 1:
		return root
	else:
		return None