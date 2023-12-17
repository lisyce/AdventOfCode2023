
def parse_graph(filename: str) -> dict[str, tuple[int, int]]:
    graph = {}
    with open(filename) as f:
        next(f)
        next(f)

        for line in f:
            line = line.split(" = ")

            key = line[0]
            paths = line[1][1:-2]
            paths = paths.split(", ")
            
            graph[key] = (paths[0], paths[1])
    return graph


if __name__ == "__main__":
    filename = "input.txt"

    with open(filename) as f:
        instructions = [c for c in f.readline().strip()]
        graph = parse_graph(filename)
    
    steps = 0
    instr_ptr = 0
    curr = "AAA"

    while curr != "ZZZ":
        # traverse
        next_dir = 0 if instructions[instr_ptr] == "L" else 1
        curr = graph[curr][next_dir]

        steps += 1
        instr_ptr = (instr_ptr + 1) % len(instructions)

    print(steps)