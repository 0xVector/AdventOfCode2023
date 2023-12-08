from math import lcm

with open("inputs/day08.txt") as file:
    commands = file.readline().strip()
    dirs  = {}
    for line in file:
        line = line.strip()
        if line:
            node, rest = line.split(" = ")
            left, right = rest[1:-1].split(", ")
            dirs[node] = (left, right)

# Part 1 ===
node = "AAA"
part1 = 0
while node != "ZZZ":
    side = commands[part1%len(commands)]
    node = dirs[node][0] if side == "L" else dirs[node][1]
    part1 += 1


# Part 2 ===
nodes = [node for node in dirs if node.endswith("A")]
solutions: list[int] = [0 for node in nodes]
i = 0
while not all(solutions):
    side = commands[i%len(commands)]
    for j, node in enumerate(nodes):
        if not solutions[j]:
            nodes[j] = dirs[node][0] if side == "L" else dirs[node][1]
            if nodes[j].endswith("Z"):
                solutions[j] = i+1
    i += 1
part2 = lcm(*solutions)


print("Part 1:", part1)
print("Part 2:", part2)
