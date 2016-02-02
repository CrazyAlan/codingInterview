'''
1. Ask the string is ASCII or not, as ASCII use 256 numbers
2. If the char only vary from 'a to z', then it could use bitwise operation
3. Use two iterative method to do it, O(n^2)
4. If allowed to use extra space, use sort algorithm to sort, then compare neighbour chars
'''

def uniqueAscii(inputString):
	charSet = [False]*256

	for i in inputString:
		if charSet[ord(i)]:
			return False
		else:
			charSet[ord(i)] = True

	return True


def uniqueAZ(inputString):
	checker = 0

	for i in inputString:
		if checker & 1<<(ord(i)-ord('a')):
			return False
		else:
			checker |= 1<<(ord(i)-ord('a'))

	return True

if __name__ == '__main__':
	positiveCase = "abcdefghijklmn"
	negativeCase = "adbde"
	funcs = [uniqueAscii, uniqueAZ]
	for func in funcs:
		if func(positiveCase):
			print "Test 1 passed"
		else:
			print "Test 1 failed"

		if not func(negativeCase):
			print "Test 2 passed"
		else:
			print "Test 2 failed"




			
