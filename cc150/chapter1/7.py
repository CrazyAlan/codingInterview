'''
1. If we go through the entire matrix, then assign the rows and cols with 0 to all zeros,
then the entire matrix would become all zeros
2. If we use a matrix M*N to store all the 0 positions, then we need o(MN) space, which is not necessary
3. Using row and col array to store which row or col have zero, then assign zero to that column or rows 
'''

def assignZeros(inputMat):
	M = len(inputMat) #rows
	N = len(inputMat[0]) #cols

	rows = [0]*M
	cols = [0]*N

	for i in xrange(0, M):
		for j in xrange(0, N):
			if inputMat[i][j] == 0:
				rows[i] = 1
				cols[j] = 1

	for i in xrange(0, M):
		for j in xrange(0, N):
			if rows[i] or cols[j]:
				inputMat[i][j] = 0

	return inputMat


if __name__ == '__main__':
	testMat = [[2, 2, 2, 5],
		       [3, 0, 6, 4],
		       [3, 1, 5, 3],
		       [4, 3, 4, 0],
		       [4, 1, 5, 5]]
	print assignZeros(testMat)
