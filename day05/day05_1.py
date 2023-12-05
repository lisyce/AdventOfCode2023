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
    
    def chunks_to_chunks(self, in_chunks: list[tuple[int, int]]) -> list[tuple[int, int]]:
        result = []
        
        for start, count in in_chunks:
            left = start
            while left < start + count:
                # find the range we fit into
                fit_range = None
                for r in self.ranges: 
                    if left >= r[1] and left < r[1] + r[2]:
                        fit_range = r
                        break
                
                if fit_range is None:
                    # does a range start somewhere in the middle?
                    found = False
                    for r in self.ranges:
                        if r[1] >= left and r[1] < left + count:
                            # found one
                            found = True
                            amt_outside_range = r[1] - left
                            result.append((left, amt_outside_range)) # outside range
                            left += amt_outside_range
                            start = left
                            count -= amt_outside_range

                    if not found:
                        result.append((left, count))
                        break
                else:
                    # how much of it fits into the range?
                    amount_that_fits = (fit_range[2] + fit_range[1]) - left
                    amount_that_fits = min(amount_that_fits, count)  # constrain to be maxed out by the range

                    result.append((self[left], amount_that_fits))
                    left += amount_that_fits
                    count -= amount_that_fits
            
        return result


def parse_transitions(filename: str):
    transitions = [RangeDict() for _ in range(7)]

    with open(filename) as f:
        f.readline() # skip seeds
        f.readline()
        for dict_counter in range(7):
            f.readline() # header
            line = f.readline().strip()
            while line:
                r = [int(n) for n in line.split(" ")]
                transitions[dict_counter].add_range(r)

                line = f.readline().strip()
    return transitions


def get_min_transition(seeds: list[int], transitions: list[RangeDict]):
    min_loc = None
    for seed in seeds:
        curr = seed
        for t in transitions:
            curr = t[curr]
        
        if min_loc is None or curr < min_loc:
            min_loc = curr
    
    return min_loc


if __name__ == "__main__":
    filename = "input.txt"
    seeds = None
    transitions = parse_transitions(filename)

    with open(filename) as f:
        nums = f.readline().strip().split(": ")[1]
        seeds = [int(n) for n in re.findall(r'\d+', nums)]

    min_loc = get_min_transition(seeds, transitions)
    
    print(min_loc)