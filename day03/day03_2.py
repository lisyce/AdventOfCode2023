from day03_1 import parse_grid, get_adj_nums


if __name__ == "__main__":
    grid = parse_grid("input.txt")

    total = 0

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "*":
                neighbors = get_adj_nums(grid, i, j)
                if len(neighbors) == 2:
                    total += neighbors[0] * neighbors[1]
    print(total)