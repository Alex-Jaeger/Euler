
def checkMultiple(num):
    divisible = 0

    for i in range(1, 21):
        if num % i == 0:
            divisible += 1

    if divisible == 20:
        return 1
    else:
        return 0

cur_num = 20

while checkMultiple(cur_num) == 0:
    print cur_num
    cur_num += 1

print cur_num
