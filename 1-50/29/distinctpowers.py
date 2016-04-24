
result_set = []

for a in range (2, 101):
    for b in range (2, 101):
        if((a ** b) not in result_set):
            result_set.append(a ** b)

result = len(result_set)

print result
