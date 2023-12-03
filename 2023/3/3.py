file_path = "3.txt"


def read_number_and_erase_it(grid, i, j):
    number = 0
    left_offset = 0
    right_offset = 0
    while j - left_offset >= 0 and str.isdigit(grid[i][j - left_offset]):
        left_offset += 1
    while j + right_offset < len(grid[i]) and str.isdigit(grid[i][j + right_offset]):
        right_offset += 1
    number = int(grid[i][j - left_offset + 1 : j + right_offset])
    for k in range(j - left_offset + 1, j + right_offset):
        grid[i] = grid[i][:k] + "." + grid[i][k + 1 :]
    return number


def read_numbers_near_symbol(grid, i, j):
    numbers = []
    for k in range(-1, 2):
        for l in range(-1, 2):
            if i + k >= 0 and i + k < len(grid) and j + l >= 0 and j + l < len(grid[i]):
                if str.isdigit(grid[i + k][j + l]):
                    numbers.append(read_number_and_erase_it(grid, i + k, j + l))
    return numbers


def part_1():
    with open(file_path, "r") as file:
        grid = []
        for line in file:
            grid.append(line.strip())

    numbers = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (not str.isdigit(grid[i][j])) and grid[i][j] != ".":
                print("symbol found", grid[i][j], "at", i, j)
                new_numbers = read_numbers_near_symbol(grid, i, j)
                numbers.append(new_numbers)
    print(sum([sum(x) for x in numbers]))


def part_2():
    with open(file_path, "r") as file:
        grid = []
        for line in file:
            grid.append(line.strip())

    numbers = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == "*":
                print("gear found", grid[i][j], "at", i, j)
                new_numbers = read_numbers_near_symbol(grid, i, j)
                numbers.append(new_numbers)
    print(sum([0 if len(x) != 2 else (x[0] * x[1]) for x in numbers]))


part_2()
