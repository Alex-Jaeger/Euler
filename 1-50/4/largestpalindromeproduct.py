
def checkNumber(n):
    string_n = str(n)

    if string_n[::-1] == string_n[::1]:
        return 1
    else:
        return 0



result = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if checkNumber(i*j) == 1:
            if i*j > result:
                result = i*j

print result
