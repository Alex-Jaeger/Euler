
def isPandigital(num_str):
    str_length = len(num_str)
    pan_total = 0

    for i in range(1, str_length+1):
        if str(i) not in num_str:
            return 0

    return 1

base = 1
prod_9 = []

while base < 10000:
    prod_str = ""
    n = 1

    while len(prod_str) < 9:
        prod_str += str(base * n)
        n += 1

    if len(prod_str) == 9:
        if(isPandigital(prod_str) == 1):
            prod_9.append(int(prod_str))

    base += 1

result = max(prod_9)
print result
