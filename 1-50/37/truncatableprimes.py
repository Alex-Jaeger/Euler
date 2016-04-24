
def gen_primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def trunc_left(n):
    str_n = str(n)
    return int(str_n[1::])

def trunc_right(n):
    str_n = str(n)
    return int(str_n[:-1])

truncatable_primes = []

prime_gen = gen_primes()
while (len(truncatable_primes) < 11):
    prime = int(next(prime_gen))

    if prime <= 7:
        continue

    is_truncatable_prime_l = False
    trunc_prime = prime

    while True:
        trunc_prime = trunc_left(trunc_prime)
        if (isPrime(trunc_prime)):
            is_truncatable_prime_l = True
            if (trunc_prime < 10):
                break
        else:
            is_truncatable_prime_l = False
            break

    is_truncatable_prime_r = False
    trunc_prime = prime

    while True:
        trunc_prime = trunc_right(trunc_prime)

        if (isPrime(trunc_prime)):
            is_truncatable_prime_r = True
            if (trunc_prime < 10):
                break
        else:
            is_truncatable_prime_r = False
            break

    if is_truncatable_prime_l == True and is_truncatable_prime_r == True:
        truncatable_primes.extend([prime])

print sum(truncatable_primes)
