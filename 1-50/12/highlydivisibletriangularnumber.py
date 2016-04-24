import math

def triangleNumber():
    n = 0

    while True:
        n += 1
        triNumber = 0

        for i in range(1, n+1):
            triNumber += i

        yield triNumber

def getNumDivisor(n):
    numDivisors = 0

    for i in range(int(math.sqrt(n)), 0, -1):
        if(n % i == 0):
            numDivisors += 1

    return numDivisors * 2

tri_generator = triangleNumber()
triNumber = 0
divisorCount = 0

while(divisorCount <= 500):
    triNumber = next(tri_generator)
    divisorCount = getNumDivisor(triNumber)

print triNumber
