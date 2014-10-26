

def sieveErato(limit, primes):
    multiples = set()
    for i in range(2, limit + 1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, limit + 1, i))

primes = []
sieveErato(2000000, primes)

print sum(primes)
