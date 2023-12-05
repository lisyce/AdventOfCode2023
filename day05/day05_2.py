from day05_1 import parse_transitions, get_min_transition

if __name__ == "__main__":
    filename = "input_test.txt"
    seed_ranges = []
    transitions = parse_transitions(filename)

    with open(filename) as f:
        line = f.readline()
        nums = [int(n) for n in line.strip().split(": ")[1].split(" ")]

        for i in range(0, len(nums), 2):
            seed_ranges.append((nums[i], nums[i+1]))
    

    result = seed_ranges
    for t in transitions:
        result = t.chunks_to_chunks(result)
        # print(result)

    min_loc = result[0][0]
    for p1, p2 in result:
        min_loc = min(min_loc, p1)
    
    print(min_loc)
    # 13756552 too high