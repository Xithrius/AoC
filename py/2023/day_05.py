import aoc_lube


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
    seeds = [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    raw_maps = [
        [[int(z) for z in y.split()] for y in x.split("\n")[1:]] for x in DATA[1:]
    ]
    maps: list[list[range]] = []
    for x in raw_maps:
        inner = []
        for a, b, c in x:
            inner.extend([range(a, a + c), range(b, b + c)])
        maps.append(inner)

    for m in maps:
        locations = []

        for seed in seeds:
            for i in range(0, len(m), 2):
                r0, r1 = m[i + 1], m[i]
                contained = r0.stop > seed.start and r0.start < seed.stop
                if contained:
                    ranges = []
                    mid = range(max(seed.start, r0.start), min(seed.stop, r0.stop))

                    if mid.start > seed.start:
                        ranges.append(range(seed.start, mid.start))

                    if seed.stop > mid.stop:
                        ranges.append(range(mid.stop, seed.stop))

                    seeds += ranges

                    other = range(max(seed.start, r0.start), min(seed.stop, r0.stop))
                    r2 = r1.start - r0.start
                    last = range(other.start + r2, other.stop + r2)
                    locations.append(last)

                    break
            else:
                locations.append(seed)

        seeds = locations

    return min(x.start for x in seeds)


aoc_lube.submit(year=2023, day=5, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=5, part=2, solution=part_two)
