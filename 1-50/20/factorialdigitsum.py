
import math

factorial_str = str(math.factorial(100))
result = 0

for char in factorial_str:
    result += int(char)

print result
