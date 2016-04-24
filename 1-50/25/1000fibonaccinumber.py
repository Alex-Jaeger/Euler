
n1 = 0
n2 = 1

result = 1

while True:
    fibo_num = n1 + n2
    fibo_str = str(fibo_num)

    result += 1

    if(len(fibo_str) >= 1000):
        break

    n1 = n2
    n2 = fibo_num

print result
