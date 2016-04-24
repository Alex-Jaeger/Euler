
def isPandigital(num_str):
    str_length = len(num_str)
    pan_total = 0

    for i in range(1, str_length+1):
        if str(i) not in num_str:
            return 0
    return 1

def calcDigitSum(num_str):
    num_str = str(num_str)
    digit_sum = 0

    for charDigit in num_str:
        digit_sum += int(charDigit)

    return digit_sum

pandigital_prod = []

for a in range(10000):
    for b in range(10000):
        product = a * b
        equ_str = "" + str(product) + str(a) + str(b)

        if len(equ_str) == 9:
            if product not in pandigital_prod:
                if isPandigital(equ_str) == 1:
                    pandigital_prod.append(product)

result = sum(pandigital_prod)
print result
