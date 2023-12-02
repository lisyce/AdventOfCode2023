from day02_1 import cube_nums, is_possible




if __name__ == "__main__":
    with open("input.txt") as f:
        total = 0
        for line in f.readlines():
            halves = line.split(":")
            id = int(halves[0].split(" ")[1])
            sets = halves[1].split(";")

            min_r = 0
            min_g = 0
            min_b = 0

            for handful in sets:
                r, g, b = cube_nums(handful)
                min_r = max(min_r, r)
                min_g = max(min_g, g)
                min_b = max(min_b, b)
            
            power = min_r * min_g * min_b
            total += power

    
    print(total)