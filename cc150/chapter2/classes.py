from random import randint
class Node():
	"""docstring for Node"""
	def __init__(self, value):
		self.value = value
		self.next = None
	def __str__(self):
		return self.value


class LinkedList():
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None
		self.tail = None

	def addNode(self, nodeValue):
		node = Node(nodeValue)
		if not self.head:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def __str__(self):

		if self.head != None:
			index = self.head
			nodestore = [str(index.value)]
			while index.next != None:
				index = index.next
				nodestore.append(str(index.value))
			return "LinkedList  [ " + "->".join(nodestore) + " ]"
		return "LinkedList  []"

	def removeNode(self, node_value):
		currentNode = self.head 
		if currentNode.value == node_value:
			self.head = self.head.next
		while currentNode.next != None:
			if currentNode.next.value == node_value:
				currentNode.next = currentNode.next.next
				break
			else:
				currentNode = currentNode.next

def randomLinkedList(length, min, max):
    linkedlist = LinkedList()
    for i in range(length):
        value = randint(min, max)
        linkedlist.addNode(value)
    return linkedlist

		
		