from day04_1 import winning_nums

if __name__ == "__main__":
    total = 0
    card_copies = {}

    with open("input.txt") as f:
        for idx, line in enumerate(f.readlines()):
            extra_spread = len(winning_nums(line))
            card_copies[idx+1] = card_copies.get(idx+1, 0)+1
            multiplier = card_copies[idx+1]
            total += multiplier

            for e in range(extra_spread):
                card_copies[idx+e+2] = card_copies.get(idx+e+2, 0) + multiplier
            
    print(total)
    