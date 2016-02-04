'''
1. Using BFS as to use queue to traverse the graph
2. Using DFS as to use stack to traverse the graph
3. Dynamic programming is need to perform *****
'''
from collections import deque
import copy


status = ['unvisited', 'visiting', 'visited']
class GraphNode():
	"""docstring for DirectGraph"""
	def __init__(self, index):
		self.index = index
		self.neighbours = []
		self.status = status[0]
	def __str__(self):
		return str(self.index)

def DFSFind(start, end):
	if start == end:
		return True

	start.status = status[1]
	stackNodeForCheck = []
	stackNodeForCheck.append(start)

	while stackNodeForCheck: #node waiting for checking is not None	
		checkingNode = stackNodeForCheck.pop()
		for i in checkingNode.neighbours:
			if i == end:
				return True
			elif i.status == status[0]:
				i.status = status[1]
				stackNodeForCheck.append(i)
			else: #Visited Node or visiting node
				continue
		checkingNode.status = status[2] #Visited
	return False

def BFSFind(start, end):
	if start == end:
		return True
	queueNodeForChecking = deque([])
	queueNodeForChecking.append(start)

	while queueNodeForChecking:
		checkingNode = queueNodeForChecking.popleft()
		for i in checkingNode.neighbours:
			if i == end:
				return True
			elif i.status == 'unvisited':
				i.status = 'visiting' #put into queue
				queueNodeForChecking.append(i)
			else: # visited or visiting node 
				continue 

		checkingNode.status = 'visited'
	return False


if __name__ == '__main__':
	node = []
	for x in xrange(0,6):
		node.append(GraphNode(x))


	node[0].neighbours.append(node[1])
	node[0].neighbours.append(node[3])
	#node[3].neighbours.append(node[2])
	node[3].neighbours.append(node[4])
	node[4].neighbours.append(node[5])

	node2 = copy.deepcopy(node)

	print DFSFind(node[0], node[2])
	print BFSFind(node2[0], node2[2])




				




