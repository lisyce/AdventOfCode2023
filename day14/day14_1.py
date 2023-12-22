def parse_grid(filename: str) -> list[list[str]]:
    result = []
    with open(filename) as f:
        for line in f:
            result.append([c for c in line.strip()])

    return result


def roll_rocks_north(grid: list[list[str]]) -> None:
    for idx, row in enumerate(grid):
        for jdx, col in enumerate(row):
            if col != "O":
                continue

            row[jdx] = "."
            ptr = idx
            while ptr > 0 and grid[ptr - 1][jdx] == ".":
                ptr -= 1
            grid[ptr][jdx] = "O"


def calculate_load(grid: list[list[str]]) -> int:
    total = 0
    for i, row in enumerate(grid):
        num_round_rocks = sum(1 for x in row if x == "O")
        total += num_round_rocks * (len(grid) - i)
    return total

if __name__ == "__main__":
    grid = parse_grid("input.txt")
    roll_rocks_north(grid)
    
    print(calculate_load(grid))