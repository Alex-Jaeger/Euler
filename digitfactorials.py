
import math

result = 0

for i in range(3, 1000000):
    num_str = str(i)

    digitfactorial = 0
    for digit in num_str:
        digitfactorial += math.factorial(int(digit))

    if(digitfactorial == i):
        result += i

print result
