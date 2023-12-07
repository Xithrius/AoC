from collections import Counter
import itertools
import aoc_lube

RAW = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
RAW = aoc_lube.fetch(year=2023, day=7)


def parse_raw():
    lst = [[x.split()[0], int(x.split()[1])] for x in RAW.split("\n")]

    return lst


DATA = parse_raw()


def rank_type(card: str) -> int:
    tests = [
        lambda c: [x[1] for x in c.most_common(1)] == [5],
        lambda c: [x[1] for x in c.most_common(2)] == [4, 1],
        lambda c: [x[1] for x in c.most_common(2)] == [3, 2],
        lambda c: [x[1] for x in c.most_common(3)] == [3, 1, 1],
        lambda c: [x[1] for x in c.most_common(3)] == [2, 2, 1],
        lambda c: [x[1] for x in c.most_common(4)] == [2, 1, 1, 1],
        lambda c: [x[1] for x in c.most_common(5)] == [1, 1, 1, 1, 1],
    ]

    counted_card = Counter(card)

    for i, test in enumerate(reversed(tests)):
        if test(counted_card):
            return i

    print("Something has gone terribly wrong")
    exit(1)


def compare_labels(c0: str, c1: str, p: list[str]) -> int:
    for x0, x1 in zip(c0, c1):
        i0, i1 = p.index(x0), p.index(x1)

        if i0 == i1:
            continue
        return i0 < i1
    return False


def part_one():
    d = sorted(
        [(hand, points, rank_type(hand)) for hand, points in DATA], key=lambda x: x[2]
    )
    p = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(d) - 1):
            (h0, _, r0), (h1, _, r1) = d[i], d[i + 1]
            if (r0 == r1) and (compare_labels(h0, h1, p)):
                d[i], d[i + 1] = d[i + 1], d[i]
                swapped = True

    results = [x[1] * i for i, x in enumerate(d, start=1)]

    return sum(results)


def create_best_hand(card: str, p: list[str]) -> str:
    if "J" not in card:
        return card

    best_score = 0
    best_card = card

    for item in itertools.product(p, repeat=card.count("J")):
        tmp = list(card)
        i = 0
        for j, c in enumerate(card):
            if c == "J":
                tmp[j] = item[i]
                i += 1
        score = rank_type(tmp)
        if score > best_score:
            best_score = score
            best_card = "".join(tmp)

    return best_card


def part_two():
    p = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    d = sorted(
        [
            (hand, points, rank_type(create_best_hand(hand, p)) )
            for hand, points in DATA
        ],
        key=lambda x: x[-1],
    )

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(d) - 1):
            (h0, _, r0), (h1, _, r1) = d[i], d[i + 1]
            if (r0 == r1) and (compare_labels(h0, h1, p)):
                d[i], d[i + 1] = d[i + 1], d[i]
                swapped = True

    results = [x[1] * i for i, x in enumerate(d, start=1)]

    return sum(results)


aoc_lube.submit(year=2023, day=7, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=7, part=2, solution=part_two)
