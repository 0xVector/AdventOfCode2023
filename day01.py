with open("inputs/day01.txt") as file:
    data = [line.strip() for line in file]


def find(line, digits, find_f, selection, inf):
    return selection((find_f(dig), i+1 if i < 9 else i-8) if dig in line else (inf, -1) for i, dig in enumerate(digits))[1]


# Part 1 ===
digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
part1 = sum(int(f"{find(line, digits, line.find, min, float('inf'))}{find(line, digits, line.rfind, max, -float('inf'))}") for line in data)


# Part 2 ===
digits = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", *digits)
part2 = sum(int(f"{find(line, digits, line.find, min, float('inf'))}{find(line, digits, line.rfind, max, -float('inf'))}") for line in data)


print("Part 1:", part1)
print("Part 2:", part2)

# print(part1 == 55477 and part2 == 54431)
assert part1 == 55477 and part2 == 54431
