def next_step(graph: list[list[str]], loc: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = loc
    curr_pipe = graph[y][x]

    result = []

    # explore up?
    if curr_pipe in ["|", "L", "J", "S"] and y > 0:
        next_pipe = graph[y-1][x]
        if next_pipe in ["|", "7", "F", "S"]:
            result.append((x, y-1))
    
    # explore down?
    if curr_pipe in ["|", "7", "F", "S"] and y < len(graph) - 1:
        next_pipe = graph[y+1][x]
        if next_pipe in ["|", "L", "J", "S"]:
            result.append((x, y+1))
    
    # explore left?
    if curr_pipe in ["-", "7", "J", "S"] and x > 0:
        next_pipe = graph[y][x-1]
        if next_pipe in ["-", "L", "F", "S"]:
            result.append((x-1, y))

    # explore right?
    if curr_pipe in ["-", "L", "F", "S"] and x < len(graph[y]) - 1:
        next_pipe = graph[y][x+1]
        if next_pipe in ["-", "J", "7", "S"]:
            result.append((x+1, y))
    
    return result


def parse_grid(filename: str) -> list[list[str]]:
    result = []
    with open(filename) as f:
        for line in f.readlines():
            result.append([c for c in line])
    
    return result


def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for idx, row in enumerate(grid):
        for jdx, col in enumerate(row):
            if col == "S":
                return (jdx, idx)


def pipe_len(grid: list[list[str]]) -> int:
    start = find_start(grid)

    curr = next_step(grid, start)[0]
    visited = set()
    visited.add(start)
    total = 1
    while curr != start:
        visited.add(curr)
        next_steps = next_step(grid, curr)
        # don't go into the "S" square unless we've already explored the other option
        if next_steps[0] in visited and next_steps[1] in visited:
            curr = start
        else:
            curr = next_steps[0] if next_steps[0] not in visited else next_steps[1]

        total += 1
    return total


if __name__ == "__main__":
    grid = parse_grid("input.txt")
    pl = pipe_len(grid)
    print(pl // 2)