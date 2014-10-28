
pandigital_primes = []

def isPandigital(num_str):
    str_length = len(num_str)
    pan_total = 0

    for i in range(1, str_length+1):
        if str(i) not in num_str:
            return 0

    return 1

def sieveErato(limit):
    multiples = set()
    prime_num = 0

    for i in range(2, limit + 1):
        if i not in multiples:
            prime_num += 1

            if isPandigital(str(i)) == 1:
                pandigital_primes.append(i)

            multiples.update(range(i * i, limit + 1, i))

sieveErato(10000000)
result = max(pandigital_primes)
print result
