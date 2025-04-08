def initialize_grid():
    print('initialize grid')
    length_grid = int(input('please input the side length of the field grid for revolution'))
    init_grid = [[0 for _ in range(length_grid)] for _ in range(length_grid)]
    print("enter initial grid row by row: use '1' for alive and '0' for dead")
    for i in range(length_grid):
        row = input(f'input either 0 or 1 for row {i + 1} of grid')
        cells = row.split()
        if len(cells) != length_grid:
            print(f'Invalid input. Row {i + 1} must contain exactly {length_grid} values')
        for j, cell in enumerate(cells):
            if cell not in ['0', '1']:
                print(f"Invalid input {cell} in row {i + 1}. Use only '0' or '1'.")
            init_grid[i][j] = int(cell)
    print(init_grid)
    return init_grid


def initialize_rules():
    print('initialize rules')
    survive_min = int(input('minimum neighboring cells for a cell to survive'))
    survive_max = int(input('maximum neighboring cells equal or below which a cell can survive'))
    birth = int(input('neighbors required for birth of a cell'))
    init_rules = {
        'survive_min': survive_min,
        'survive_max': survive_max,
        'birth': birth
    }
    print(init_rules)
    return init_rules


def count_neighbors(count_grid, row, col):
    count = 0
    length_grid = len(count_grid)
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            if 0 <= row + i < length_grid and 0 <= col + j < length_grid:
                count += count_grid[row + i][col + j]
    return count


def next_generation(past_grid, rule):
    length_grid = len(past_grid)
    new_grid = [[0 for _ in range(length_grid)] for _ in range(length_grid)]
    for i in range(length_grid):
        for j in range(length_grid):
            if past_grid[i][j] == 1:
                if rule['survive_min'] <= count_neighbors(past_grid, i, j) <= rule['survive_max']:
                    new_grid[i][j] = 1
            else:
                if count_neighbors(past_grid, i, j) == rule['birth']:
                    new_grid[i][j] = 1
    print(new_grid)
    return new_grid


def print_grid(new_grid):
    length_grid = len(new_grid)
    printed_grid = [['' for _ in range(length_grid)] for _ in range(length_grid)]
    for i in range(length_grid):
        for j in range(length_grid):
            if new_grid[i][j] == 0:
                printed_grid[i][j] = '□'
                # the use of the ASCII character □ is the idea of DeepSeek
            if new_grid[i][j] == 1:
                printed_grid[i][j] = '■'
                # the use of the ASCII character ■ is the idea of DeepSeek
    for t in range(length_grid):
        print(printed_grid[t])
    return printed_grid


def start_simulation():
    grid = initialize_grid()
    rules = initialize_rules()
    iterations = int(input("Number of iterations: "))

    for k in range(iterations):
        grid = next_generation(grid, rules)
        print(f"\nGeneration {k + 1}:")
        print_grid(grid)

        cmd = input("Press Enter to continue, input 'reset' to restart, or 'quit' to exit: ")
        if cmd == "reset":
            start_simulation()
            return
        elif cmd == "quit":
            return


print("Welcome to the adapted version of Conway's Game of Life!", "\n", "There you will be able to "
      "customize rules, start points, and to pause, restart, or quit at any time; and you will be able to see"
      "the result of evolution.")
start_simulation()
