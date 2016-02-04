'''
1. Using 2 stacks to mimic the queue 
2. We push new elements into s1
3. For dequeue, we pop out elements from s2, as when s2 is empty, we pop out
elements from s1 to s2
'''

class MyQueue():
	"""docstring for MyQueue"""
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enqueue(self, value):
		self.s1.append(value)

	def dequeue(self):
		if self.s2:
			return self.s2.pop()
		else:
			while self.s1:
				self.s2.append(s1.pop())
		if self.s2:		
			return self.s2.pop()

	def peek(self):
		if self.s2:
			return self.s2[-1]
		else:
			while self.s1:
				self.s2.append(self.s1.pop())
		if self.s2:		
			return self.s2[-1]

if __name__ == '__main__':
	testQue = MyQueue()
	for x in xrange(1,10):
		testQue.enqueue(x)

	print testQue.s1
	testQue.peek()
	print testQue.dequeue()
	print testQue.s1


