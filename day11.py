with open("inputs/day11.txt") as file:
    data = [line.strip() for line in file]

# Part 1 & 2 ===
galaxies = []
empty_rows,empty_cols = [], []
for x, col in enumerate(zip(*data)):
    if col.count("#") == 0:
        empty_cols.append(x)
for y, row in enumerate(data):
    if row.count("#") == 0:
        empty_rows.append(y)
    for x, char in enumerate(row):
        if char == "#":
            galaxies.append((x, y))

part1, part2 = 0, 0

checked = set()
for x, y in galaxies:
    for x2, y2 in galaxies:
        if (x, y) == (x2, y2):
            continue
        if frozenset(((x, y), (x2, y2))) in checked:
            continue
        checked.add(frozenset(((x, y), (x2, y2))))

        dx, dy = abs(x - x2), abs(y - y2)
        part1 += dx + dy
        part2 += dx + dy
        for empty_x in empty_cols:
            if x < empty_x < x2 or x2 < empty_x < x:
                part1 += 1
                part2 += 10**6 - 1
        for empty_y in empty_rows:
            if y < empty_y < y2 or y2 < empty_y < y:
                part1 += 1
                part2 += 10**6 - 1


print("Part 1:", part1)
print("Part 2:", part2)
