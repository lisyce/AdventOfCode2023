def parse_grids(filename: str) -> list[list[str]]:
    with open(filename) as f:
        result = []
        for line in f:
            line = line.strip()
            if line == "":
                yield result
                result = []
            else:
                result.append([c for c in line])
    
    yield result


def cols_equal(pattern: list[list[str]], col1, col2) -> bool:
    for row in pattern:
        if row[col1] != row[col2]:
            return False
    
    return True


def is_vertical_symmetry(pattern: list[list[str]], split: int) -> bool:
    # spread outward from the split
    # we have to hit at least one edge for this to be symmetry
    left_ptr = split
    right_ptr = split + 1

    while left_ptr >= 0 and right_ptr <= len(pattern[0]) - 1:
        if not cols_equal(pattern, left_ptr, right_ptr):
            return False
        left_ptr -= 1
        right_ptr += 1
    return True


def is_horizontal_symmetry(pattern: list[list[str]], split: int) -> bool:
    top_ptr = split
    bottom_ptr = split + 1
    while top_ptr >= 0 and bottom_ptr <= len(pattern) - 1:
        if pattern[top_ptr] != pattern[bottom_ptr]:
            return False
        top_ptr -= 1
        bottom_ptr += 1
    return True


def get_summary(pattern: list[list[str]]) -> int:
    # check for vertical symmetry
    for split in range(len(pattern[0]) - 1):
        if is_vertical_symmetry(pattern, split):
            return split + 1
    
    # check for horizontal symmetry
    for split in range(len(pattern) - 1):
        if is_horizontal_symmetry(pattern, split):
            return 100 * (split + 1)
    
    return 0


if __name__ == "__main__":
    total = sum(get_summary(g) for g in parse_grids("input.txt"))
    print(total)
        