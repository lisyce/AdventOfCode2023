def is_word_digit(line: str, startIdx) -> str:
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    builder = ""
    for i in range(startIdx, startIdx+5):
        if i >= len(line):
            break
        builder += line[i]
        if builder in nums:
            return builder
        
    return ""



def get_num(line: str) -> int:
    key = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
    }

    first = ""
    last = ""
    for i, char in enumerate(line):
        if char in "0123456789":
            if not first:
                first = char
            last = char
        elif is_word_digit(line, i):
            converted = str(key[is_word_digit(line, i)])
            if not first:
                first = converted
            last = converted
    
    return int(first + last)

with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        total += get_num(line)
    
    print(total)