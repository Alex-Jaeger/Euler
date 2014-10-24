
def phi(n):
    phi = 1
    # p == prime number
    for i in range(0, int(end) + 1):
        phi *= (n * (1 - (1 / i)))

    return phi

print phi(36)
