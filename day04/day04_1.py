import re

def winning_nums(line: str) -> set[int]:
    halves = line.strip().split(" | ")
    # winning nums
    winning = halves[0].split(": ")[1]
    winning = {int(n) for n in re.findall(r'\d+', winning)}

    # ours
    ours = {int(n) for n in re.findall(r'\d+', halves[1])}
    return ours.intersection(winning)


if __name__ == "__main__":
    total = 0
    with open("input.txt") as f:
        for line in f.readlines():
            nums = winning_nums(line)
            if len(nums) > 0:
                total += 2 ** (len(nums)-1)

    print(total)
