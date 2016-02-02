'''
Test Case: Null, Empty, aaa, aabb, abababa
1. O(n^2), with few variable 
2. O(n), with constant array 
3. Use one int variable as indicator
'''

def func1(inputString):
	if not inputString:
		return 

	for x in range(0, len(inputString)):
		for y in range(0, len(inputString)):
			if x != y:
				if inputString[x] == inputString[y]:
					return False
	return True

def func2(inputString):
	if not inputString:
		return

	charSet = [False]*256

	for x in inputString:
		if ord:
			pass


if __name__ == '__main__':
	postive = "abcdefg"
	negtive = "ababab"

	if func1(postive):
		print "Test 1 Passed"
	else:
		print "Test 1 Failed"

	if not func1(negtive):
		print "Test 2 Passed"
	else:
		print "Test 2 Failed"