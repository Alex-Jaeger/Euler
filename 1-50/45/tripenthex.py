def triangle(n):
    return (n * (n + 1)) / 2

def pentagonal(n):
    return (n * ((3 * n) - 1)) / 2

def hexagonal(n):
    return (n * ((2 * n) - 1))

tri_i = 285
while True:
    tri = triangle(tri_i)
    tri_i += 1

    pent_i = 0
    found_pent = False
    while True:
        if (pentagonal(pent_i) < tri):
            pent_i += 1
        elif (pentagonal(pent_i) == tri):
            found_pent = True
            break
        elif (pentagonal(pent_i) > tri):
            found_pent = False
            break

    if found_pent == False:
        continue

    hex_i = 0
    found_hex = False
    while True:
        if (hexagonal(hex_i) < tri):
            hex_i += 1
        elif (hexagonal(hex_i) == tri):
            found_hex = True
            break
        elif (hexagonal(hex_i) > tri):
            found_hex = False
            break

    if found_pent == True and found_hex == True:
        if (tri_i - 1) != 285:
            print "Triangle n: " + str(tri_i - 1)
            print "Pentagon n: " + str(pent_i)
            print "Hexagonal n: " + str(hex_i)
            print "Triangle value: " + str(tri)
            break
