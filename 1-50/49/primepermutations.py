from itertools import permutations

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i*i < n:
        if n % i == 0 or n % (i + 2) == 0 :
            return False
        i += 6

    return True

for n in range(1000, 3339):
    if (isPrime(n)):
        perms = {}

        perm = ''
        for p in permutations(str(n)):
            perms[int(''.join(p))] = None

        n1 = n
        n2 = n1 + 3330
        n3 = n2 + 3330

        # are n1, n2, n3 permutations of n?
        if n1 in perms and n2 in perms and n3 in perms:
            # are n1, n2, n2 primes?
            if isPrime(n1) and isPrime(n2) and isPrime(n3):
                # The question states there are two possibilities, eliminate the first 
                if n1 != 1487:
                    print str(n1) + str(n2) + str(n3)
