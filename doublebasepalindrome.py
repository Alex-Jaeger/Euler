
def checkPalindrome(numstr):
    if numstr[::1] == numstr[::-1]:
        return 1

def convertToBinary(num):
    if num <= 1:
        return num
    return str(convertToBinary(num / 2)) + str(num % 2)

palindromes = []
for i in range(1, 1000001):
    if checkPalindrome(str(i)) == 1:
        if checkPalindrome(str(convertToBinary(i))) == 1:
            palindromes.append(i)

print sum(palindromes)
