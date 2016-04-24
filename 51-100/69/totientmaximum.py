import fractions

def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount

ratiomax = 0.0
maxn = 0

for n in range(1, 1000001):
	value = (n * 1.0) / phi(n)

	if value > ratiomax:
		ratiomax = value
		maxn = n

print maxn