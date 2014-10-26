
def triangleNumbers(limit):
    for n in range(1, limit * 5):
        if ((n * (n + 1)) / 2) == limit:
            return n
    return 0

def getSum(word):
    word_sum = 0
    for char in word:
        word_sum += ord(char) - ord("@")
    return word_sum

word_file = open("./data/trianglenumbers_words.txt")
words = word_file.read().replace("\"", "").split(",")

word_count = 0
for word in words:
    if triangleNumbers(getSum(word)) != 0:
        word_count += 1
print word_count
