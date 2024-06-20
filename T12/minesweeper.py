
#Gets the number of mines around the postion (row,col)
def mine_num(row, col):
    num_mines = 0
    #                NW        N        NE       W       E        SW      S       SE
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x, y in directions:
        new_row, new_col = row + x, col + y
        #The if below looks for "#" within the grid boundaries and increments by 1 if a mine is found
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "#":
            num_mines += 1
    return num_mines

grid=[["-","-","-","#","#"],
      ["-","#","-","-","-"],
      ["-","-","#","-","-"],
      ["-","#","#","-","-"],
      ["-","-","-","-","-"]]

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "-":
            num = mine_num(row, col)
            grid[row][col] = str(num)

#Prints the new grid with the number of mines that are close
for row in grid:
    print(" ".join(row))


             
