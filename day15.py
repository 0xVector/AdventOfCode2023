with open("inputs/day15.txt") as file:
    data = file.readline().strip().split(",")


def HASH(string):
    digest = 0
    for char in string:
        digest = (digest + ord(char))*17 % 256
    return digest


# Part 1 ===
part1 = sum(HASH(string) for string in data)


# Part 2 ===
boxes = [[] for _ in range(256)]
for step in data:
    if "-" in step:
        label = step[:-1]
        box = boxes[HASH(label)]
        for i, lens in enumerate(box):
            if lens[0] == label:
                box.pop(i)
                break
    else:
        label, focal = step.split("=")
        box = boxes[HASH(label)]
        replaced = False
        for i, lens in enumerate(box):
            if lens[0] == label:
                box[i] = (label, focal)
                replaced = True
                break
        if not replaced:
            box.append((label, focal))

part2 = sum((i+1)*(j+1)*int(lens[1]) for i, box in enumerate(boxes) for j, lens in enumerate(box))


print("Part 1:", part1)
print("Part 2:", part2)
