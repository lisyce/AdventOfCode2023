from day15_1 import HASH

def idx_of_label(box: list[list[str, int]], label: str) -> int:
    for idx, (l, _) in enumerate(box):
        if l == label:
            return idx
        
    return -1


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline().strip()

    # perform instructions to put lenses in boxes
    boxes = [[] for _ in range(256)]
    for x in line.split(","):
        op = "=" if "=" in x else "-"
        label = x.split(op)[0]
        box = HASH(label)

        label_idx = idx_of_label(boxes[box], label)
        if op == "-" and label_idx >= 0:
            boxes[box].pop(label_idx)
        elif op == "=":
            focal_length = int(x.split(op)[1])
            if label_idx >= 0:
                boxes[box][label_idx][1] = focal_length
            else:
                boxes[box].append([label, focal_length])

    # find focusing power
    total = 0
    for box_num, box in enumerate(boxes):
        for slot_num, lens in enumerate(box):
            focus = (1 + box_num) * (1 + slot_num) * lens[1]
            total += focus
    
    print(total)