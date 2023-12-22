from day14_1 import parse_grid, roll_rocks_north, calculate_load
from tqdm import tqdm

def roll_rocks_west(grid: list[list[str]]) -> None:
    for idx, row in enumerate(grid):
        for jdx, col in enumerate(row):
            if col != "O":
                continue

            row[jdx] = "."
            ptr = jdx
            while ptr > 0 and grid[idx][ptr - 1] == ".":
                ptr -= 1
            grid[idx][ptr] = "O"


def roll_rocks_east(grid: list[list[str]]) -> None:
    for idx, row in enumerate(grid):
        for jdx in range(len(grid[0]), 0, -1):
            col = row[jdx - 1]
            if col != "O":
                continue

            row[jdx - 1] = "."
            ptr = jdx - 1
            while ptr < len(grid[0]) - 1 and grid[idx][ptr + 1] == ".":
                ptr += 1
            grid[idx][ptr] = "O"


def roll_rocks_south(grid: list[list[str]]) -> None:
    for idx in range(len(grid), 0, -1):
        row = grid[idx-1]
        for jdx, col in enumerate(row):
            if col != "O":
                continue

            row[jdx] = "."
            ptr = idx - 1
            while ptr < len(grid) - 1 and grid[ptr + 1][jdx] == ".":
                ptr += 1
            grid[ptr][jdx] = "O"


def spin_cycle(grid: list[list[str]]) -> None:
    roll_rocks_north(grid)
    roll_rocks_west(grid)
    roll_rocks_south(grid)
    roll_rocks_east(grid)


def copy_grid(grid: list[list[str]]) -> list[list[str]]:
    result = []
    for row in grid:
        result.append([c for c in row])
    return result


if __name__ == "__main__":
    grid = parse_grid("input.txt")

    seen_grids = []
    pattern_length = 0
    cycles_until_repeat = 0

    for i in range(1000000000):
        original = copy_grid(grid)
        seen_grids.append(original)
        spin_cycle(grid)

        if grid in seen_grids:
            last_seen_idx = seen_grids.index(grid)
            pattern_length = i-last_seen_idx + 1
            cycles_until_repeat = i - pattern_length
            break

    remainder_cycles = (1000000000 - 1 - i) % pattern_length
    for i in range(remainder_cycles):
        spin_cycle(grid)
    print(calculate_load(grid))