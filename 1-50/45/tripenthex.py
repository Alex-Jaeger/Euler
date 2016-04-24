def triangle(n):
    return (n * (n + 1)) / 2

def pentagonal(n):
    return (n * ((3 * n) - 1)) / 2

def hexagonal(n):
    return (n * ((2 * n) - 1))

tri_inc = 1
pent_inc = 1
hex_inc = 1

while True:
    tri = triangle(inc)
    pent = pentagonal(inc)
    hexa = hexagonal(inc)
