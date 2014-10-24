
def A(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m - 1, 1)
    elif m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))

result = 0

for i in range(0,6):
    result += A(i, i)

result = result % (14 ** 8)

print result
