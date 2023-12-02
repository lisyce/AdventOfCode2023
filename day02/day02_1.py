import re

RED = 12
GREEN = 13
BLUE = 14

def is_possible(red: int, green: int, blue: int) -> bool:
    return red <= RED and green <= GREEN and blue <= BLUE

def cube_nums(line: str) -> tuple[int]:
    line = line.strip()
    red = 0
    green = 0
    blue = 0
    parts = line.split(", ")

    for part in parts:
        num = int(re.findall("\d+", part)[0])
        color = part.split(" ")[1]

        if color == "red":
            red += num
        elif color == "green":
            green += num
        elif color == "blue":
            blue += num
        
    return (red, green, blue)


if __name__ == "__main__":
    with open("input.txt") as f:
        total = 0
        for line in f.readlines():
            halves = line.split(":")
            id = int(halves[0].split(" ")[1])
            sets = halves[1].split(";")

            possible = True
            for handful in sets:
                r, g, b = cube_nums(handful)
                if not is_possible(r, g, b):
                    possible = False
                    break

            if possible:
                total += id
    
    print(total)