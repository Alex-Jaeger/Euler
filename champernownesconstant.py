
num_str = ""

for i in range(1000001):
    num_str += str(i)

result = 1

for i in range(7):
    result *= int(num_str[10 ** i])
print result
