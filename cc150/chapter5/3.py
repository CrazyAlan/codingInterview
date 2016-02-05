'''
1. Get the next largest value, simply scan from right to left, turn on zero next to one, then turn off that one, then move right part to most right
2. Get the next smallest value, simply scan from right to left, turn off 1 next to zero, then turn on this zero, then move ones to next to this one 
3. Need a counter to count how many ones need to be assign at last 
'''

def getBit(n, index):
	return (n & (1<<index)) > 0

def setBit(n, index, flag):
	if flag: # 1 	
		return  n | 1<<index
	else:
		return  n & (~(1<<index))

def findNextLargest(n):
	onesCount = 0
	index = 0
	while not getBit(n, index): #zeros
		index += 1

	#Now index is the first one
	
	while getBit(n, index) :
		onesCount += 1 #include the first one, count all the ones between first one and another zeros
		index += 1
	
	#Now index is the zero
	
	#Set this zero to one
	n = setBit(n, index, True)
	#Set next one to zero
	n = setBit(n, index-1, False) 

	#Now set all right to zeros 
	for i in range(0, index-1): #to index-2 zeros
		n = setBit(n, i, False)

	#Now set right most as ones
	for i in range(0, onesCount-1): # onesCount -1 ones 
		n = setBit(n, i, True)

	return n

if __name__ == '__main__':
	a = 3
	print findNextLargest(a)
