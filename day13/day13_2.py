from day13_1 import parse_grids, is_vertical_symmetry, is_horizontal_symmetry


def col_diff(pattern: list[list[str]], col1, col2) -> int:
    total = 0
    for row in pattern:
        if row[col1] != row[col2]:
            total += 1
    
    return total


def row_diff(pattern: list[list[str]], row1, row2) -> int:
    total = 0
    for x, y in zip(pattern[row1], pattern[row2]):
        if x != y:
            total += 1
    
    return total


def is_vertical_symmetry_with_one_smudge(pattern: list[list[str]], split: int) -> bool:
    # spread outward from the split
    # we have to hit at least one edge for this to be symmetry
    left_ptr = split
    right_ptr = split + 1

    smudges = 1

    while left_ptr >= 0 and right_ptr <= len(pattern[0]) - 1:
        diff = col_diff(pattern, left_ptr, right_ptr)
        if diff - smudges > 0:
            return False

        smudges -= diff
        left_ptr -= 1
        right_ptr += 1

    return True


def is_horizontal_symmetry_with_one_smudge(pattern: list[list[str]], split: int) -> bool:
    top_ptr = split
    bottom_ptr = split + 1

    smudges = 1

    while top_ptr >= 0 and bottom_ptr <= len(pattern) - 1:
        diff = row_diff(pattern, top_ptr, bottom_ptr)
        if diff - smudges > 0:
            return False
        smudges -= diff
        top_ptr -= 1
        bottom_ptr += 1

    return True


def get_summary(pattern: list[list[str]]) -> int:
    # check for vertical symmetry
    for split in range(len(pattern[0]) - 1):
        if not is_vertical_symmetry(pattern, split) and is_vertical_symmetry_with_one_smudge(pattern, split):
            return split + 1
    
    # check for horizontal symmetry
    for split in range(len(pattern) - 1):
        if not is_horizontal_symmetry(pattern, split) and is_horizontal_symmetry_with_one_smudge(pattern, split):
            return 100 * (split + 1)
    
    return 0


if __name__ == "__main__":
    total = sum(get_summary(g) for g in parse_grids("input.txt"))
    print(total)
