
triangle_file = open("./data/maximumpathsum1_triangle.txt", "r")
number_triangle = []

for line in triangle_file:
    numbers = line.strip().split(' ')
    for num in numbers:
        number_triangle.append(int(num))

k = 0
path_sum = number_triangle[k]

while True:
    if number_triangle[2 * k + 1] >= number_triangle[k]:
        path_sum += number_triangle[2 * k + 1]
        print number_triangle[2 * k + 1]
        k = 2 * k + 1

    else:
        path_sum += number_triangle[2 * k + 2]
        print number_triangle[2 * k + 2]
        k = 2 * k + 2


print path_sum
