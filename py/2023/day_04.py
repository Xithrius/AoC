import aoc_lube
from collections import defaultdict


RAW = aoc_lube.fetch(year=2023, day=4)


def parse_raw():
    lst = [x for x in RAW.split("\n")]
    lst = [x.split(": ")[1].strip().split("|") for x in lst]
    lst = [[set([int(z) for z in y.strip().split()]) for y in x] for x in lst]

    return lst


DATA = parse_raw()


def part_one():
    return sum(
        2 ** (len(z) - 1) for z in [x.intersection(y) for x, y in DATA] if len(z) > 0
    )


def part_two():
    d = defaultdict(lambda: 1)

    for i, (x, y) in enumerate(DATA):
        winning = x.intersection(y)
        points = len(winning)

        for _ in range(d[i]):
            for j in range(i + 1, i + points + 1):
                d[j] += 1

    return sum(d.values())


aoc_lube.submit(year=2023, day=4, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=4, part=2, solution=part_two)
