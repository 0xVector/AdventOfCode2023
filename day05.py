with open("inputs/day05.txt") as file:
    data = [line.strip() for line in file]


def find(seed):
    for mode in range(7):
        for source, dest in maps[mode].items():
            if seed in source:
                seed = dest[seed - source.start]
                break
    return seed


maps = [{} for _ in range(7)]
range_starts = []
for line in data:
    if "seeds" in line:
        seeds = tuple(map(int, line.split(":")[1].split()))
    elif "seed-to-soil" in line:
        mode = 0
    elif "soil-to-fertilizer" in line:
        mode = 1
    elif "fertilizer-to-water" in line:
        mode = 2
    elif "water-to-light" in line:
        mode = 3
    elif "light-to-temperature" in line:
        mode = 4
    elif "temperature-to-humidity" in line:
        mode = 5
    elif "humidity-to-location" in line:
        mode = 6

    elif line:
        dest, source, length = map(int, line.split())
        maps[mode][range(source, source + length)] = range(dest, dest + length)
        range_starts.append(source)
        range_starts.append(dest)


# Part 1 ===
part1 = min(find(seed) for seed in seeds)


# Part 2 ===
seeds = tuple(
    range_start
    for range_start in range_starts
    for start, length in zip(seeds[::2], seeds[1::2])
    if range_start in range(start, start + length)
)
part2 = min(find(seed) for seed in seeds)


print("Part 1:", part1)
print("Part 2:", part2)

assert part1 == 26273516
assert part2 == 34039469
