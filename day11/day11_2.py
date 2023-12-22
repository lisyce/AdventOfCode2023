from day11_1 import parse_universe, paths_sum

if __name__ == "__main__":
    universe = parse_universe("input.txt")
    print(paths_sum(universe, 1000000))