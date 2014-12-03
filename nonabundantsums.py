def d(n):
    divisor_sum = 0
    for i in range(1, (n / 2) + 1):
        if (n % i) == 0:
            divisor_sum += i
    return divisor_sum

def isAbundant(n):
	if(d(n) > n):
		return True

print isAbundant(12)


cur_num = 0
max_num = 30

while cur_num <= max_num:
	print "abundant: " + str(cur_num) + str(isAbundant(cur_num))
	cur_num += 1

#while cur_num <= max_num:
