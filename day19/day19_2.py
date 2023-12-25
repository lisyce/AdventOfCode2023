from day19_1 import get_workflows

def get_all_accept_paths(workflows):
    result = []
    _get_all_accept_paths_helper(result, ["in"], workflows)
    return result

def _get_all_accept_paths_helper(result: list[list[str]], curr_path: list[str], workflows):
    curr_node = curr_path[-1]
    if curr_node == "A":
        copy = curr_path.copy()
        if copy not in result:
            result.append(copy)

    elif curr_node != "R": # we can keep traversing
        neighbors = [x[1] for x in workflows[curr_node]]
        for n in neighbors:
            curr_path.append(n)
            _get_all_accept_paths_helper(result, curr_path, workflows)
            curr_path.pop()


if __name__ == "__main__":
    filename = "input_test.txt"

    workflows = get_workflows(filename)
    accept = get_all_accept_paths(workflows)
    print(len(accept))
