from typing import Literal
from collections import deque

def add_col(grid: list[list[str]], side: Literal["left", "right"]):
    if side == "left":
        for row in grid:
            row.insert(0, ".")
    
    elif side == "right":
        for row in grid:
            row.append(".")


def dig_perimeter(filename: str) -> tuple[list[list[str]], tuple[int, int]]:
    grid = [["#"]]
    cx = 0
    cy = 0

    fill_start = [0, 0]
    start_moved_times = 0

    with open(filename) as f:
        for line in f:
            line = line.strip().split(" ")
            direction = line[0]
            amt = int(line[1])

            if start_moved_times < 2:
                start_moved_times += 1
                if direction in ["L", "R"]:
                    fill_start[0] += 1 if direction == "R" else -1
                else:
                    fill_start[1] += 1 if direction == "D" else -1

            if direction == "R":
                for _ in range(amt):
                    cx += 1
                    if cx >= len(grid[0]):
                        add_col(grid, "right")
                    grid[cy][cx] = "#"
            
            elif direction == "L":
                for _ in range(amt):
                    cx -= 1
                    if cx < 0:
                        add_col(grid, "left")
                        cx = 0
                    grid[cy][cx] = "#"
            
            elif direction == "U":
                for _ in range(amt):
                    cy -= 1
                    if cy < 0:
                        grid.insert(0, ["." for _ in grid[0]])
                        cy = 0
                    grid[cy][cx] = "#"
            
            elif direction == "D":
                for _ in range(amt):
                    cy += 1
                    if cy >= len(grid):
                        grid.append(["." for _ in grid[0]])
                    grid[cy][cx] = "#"
            
    return grid, (cx + fill_start[0], cy + fill_start[1])


def fill_pit(grid: list[list[str]], start: tuple[int, int]):
    # BFS to fill
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        grid[y][x] = "#"

        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nx, ny in neighbors:
            if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid):
                if (nx, ny) not in q and grid[ny][nx] != "#":
                    q.append((nx, ny))


            
def pit_size(grid: list[list[str]]) -> int:
    total = 0
    for row in grid:
        for col in row:
            if col in ["*", "#"]:
                total += 1
    return total


if __name__ == "__main__":
    # 45475 too high
    # 29229 too low
    grid, fill_start = dig_perimeter("input.txt")
    fill_pit(grid, fill_start)
    print(pit_size(grid))