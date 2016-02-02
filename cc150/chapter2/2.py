'''
1. Use two pointer, P1 point to front node, P2 point to the point that is n from P1
2. Iteratively increment P1 and P2 until P2 next is None
'''

from classes import *

def nthLast(linkedlist, n):
	P1 = linkedlist.head
	P2 = linkedlist.head


	for x in xrange(0,n-1):
		if P2 == None:
			return None
		P2 = P2.next

	while P2.next != None:
		P2 = P2.next
		P1 = P1.next

	return P1

if __name__ == '__main__':
	testLink = randomLinkedList(8,1,10)
	print testLink
	b = nthLast(testLink, 3)
	print b.value

			