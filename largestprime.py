
import math

n = 600851475143
result = 0

for i in range(3, int(round(math.sqrt(n))), 2):
    while n % i == 0:
        if i > result:
            result = i

        n = n / i

print result
