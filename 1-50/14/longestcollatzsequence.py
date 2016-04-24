
termCount = 1

def even(n):
    global termCount

    termCount += 1
    return n / 2

def odd(n):
    global termCount

    termCount += 1
    return (3 * n) + 1

def rec_func(n):
    if(n == 1):
        return None

    if(n % 2 == 0):
        rec_func(even(n))

    else:
        rec_func(odd(n))

longest_seq = 0
longest_num = 0

for i in range(1000000, 1, -1):
    rec_func(i)

    if(termCount >= longest_seq):
        longest_seq = termCount
        longest_num = i

    print(i)

    termCount = 1

print(longest_num)
