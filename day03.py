with open("inputs/day03.txt") as file:
    data = [list(line.strip()) for line in file]


def is_symbol(char):
    return not char.isdigit() and char != "."


def inside(x, y):
    return 0 <= x < len(data[0]) and 0 <= y < len(data)


DIFFS = ((0, -1), (-1, 0), (1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1))

# Part 1 ===
part1 = 0
number = []
a = []
is_part = False
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char.isdigit():
            number.append(char)
            is_part |= any(
                is_symbol(data[y + dy][x + dx]) for dx, dy in DIFFS if inside(x + dx, y + dy))
        else:
            if number and is_part:
                part1 += int("".join(number))
                a.append(number)
            number = []
            is_part = False
    if number and is_part:
        part1 += int("".join(number))
        a.append(number)
    number = []
    is_part = False


# Part 2 ===
part2 = 0
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "*":
            numbers = []
            for dx, dy in DIFFS:
                if inside(x + dx, y + dy):
                    number = []
                    i = 0
                    while inside(x + dx + i, y + dy) and data[y + dy][x + dx + i].isdigit():
                        number.append(data[y + dy][x + dx + i])
                        data[y + dy][x + dx + i] = "."
                        i += 1
                    i = 1
                    while number and inside(x + dx - i, y + dy) and data[y + dy][x + dx - i].isdigit():
                        number.insert(0, data[y + dy][x + dx - i])
                        data[y + dy][x + dx - i] = "."
                        i += 1
                    if number:
                        numbers.append(int("".join(number)))

            if len(numbers) == 2:
                part2 += numbers[0] * numbers[1]



print("Part 1:", part1)
print("Part 2:", part2)