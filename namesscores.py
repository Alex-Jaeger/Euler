
names = [name.replace('"', '') for name in open("./data/namesscores_names.txt").readlines()[0].split(',')]

names = sorted(names)
result = 0

for i in range(0, len(names)):
    char_sum = 0

    for character in names[i]:
        char_sum += (ord(character) - ord('@'))

    result += (char_sum * (i+1))

print result
