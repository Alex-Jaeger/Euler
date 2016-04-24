
grid_file = open("data.txt", "r")

grid = [[0 for x in xrange(20)] for x in xrange(20)]

def inGrid(x, y):
    if (x >= 0 and x < 20):
        if (y >= 0 and y < 20):
            return True
    return False

cur_row = 0
for line in grid_file:
    grid_row = line.split(" ")

    cur_col = 0
    for num in grid_row:
        grid[cur_row][cur_col] = int(num)
        cur_col += 1
    cur_row += 1

directions = [
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [-1, 0], [-2, 0], [-3, 0]],
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [0, -1], [0, -2], [0, -3]],
    [[0, 0], [1, 1], [2, 2], [3, 3]],
    [[0, 0], [-1, -1], [-2, -2], [-3, -3]],
    [[0, 0], [1, -1], [2, -2], [3, -3]],
    [[0, 0], [-1, 1], [-2, 2], [-3, 3]]
]

products = []
for i in range(20):
    for j in range(20):
        cell = [i, j]

        for direction in directions:
            line_product = 1

            for delta in direction:
                temp_x = cell[0]
                temp_y = cell[1]

                temp_x += delta[0]
                temp_y += delta[1]

                if inGrid(temp_x, temp_y):
                    line_product *= grid[temp_x][temp_y]

            products.extend([line_product])

print(max(products))
