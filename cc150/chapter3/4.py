'''
1. Hanoi Tower
2. Recursive algorithm, move the top N-1 to the buffer using destination as buffer, then move the 
last one to destination, then using rod 0 as buffer, move the rest n-1 to rod 0, then last one to 
destination.
3. When compare self data, need to make sure self data got content in
4. Need to make sure use which as the buffer, which as the destination, which tower is the origin
'''

class Tower():
	"""docstring for Tower"""
	def __init__(self, index):
		self.index = index
		self.data = []

	def add(self, value):
		if self.data and self.data[-1] < value:
			print "Error put data %d into %d"%(value, self.index)
		else:
			self.data.append(value)

	def movTop(self, destination):
		if self.data:
			value = self.data.pop()

			print 'Move data %d from tower %d to tower %d'%(value, self.index, destination.index)
			destination.add(value)

	def moveDisks(self, n, destination, bufferDisk):
		if n > 0:
			 
			self.moveDisks(n-1, bufferDisk, destination)
			self.movTop(destination)
			bufferDisk.moveDisks(n-1, destination, self)

if __name__ == '__main__':
	towers = []
	for x in xrange(0,3):
		towers.append(Tower(x))

	for i in range(10,0,-1):
		towers[0].add(i)

	print towers[0].data

	towers[0].moveDisks(len(towers[0].data), towers[1], towers[2])

	print towers[1].data