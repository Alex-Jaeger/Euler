
def isPandigital(num_str):
    str_length = len(num_str)
    pan_total = 0

    for i in range(1, str_length+1):
        if str(i) not in num_str:
            return 0
    return 1
