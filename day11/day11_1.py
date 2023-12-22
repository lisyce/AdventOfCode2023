def empty_col(universe: list[list[str]], col: int) -> bool:
    for row in universe:
        if row[col] == "#":
            return False
    
    return True


def parse_universe(filename: str) -> list[list[str]]:
    result = []

    with open(filename) as f:
        for line in f.readlines():
            result.append([c for c in line.strip()])

    return result


def galaxy_locs(universe: list[list[str]]) -> set[tuple[int, int]]:
    result = set()
    for idx, row in enumerate(universe):
        for jdx, char in enumerate(row):
            if char == "#":
                result.add((jdx, idx))
    return result



def empty_rows(universe: list[list[str]]) -> set[int]:
    result = set()
    for idx, row in enumerate(universe):
        if "#" not in row:
            result.add(idx)
    
    return result


def empty_cols(universe: list[list[str]]) -> set[int]:
    result = set()
    for i in range(len(universe[0])):
        if empty_col(universe, i):
            result.add(i)
    
    return result


def paths_sum(universe: list[list[str]], multiplier: int) -> int:
    er = empty_rows(universe)
    ec = empty_cols(universe)

    total = 0
    galaxies = galaxy_locs(universe)

    while galaxies:
        curr = galaxies.pop()
        for other in galaxies:
            # x
            direction = 1 if curr[0] < other[0] else -1
            for i in range(curr[0], other[0], direction):
                total += multiplier if i in ec else 1

            # y
            direction = 1 if curr[1] < other[1] else -1
            for j in range(curr[1], other[1], direction):
                total += multiplier if j in er else 1

    return total


if __name__ == "__main__":
    universe = parse_universe("input.txt")
    print(paths_sum(universe, 2))