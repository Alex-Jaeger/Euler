
def getTriangleNumber(n):
    triNumber = 0

    for i in range(n, 0, -1):
        triNumber += i

    return triNumber

def getNumDivisor(n):
    numDivisors = 0

    for i in range(n, 0, -1):
        if(n % i == 0):
            numDivisors += 1

    return numDivisors

divisorCount = 0
triNumber = 0
i = 1

while(divisorCount <= 500):
    triNumber = getTriangleNumber(i)
    divisorCount = getNumDivisor(triNumber)
    i += 1

    print divisorCount

print triNumber
