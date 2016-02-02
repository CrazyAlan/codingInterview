'''
reverse string
1. Using traditional method, reverse between middle one
2. Using recursive function, return "" at final step
'''

def tReverse(inputString):
	rst = list(inputString)
	start = 0
	end = len(inputString)-1

	while start < end:	
		rst[start], rst[end]  = rst[end], rst[start]
		start += 1
		end -= 1
	return "".join(rst)

def rReverse(inputString):
	if inputString != "":
		return inputString[-1:] + rReverse(inputString[:-1])
	else:
		return ""

if __name__ == '__main__':
	palindrome = "abcdedcba"
	nonpalindrome = "hello!"

	if palindrome == rReverse(palindrome):
		print "Test 1 passed"
	if nonpalindrome != rReverse(nonpalindrome):
		print "Test 2 passed"