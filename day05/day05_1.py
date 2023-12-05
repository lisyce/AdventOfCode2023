import re

class RangeDict():
    ranges: list[tuple[int, int, int]]

    def __init__(self) -> None:
        self.ranges = []

    def add_range(self, r: list[int, int, int]):
        self.ranges.append((r[0], r[1], r[2]))

    def __getitem__(self, key: int):
        for dst, src, count in self.ranges:
            if key >= src and key < src + count:
                # we found the range it's in
                offset = key - src
                return dst + offset

        # we never found it
        return key


if __name__ == "__main__":
    seeds = None
    transitions = [RangeDict() for _ in range(7)]

    with open("input.txt") as f:
        nums = f.readline().strip().split(": ")[1]
        seeds = [int(n) for n in re.findall(r'\d+', nums)]
        f.readline() # blank

        for dict_counter in range(7):
            f.readline() # header
            line = f.readline().strip()
            while line:
                r = [int(n) for n in line.split(" ")]
                transitions[dict_counter].add_range(r)

                line = f.readline().strip()

    min_loc = None
    for seed in seeds:
        curr = seed
        for t in transitions:
            curr = t[curr]
        
        if min_loc is None or curr < min_loc:
            min_loc = curr
    
    print(min_loc)