

def reverseInt(n):
	return int(str(n)[::-1])

def isPalindrome(n):
	if n == reverseInt(n):
		return True
	return False

def isLychrel(n):
	#if(n >= 10000):
	#	return False

	revSum = n + reverseInt(n)

	if isPalindrome(revSum):
		print revSum
		return True
	
	return isLychrel(revSum)

print isLychrel(10677)
# print numLychrel