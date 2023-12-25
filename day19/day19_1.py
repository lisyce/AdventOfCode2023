import re

def fn_from_condition(condition: str):
    tuple_map = {
        "x": 0,
        "m": 1,
        "a": 2,
        "s": 3
    }

    idx = tuple_map[condition[0]]
    comparison = condition[1]
    amt = int(condition[2:])

    if comparison == ">":
        return lambda x: x[idx] > amt

    return lambda x: x[idx] < amt


def get_workflows(filename: str):
    result = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                break

            name = line.split("{")[0]
            result[name] = []
            
            conditions = line.split("{")[1][:-1]
            for condition in conditions.split(","):
                parts = condition.split(":")

                if len(parts) == 2:
                    fn = fn_from_condition(parts[0])
                    result[name].append((fn, parts[1]))
                else:
                    result[name].append((None, parts[0]))

    return result


def part_accepted(workflows, part: tuple[int, int, int, int]) -> bool:
    curr_workflow = "in"

    while True:
        for fn, next_workflow in workflows[curr_workflow]:
            if fn is None or fn(part) == True:
                curr_workflow = next_workflow
                break

        if next_workflow in ["A", "R"]:
            return next_workflow == "A"


def get_parts(filename: str):
    finished_skipping = False
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                finished_skipping = True
                continue

            if finished_skipping:
                nums = [int(n) for n in re.findall("\d+", line)]
                yield (nums[0], nums[1], nums[2], nums[3])


if __name__ == "__main__":
    filename = "input.txt"

    workflows = get_workflows(filename)

    total = 0
    for part in get_parts(filename):
        if part_accepted(workflows, part):
            total += sum(part)
    
    print(total)