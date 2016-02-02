'''
1. If could use hash table, the set a table with indicator which character exists
2. No use of any other buffer, use O(n^2) method  
'''
from classes import *

def solHash(linkedlist):
	if linkedlist.head != None:
		currentNode = linkedlist.head
		dic = {currentNode.value : True}

		while currentNode.next != None:
			if currentNode.next.value in dic:
				currentNode.next = currentNode.next.next
			else:
				dic[currentNode.next.value] = True	
				currentNode = currentNode.next


def solNoBuff(linkedlist):
	currentNode = linkedlist.head
	if currentNode == None:
		return None
	while currentNode != None:
		runner = currentNode
		while runner.next != None:
		#	print runner.value
			if currentNode.value ==  runner.next.value:
				runner.next = runner.next.next
			else:
				runner = runner.next

		currentNode = currentNode.next
				

L1 = randomLinkedList(4,3,6)
print L1
solNoBuff(L1)
print L1