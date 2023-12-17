from day08_1 import parse_graph
from math import lcm

if __name__ == "__main__":
    filename = "input.txt"

    with open(filename) as f:
        instructions = [c for c in f.readline().strip()]
        graph = parse_graph(filename)

    # find all start nodes
    locs = [k for k in graph.keys() if k[-1] == "A"]
    loop_len = [0 for _ in range(len(locs))]

    for idx, loc in enumerate(locs):
        steps = 0
        instr_ptr = 0
        while loc[-1] != "Z":
            # traverse
            next_dir = 0 if instructions[instr_ptr] == "L" else 1
            loc = graph[loc][next_dir]

            steps += 1
            instr_ptr = (instr_ptr + 1) % len(instructions)
        
        loop_len[idx] = steps
        locs[idx] = loc

    print(lcm(*loop_len))
