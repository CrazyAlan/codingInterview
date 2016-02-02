'''
1. If 2 runners with speed 2 and 1, if they move from the start, they will meet at the start point of the loop
2. If runner 2 is k step before runner 1, then they will meet at n-k step
3. So if two runners run from the beginning of the linked list, they will meet at n-k
here k is the step that runner 2 ahead of runner 1, actually it should be k%n
4. So once they meet each other, we put runner 1 at the beginning of the list, then set they run at the same speed
they would meet at the loop start point
5. If there is a loop in the linked list, you need to first identify the loop start point, then 
print out to that node again
'''

from classes import *

def findLoopBegin(linkedlist):
	if linkedlist.head == None:
		return None

	n1 = linkedlist.head
	n2 = linkedlist.head

	while n2.next != None:
		n1 = n1.next
		n2 = n2.next.next
		if n1 == n2:
			break
	if n2.next == None:
		return None

	n1 = linkedlist.head

	while n1 != n2:
		n1 = n1.next
		n2 = n2.next

	return n1

if __name__ == '__main__':
	linkedlist = randomLinkedList(4, 1,10)
	print linkedlist
	linkedlist2 = randomLinkedList(3, 1, 10)
	print linkedlist2

	linkedlist2.tail.next = linkedlist2.head
	linkedlist.tail.next = linkedlist2.head


	rst = findLoopBegin(linkedlist)
	print rst.value
