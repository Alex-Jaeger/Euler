
number_file = open("./data/largesum_number.txt")


result = 0
for line in number_file:
    result += int(line)


print str(result)[:10]
