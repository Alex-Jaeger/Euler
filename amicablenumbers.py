
def d(n):
    divisor_sum = 0
    for i in range(1, (n / 2) + 1):
        if (n % i) == 0:
            divisor_sum += i
    return divisor_sum

result = 0
for a in range(1, 10001):
    for b in range(1, 10001):
        if (d(a) == b) and (d(b) == a) and (a != b):
            result += a
            result += b

print result
