import sys

def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m - 1, 1)
    elif m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))

sys.setrecursionlimit(11500)

result = 0

result += A(5, 5)

result = result % (14 ** 8)

print result
