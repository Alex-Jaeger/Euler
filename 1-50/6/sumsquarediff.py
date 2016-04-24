
sumsquare = 0
for i in range(101):
    sumsquare += i ** 2

squaresum = 0
for i in range(101):
    squaresum += i

squaresum = squaresum ** 2

diff = squaresum - sumsquare

print diff
