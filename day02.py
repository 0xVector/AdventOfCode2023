with open("inputs/day02.txt") as file:
    data = [line.strip() for line in file]

# Part 1 ===
part1 = 0
part2 = 0
# red_max, green_max, blue_max = 12, 13, 14
for game in data:
    game = game.split(":")
    game_id = int(game[0].split()[1])
    parts = game[1].split(";")
    possible = True
    min_counts = {"red": 0, "green": 0, "blue": 0}
    for part in parts:
        counts = {"red": 0, "green": 0, "blue": 0}
        colors = part.strip().split(",")
        for color in colors:
            color = color.strip().split()
            counts[color[1]] += int(color[0])
            min_counts[color[1]] = max(min_counts[color[1]], int(color[0]))
        if counts["red"] > 12 or counts["green"] > 13 or counts["blue"] > 14:
            possible = False

    if possible:
        part1 += game_id
    part2 += min_counts["red"] * min_counts["green"] * min_counts["blue"]



# Part 2 ===



print("Part 1:", part1)
print("Part 2:", part2)