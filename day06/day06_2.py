from day06_1 import ways_to_win

def fix_kerning(line: str) -> int:
    line = line.strip().replace(" ", "")
    return int(line.split(":")[1])


if __name__ == "__main__":
    with open("input.txt") as f:
        time = fix_kerning(f.readline())
        dist = fix_kerning(f.readline())
        print(ways_to_win(time, dist))