'''
1. Layer by layer, move left to top, bottom to right
2. Need to pay attention to corner part, in case it rotate twice
'''

def rotate(inputArray):
	matN = len(inputArray)
	for i in xrange(0, matN/2):
		
		first = i
		end = matN - first 

		#The Corner
		inputArray[end-1][first], inputArray[first][end - 1] = inputArray[first][end - 1], inputArray[end-1][first]

		for j in xrange(first+1, end-1):
			inputArray[j][first], inputArray[first][j] = inputArray[first][j], inputArray[j][first]
			inputArray[j][end-1], inputArray[end-1][j] = inputArray[end-1][j], inputArray[j][end-1]


	return inputArray


if __name__ == '__main__':
	testArray = [[3, 5, 3, 1, 4],
      			 [3, 2, 1, 5, 6],
     			 [4, 1, 2, 2, 5],
     			 [1, 2, 4, 5, 6],
      			 [4, 3, 6, 6, 3]]
	testArrayRst = [[3, 3, 4, 1, 4],
			        [5, 2, 1, 2, 3],
			        [3, 1, 2, 4, 6],
			        [1, 5, 2, 5, 6],
			        [4, 6, 5, 6, 3]]

	
	print rotate(testArray)
