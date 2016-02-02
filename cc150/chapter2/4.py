'''
1. Using recursive method
2. addLinkedList to return every node 
3. Return None type, need to consider once the high position digit is 1 or 0
4. Need to consider return types, must be linkedlist, also the node next should be more.head
'''
from classes import *


def addLinkedList(list1, list2, carry):
	rstList = LinkedList()
	rst = Node(carry)
	rstList.head = rst
	if list1 == None and list2 == None:
		if carry:
			return rstList
		else:
			return None
	if list1 != None:
		rst.value += list1.value
	if list2 != None:
		rst.value += list2.value

	if rst.value > 9:
		more = addLinkedList(list1.next if list1 else None, list2.next if list2 else None, 1)
	else:
		more = addLinkedList(list1.next if list1 else None, list2.next if list2 else None, 0)

	rst.value %= 10
	if more:
		rst.next = more.head 

	#return rst
	rstList.next = more
	return rstList

def addLinkedListIterative(list1, list2):
	p1 = list1.head
	p2 = list2.head
	carry = 0
	rstList = LinkedList()
	while p1 or p2 or carry:
		value = carry
		if p1:
			value += p1.value
			p1 = p1.next #once p1 is none, it will stay there
		if p2:
			value += p2.value
			p2 = p2.next
		if value > 9:
			carry = 1
			value %= 10
		else:
			carry = 0
		
		rstList.addNode(value)

		
	return rstList

if __name__ == '__main__':
	
	list1 = randomLinkedList(13,0,9)
	list2 = randomLinkedList(3,0,9)

	result1 = addLinkedList(list1.head, list2.head, 0)
	result2 = addLinkedListIterative(list1, list2)
	print list1, list2
	print "hello"
	print result1, result2
