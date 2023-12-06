import aoc_lube
import itertools

import numpy as np

RAW = aoc_lube.fetch(year=2023, day=5)


def parse_raw():
    lst = [x for x in RAW.split("\n\n")]

    return lst


DATA = parse_raw()


def part_one():
    seeds = [int(x) for x in DATA[0].split()[1:]]

    maps = [[[int(z) for z in y.split()] for y in x.split("\n")[1:]] for x in DATA[1:]]
    lst = []
    for x in maps:
        inner = []
        for a, b, c in x:
            inner.extend([range(a, a + c), range(b, b + c)])
        lst.append(inner)

    locations = []

    for seed in seeds:
        location = seed

        for m in lst:
            for i in range(0, len(m), 2):
                if location in m[i + 1]:
                    location = m[i][m[i + 1].index(location)]
                    break

        locations.append(location)

    return min(locations)


def part_two():
    seeds = [int(x) for x in DATA[0].split()[1:]]

    seeds = itertools.chain(*[range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)])

    maps = [[[int(z) for z in y.split()] for y in x.split("\n")[1:]] for x in DATA[1:]]

    lst = []
    for x in maps:
        inner = []
        for a, b, c in x:
            inner.extend([range(a, a + c), range(b, b + c)])
        lst.append(inner)

    minimum = None

    for seed in seeds:
        location = seed

        for m in lst:
            for m0, m1 in zip(m[::2], m[1::2]):
                if location in m1:
                    location = m0[m1.index(location)]
                    break

        if minimum is None or location < minimum:
            minimum = location




    return minimum


# aoc_lube.submit(year=2023, day=5, part=1, solution=part_one)

print(part_two())
# aoc_lube.submit(year=2023, day=5, part=2, solution=part_two)
