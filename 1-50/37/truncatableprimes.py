

def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def trunc_left(n):
    str_n = str(n)
    return int(str_n[1::])

def trunc_right(n):
    str_n = str(n)
    return int(str_n[::-1])

print trunc_right(155)
print isPrime(13)

n = 7

num = 0
num_sum = 0

while(num < 11):

    l_r = 0
    l_r_n = n

    r_l = 0
    r_l_n = n

    while len(str(l_r_n)) > 1:
        if(isPrime(l_r_n)):
            l_r_n = trunc_left(l_r_n)
        else:
            break

        if(isPrime(l_r_n)):
            l_r_n = trunc_right(l_r_n)
        else:
            break

    if(len(str(l_r_n)) > 1):
        l_r = 0
    else:
        l_r = 1

    while len(str(r_l_n)) > 1:
        if(isPrime(r_l_n)):
            r_l_n = trunc_left(r_l_n)
        else:
            break

        if(isPrime(l_r_n)):
            r_l_n = trunc_right(r_l_n)
        else:
            break

    if(len(str(r_l_n)) > 1):
        r_l = 0
    else:
        r_l = 1

    if(r_l == 1 & l_r == 1):
        num += 1
        num_sum += n

    n += 1

print num_sum
