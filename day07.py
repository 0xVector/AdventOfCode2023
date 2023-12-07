with open("inputs/day07.txt") as file:
    data = [(line.split()[0], int(line.split()[1])) for line in file]

ORDER = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")


def score(hand):
    return sorted((hand.count(card) for card in ORDER if card in hand), reverse=True)


def score2(hand):
    score_ = sorted(
        (hand.count(card) for card in ORDER if card in hand and card != "J"),
        reverse=True,
    ) or [0]
    score_[0] += hand.count("J")
    return score_


# Part 1 ===
part1 = sum(
    rank * bid
    for rank, (_, bid) in enumerate(
        sorted(data, key=lambda x: (score(x[0]), tuple(map(ORDER.index, x[0])))),
        start=1,
    )
)


# Part 2 ===
part2 = sum(
    rank * bid
    for rank, (_, bid) in enumerate(
        sorted(
            data,
            key=lambda x: (
                score2(x[0]),
                tuple(
                    map((["J"] + list(filter(lambda x: x != "J", ORDER))).index, x[0])
                ),
            ),
        ),
        start=1,
    )
)


print("Part 1:", part1)
print("Part 2:", part2)
