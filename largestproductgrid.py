
grid_file = open("./data/largestproductgrid_grid.txt","r")

grid = [[0 for x in xrange(20)] for x in xrange(20)]

cur_row = 0
for line in grid_file:
    grid_row = line.split(" ")

    cur_col = 0
    for num in grid_row:
        grid[cur_row][cur_col] = num
        cur_col += 1

    cur_row += 1

print(grid)
