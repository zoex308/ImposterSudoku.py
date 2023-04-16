grid_size = 9
def print_puzzle(a):
    print(' ' * 6, '|', ' ' * 5, '|')
    for i in range(grid_size):
        print(end=" ")
        for j in range(grid_size):
            if j > 0 and j % 3 == 0: print("| ", end = "")
            print(a[i][j],end = " ")
        print()
        if i < 8 and (i + 1) % 3 == 0: print('-' * 23)
    print(' ' * 6, '|', ' ' * 5, '|')

def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
            
    return True
 
def solve_puzzle(grid, row, col):
    if (row == grid_size - 1 and col == grid_size):
        return True
    
    if col == grid_size:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve_puzzle(grid, row, col + 1)
    
    for num in range(1, grid_size + 1, 1): 
        if solve(grid, row, col, num):
            grid[row][col] = num

            if solve_puzzle(grid, row, col + 1):
                return True
            
        grid[row][col] = 0

    return False

color_map = {
    'Y': "yellow",
    'R': "red",
    'W': "white",
    'I': "pink",
    'P': "purple",
    'B': "black",
    'N': "brown",
    'E': "blue",
    'C': "cyan",
    'O': "orange",
    'L': "lime"
}

orig_grid ="""
Y-R-WIP-B
-N-------
-PEN-----
P--YB--IW
RYW-E---N
-I---W-CY
-W-C-OY-R
NO--IL-WP
B----Y--I
"""

all_colors = []

for i in range(len(orig_grid)):
    color = orig_grid[i]
    if color not in all_colors:
        all_colors.append(color)

all_colors.remove('-')
all_colors.remove('\n')

for first_color_index in range(len(all_colors)):
    first_color = all_colors[first_color_index]
    for second_color_index in range(first_color_index + 1, len(all_colors)):
        second_color = all_colors[second_color_index]

        all_colors_set = set(all_colors)

        curr_grid = orig_grid
        curr_colors = all_colors_set - {first_color, second_color}

        num = 1
        color2num = {}
        num2color = {}

        for color_again in curr_colors:
            color2num[color_again] = num
            num2color[num] = color_again
            curr_grid = curr_grid.replace(color_again, str(num))
            num += 1

        curr_grid = curr_grid.replace(first_color, '0')
        curr_grid = curr_grid.replace(second_color, '0')
        curr_grid = curr_grid.replace('-', '0')
        grid_split = curr_grid.split('\n')[1 : -1]

        grid = []

        for line in grid_split:
            row = []
            for character in line:
                row.append(int(character))
            grid.append(row)

        if (solve_puzzle(grid, 0, 0)):
            for row in range(len(grid)):
                for col in range(len(grid)):
                    grid[row][col] = num2color[grid[row][col]]

            print(f"\nSolution found for imposters: {first_color}, {second_color}!")
            print_puzzle(grid)
            print()
        else:
            print(f"Solution not found for imposters: {first_color}, {second_color}. They are not the imposters.")