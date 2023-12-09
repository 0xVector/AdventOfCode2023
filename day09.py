with open("inputs/day09.txt") as file:
    data = [list(map(int, line.split())) for line in file]

part1, part2 = 0, 0
for numbers in data:
    sequences = [numbers]
    while any(sequences[-1]):
        sequences.append([b-a for a,b in zip(sequences[-1], sequences[-1][1:])])
  
    # Part 1
    for sequence in reversed(sequences):
        part1 += sequence[-1]

    # Part 2
    new = 0
    for sequence in reversed(sequences):
        new = sequence[0] - new
    part2 += new


print("Part 1:", part1)
print("Part 2:", part2)
