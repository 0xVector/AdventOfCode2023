with open("day06in.txt") as file:
    times = tuple(map(int, file.readline().strip().split(":")[1].split()))
    distances = tuple(map(int, file.readline().strip().split(":")[1].split()))

part1 = 1
for t, d in zip(times, distances):
    x = 1
    while not d/x + x < t:
        x += 1
    start = x
    x = t
    while not d/x + x < t:
        x -= 1
    end = x
    part1 *= end - start + 1

print(part1)

part2 = 1
t, d = int("".join(map(str, times))), int("".join(map(str, distances)))
x = 1
while not d/x + x < t:
    x += 1
start = x
x = t
while not d/x + x < t:
    x -= 1
end = x
part2 *= end - start + 1

print(part2)

#  x = time pressed = speed
#  d/x + x < t
