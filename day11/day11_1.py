def empty_col(universe: list[list[str]], col: int) -> bool:
    for row in universe:
        if row[col] == "#":
            return False
    
    return True


def insert_empty_col(universe: list[list[str]], col: int) -> None:
    for idx, row in enumerate(universe):
        universe[idx] = row[0:col] + ["."] + row[col:]


def expand_universe(universe: list[list[str]]) -> list[list[str]]:
    result = []
    for row in universe:
        result.append(row)
        if "#" not in row:
            result.append(row)

    ptr = 0 
    while ptr < len(result[0]):
        if empty_col(result, ptr):
            insert_empty_col(result, ptr)
            ptr += 1
        ptr += 1

    return result


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


def paths_sum(universe: list[list[str]]) -> str:
    total = 0
    galaxies = galaxy_locs(universe)

    while galaxies:
        curr = galaxies.pop()
        for other in galaxies:
            total += abs(curr[0] - other[0]) + abs(curr[1] - other[1])

    return total

if __name__ == "__main__":
    universe = parse_universe("input.txt")
    universe = expand_universe(universe)

    print(paths_sum(universe))