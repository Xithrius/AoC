import time
import aoc_lube
import itertools

import numpy as np


RAW = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
# RAW = aoc_lube.fetch(year=2023, day=5)


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

    seeds = list(sorted([(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)], key=lambda x: x[0]))

    maps = [[[int(z) for z in y.split()] for y in x.split("\n")[1:]] for x in DATA[1:]]

    lst = []
    for x in maps:
        inner = []
        for a, b, c in x:
            inner.extend([range(a, a + c), range(b, b + c)])
        lst.append(inner)

    # for j, (start, stop) in enumerate(seeds):
    for start, stop in seeds:
        splits = [(start, stop)]

        # splitted = True
        # while splitted:
        #     splitted = False

        j = 0
        while j < len(splits):
            for m in lst:
                for m0, m1 in zip(m[1::2], m[::2]):
                    diff = m1.start - m0.start

                    print(start, stop, m0, m1, diff, splits)

                    # start and end before or after source, or maybe surrounding
                    if (start not in m0) and (stop not in m0):
                        if (start < m0.start) and (stop > m0.stop):
                            splits[j] = (start, m0.start)
                            splits.insert(j + 1, (m0.start + diff, m0.stop + diff))
                            splits.insert(j + 1, (m0.stop, stop ))
                        else:
                            continue
                    # start before source, but end in source
                    elif (start not in m0) and (stop in m0):
                        splits[j] = (start, m0.start)
                        splits.insert(j + 1, (m0.start + diff, m0.stop + diff))
                    # entire seed range in source
                    elif (start in m0) and (stop in m0):
                        splits[j] = (start + diff, stop + diff)
                        if (stop != m0.stop):
                            splits.insert(j + 1, (stop, m0.stop))

                        if (start != m0.start):
                            splits.insert(j + 1, (start, m0.start))

                    # start in source, but end is outside
                    else:
                        splits[j] = (start + diff, m0.start + diff)
                        splits.insert(j + 1, (m0.stop, stop))

            time.sleep(10)

            j += 1

        print([x[0] for x in splits])

        break

    # print(seeds)
    # print()
    # print(lst)

    # lowers = []

    # for seed in seeds:
    #     split_seeds = [seed]

    #     i = 0

    #     # for i, (start, stop) in enumerate(split_seeds):
    #     while i < len(split_seeds):
    #         start, stop = split_seeds[i]

    #         for m in lst:
    #             for m0, m1 in zip(m[1::2], m[::2]):
    #                 diff = m0.start - m1.start

    #                 print(start, stop, m0, m1, diff, split_seeds)

    #                 # start and end before or after source,
    #                 # or maybe surrounding
    #                 if (start not in m0) and (stop not in m0):
    #                     if (start < m0.start) and (stop > m0.stop):
    #                         n0 = (start, m0.start + 1)
    #                         n1 = (m0.start + diff, m0.stop + diff + 1)
    #                         n2 = (m0.stop, stop + 1)
    #                         split_seeds[i] = n0
    #                         split_seeds.insert(i + 1, n2)
    #                         split_seeds.insert(i + 1, n1)
    #                         i += 2
    #                     else:
    #                         continue
    #                 # start before source, but end in source
    #                 elif (start not in m0) and (stop in m0):
    #                     n0 = (start, m0.start + 1)
    #                     n1 = (m0.start + diff, m0.stop + diff + 1)
    #                     split_seeds[i] = n0
    #                     split_seeds.insert(i + 1, n1)
    #                     i += 1
    #                 # entire seed range in source
    #                 elif (start in m0) and (stop in m0):
    #                     n0 = (start + diff, stop + diff + 1)
    #                     split_seeds[i] = n0
    #                     if (stop != m0.stop):
    #                         n2 = (stop, m0.stop + 1)
    #                         split_seeds.insert(i + 1, n2)
    #                         i += 1

    #                     if (start != m0.start):
    #                         n1 = (start, m0.start + 1)
    #                         split_seeds.insert(i + 1, n1)
    #                         i += 1

    #                 # start in source, but end is outside
    #                 else:
    #                     n0 = (start + diff, m0.start + diff + 1)
    #                     n1 = (m0.stop, stop + 1)
    #                     split_seeds[i] = n0
    #                     split_seeds.insert(i + 1, n1)
    #                     i += 1

    #         i += 1

    #     print(min(x[0] for x in split_seeds))

    #     break

                # # start and end before or after source
                # if (start not in m0) and (end not in m0):
                #     if (start < m0.start) and (end > m0.stop):
                #         n0 = (start, m0.start)
                #         n1 = (m0.start + diff, m0.stop + diff)
                #         n2 = (m0.stop, end)
                #         seeds[i] = n0
                #         seeds.insert(i + 1, n2)
                #         seeds.insert(i + 1, n1)
                #     else:
                #         continue
                # # start before source, but end in source
                # elif (start not in m0) and (end in m0):
                #     # first half of seed, before source start
                #     n0 = (start, m0.start)
                #     n1 = (m0.start + diff, m0.stop + diff)
                #     seeds[i] = n0
                #     seeds.insert(i + 1, n1)
                # # entire seed range in source
                # elif (start in m0) and (end in m0):
                #     n0 = (start + diff, end + diff)
                #     seeds[i] = n0
                #     if (end != m0.stop):
                #         n2 = (end, m0.stop)
                #         seeds.insert(i + 1, n2)
                #     if (start != m0.start):
                #         n1 = (start, m0.start)
                #         seeds.insert(i + 1, n1)
                # # start in source, but end is outside
                # else:
                #     n0 = (start + diff, m0.start + diff)
                #     n1 = (m0.stop, end)
                #     seeds[i] = n0
                #     seeds.insert(i + 1, n1)


    # return min(x[0] for x in lowers)
    return 0


# aoc_lube.submit(year=2023, day=5, part=1, solution=part_one)

print(part_two())
# aoc_lube.submit(year=2023, day=5, part=2, solution=part_two)
