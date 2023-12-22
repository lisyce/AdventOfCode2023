def HASH(x: str) -> int:
    result = 0
    for char in x:
        result += ord(char)
        result *= 17
        result %= 256
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline().strip()

    total = sum(HASH(x) for x in line.split(","))
    print(total)