
number_file = ''.join([line.strip() for line in open("./data/largestproduct_number.txt", "r").readlines()])

result = 0

for i in range(0, len(number_file) - 13, 1):
    nums = number_file[i:i+13]

    product = 1
    for num in nums:
        product *= int(num)

    if product > result:
        result = product

print result
