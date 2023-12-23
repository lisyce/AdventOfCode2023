from day16_1 import parse_grid, bounce_beam, get_unique_visits

if __name__ == "__main__":
    grid = parse_grid("input.txt")
    best = 0

    # top/bottom
    for i in range(len(grid[0])):
        visited = set()
        bounce_beam(grid, i, 0, "down", visited)
        best = max(get_unique_visits(visited), best)

        visited = set()
        bounce_beam(grid, i, len(grid) - 1, "up", visited)
        best = max(get_unique_visits(visited), best)

    # left/right
    for i in range(len(grid)):
        visited = set()
        bounce_beam(grid, 0, i, "right", visited)
        best = max(get_unique_visits(visited), best)

        visited = set()
        bounce_beam(grid, len(grid[0]) - 1, i, "left", visited)
        best = max(get_unique_visits(visited), best)
        

    print(best)