def get_adj_nums(grid: list[list[str]], i: int, j: int) -> list[int]:
    result = []

    points = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for row, col in points:
        if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col].isdigit():
            result.append(get_rest_of_num(grid, row, col))
    
    return result


def get_rest_of_num(grid: list[list[str]], i: int, j: int) -> int:
    builder = grid[i][j]
    grid[i][j] = "."
    ptr1 = j-1
    ptr2 = j+1
    while ptr1 >= 0 and grid[i][ptr1].isdigit():
        builder = grid[i][ptr1] + builder
        grid[i][ptr1] = "."
        ptr1 -= 1

    while (ptr2 < len(grid[i]) and grid[i][ptr2].isdigit()):
        builder += grid[i][ptr2]
        grid[i][ptr2] = "."
        ptr2 += 1

    return int(builder)


def parse_grid(file_name: str) -> list[list[str]]:
    with open(file_name) as f:
        return [[c for c in line.strip()] for line in f.readlines()]
    


if __name__ == "__main__":
    not_symbols = "1234567890."
    grid = parse_grid("input.txt")
    total = 0

    for idx, row in enumerate(grid):
        for jdx, col in enumerate(row):
            if col not in not_symbols:
                nums = get_adj_nums(grid, idx, jdx)
                for n in nums:
                    total += n
    
    print(total)
