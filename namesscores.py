
names_file = open("./data/namesscores_names.txt")
names = [name.replace('"', '') for name in names_file.readlines()[0].split(',')]

names = sorted(names)

result = 0
for i in range(0,len(names)):
    result += sum([ord(character) for character in names[i]]) * (i + 1)

print result
