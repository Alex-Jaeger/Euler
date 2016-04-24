
amicableNumbers = []

def d(n):
    divisor_sum = 0
    for i in range(1, (n / 2) + 1):
        if (n % i) == 0:
            divisor_sum += i
    return divisor_sum

def isAmicable(n):
	if(d(d(n)) == n):
		return True

cur_num = 1
while cur_num < 10000:
	if isAmicable(cur_num):
		if cur_num not in amicableNumbers:
			amicableNumbers.append(cur_num)

	cur_num += 1

result = sum(amicableNumbers)
print result
