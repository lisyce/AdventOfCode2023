import re

def parse_input(filename: str) -> list[tuple[int, int]]:
    with open(filename) as f:
        line = f.readline().strip()
        times = [int(n) for n in re.findall(r'\d+', line)]
        line = f.readline().strip()
        dists = [int(n) for n in re.findall(r'\d+', line)]

        return [(t, d) for t, d in zip(times, dists)]


def ways_to_win(time: int, dist: int) -> int:
    sum = 0
    for i in range(time+1):
        if (i * (time-i)) > dist:
            sum += 1
    return sum

if __name__ == "__main__":
    # 374220 too low
    races = parse_input("input.txt")

    total = 1
    for time, dist in races:
        total *= ways_to_win(time, dist)

    print(total)