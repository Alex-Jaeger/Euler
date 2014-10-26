
digitfifth = []

for cur_num in range(1000, 1000001):
    num_str = str(cur_num)
    digit_sum = 0

    for char_digit in num_str:
        digit_sum += int(char_digit) ** 5

    if digit_sum == int(num_str):
        digitfifth.append(int(num_str))

print sum(digitfifth)
