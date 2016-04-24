
import math

result = 0

i = 0
j = 1

while j < 4000000:

    fibo_num = i + j

    if fibo_num % 2 == 0:
        result += fibo_num

    i = j
    j = fibo_num

print result
