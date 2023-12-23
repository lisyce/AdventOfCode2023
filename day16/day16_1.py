from typing import Literal

def parse_grid(filename: str) -> list[list[str]]:
    result = []
    with open(filename) as f:
        for line in f:
            result.append([c for c in line.strip()])

    return result


def bounce_beam(grid: list[list[str]], x: int, y: int,
                direction: Literal["up", "down", "right", "left"],
                visited: set(tuple[int, int, str])) -> None:

    while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid) and (x, y, direction) not in visited:
        visited.add((x, y, direction))

        if direction == "up":
            if grid[y][x] == "-":
                bounce_beam(grid, x-1, y, "left", visited)
                direction = "right"
                x += 1
            elif grid[y][x] == "\\":
                direction = "left"
                x -= 1
            elif grid[y][x] == "/":
                direction = "right"
                x += 1
            else:
                y -= 1
        
        elif direction == "down":
            if grid[y][x] == "-":
                bounce_beam(grid, x-1, y, "left", visited)
                direction = "right"
                x += 1
            elif grid[y][x] == "\\":
                direction = "right"
                x += 1
            elif grid[y][x] == "/":
                direction = "left"
                x -= 1
            else:
                y += 1

        elif direction == "left":
            if grid[y][x] == "|":
                bounce_beam(grid, x, y-1, "up", visited)
                direction = "down"
                y += 1
            elif grid[y][x] == "\\":
                direction = "up"
                y -= 1
            elif grid[y][x] == "/":
                direction = "down"
                y += 1
            else:
                x -= 1

        elif direction == "right":
            if grid[y][x] == "|":
                bounce_beam(grid, x, y-1, "up", visited)
                direction = "down"
                y += 1
            elif grid[y][x] == "\\":
                direction = "down"
                y += 1
            elif grid[y][x] == "/":
                direction = "up"
                y -= 1
            else:
                x += 1


def get_unique_visits(visited: set[tuple[int, int, str]]) -> int:
    unique = set()
    for x, y, _ in visited:
        unique.add((x, y))
    
    return len(unique)


if __name__ == "__main__":
    grid = parse_grid("input.txt")
    visited = set()

    bounce_beam(grid, 0, 0, "right", visited)
    print(get_unique_visits(visited))