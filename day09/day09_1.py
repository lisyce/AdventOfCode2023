import numpy as np

def next_value(sequence: list[int]) -> int:
    if not np.any(sequence):
        # list is all 0's; base case
        return 0
    
    next_sequence = []
    for i in range(1, len(sequence)):
        diff = sequence[i] - sequence[i-1]
        next_sequence.append(diff)
    
    n = next_value(next_sequence)
    return sequence[-1] + n


if __name__ == "__main__":
    total = 0

    with open("input.txt") as f:
        for line in f.readlines():
            sequence = [int(n) for n in line.split(" ")]
            total += next_value(sequence)
    
    print(total)