'''
1. if only get access to the node to be deleted, then just replace the node's 
value and next node
2. If the node is the last node, then could not delete it, as in this way, 
it only replace the node not delete
'''

from classes import *



def deleteNode(node):
	
	if node == None or node.next == None:
		return False #failed to delete

	next = node.next
	node.value = next.value
	node.next = next.next
	return True

#Test
if __name__ == '__main__':
	linkedlist = randomLinkedList(4,1,10)
	print linkedlist

	node = linkedlist.head.next.next.next
	print node.value
	print deleteNode(node)

	print linkedlist
