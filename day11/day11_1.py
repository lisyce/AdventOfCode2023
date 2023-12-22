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

    ptr = 0 # FIXME this part is the part that doesn't work
    while ptr < len(result[0]):
        if empty_col(universe, ptr):
            insert_empty_col(universe, ptr)
        ptr += 1

    return result


def parse_universe(filename: str) -> list[list[str]]:
    result = []

    with open(filename) as f:
        for line in f.readlines():
            result.append([c for c in line.strip()])

    return result


if __name__ == "__main__":
    universe = parse_universe("input_test.txt")
    universe = expand_universe(universe)

    for row in universe:
        for col in row:
            print(col, end="")
        print()

    