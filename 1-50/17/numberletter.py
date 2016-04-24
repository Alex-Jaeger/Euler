
from num2words import num2words

result = 0

for i in range(1, 1001):
    num_word = num2words(i)
    num_word = num_word.replace(" ", "")
    num_word = num_word.replace("-", "")
    result += len(num_word)

print result
