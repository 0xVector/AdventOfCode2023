with open("inputs/day04.txt") as file:
    data = []
    for line in file:
        card = []
        for part in line.strip().split(":")[1].split("|"):
            card.append(set(map(int, part.split())))
        data.append(card)


# Part 1 ===
part1 = 0
for winning, mine in data:
    my_score = len(winning & mine)
    if my_score > 0:
        part1 += 2**(my_score - 1)


# Part 2 ===
cards = {card: 1 for card in range(len(data))}
for card_number, (winning, mine) in enumerate(data):
    score = len(winning & mine)
    for won_card in range(card_number+1, card_number+1 + score):
        cards[won_card] += cards[card_number]
part2 = sum(cards[card] for card in cards)


print("Part 1:", part1)
print("Part 2:", part2)

assert part1 == 33950
assert part2 == 14814534
