
import math

def sieveErato(limit):
    multiples = set()
    prime_num = 0

    for i in range(2, limit + 1):
        if i not in multiples:
            prime_num += 1

            if prime_num >= 10001:
                return i

            multiples.update(range(i * i, limit + 1, i))


print sieveErato(1000000)
