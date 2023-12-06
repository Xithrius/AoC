import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=6)


def parse_raw():
    lst = [[int(y) for y in x.split()[1:]] for x in RAW.split("\n")]

    return lst


DATA = parse_raw()


def part_one():
    t, d = DATA
    total = 1
    for x, y in zip(t, d):
        best = 0
        for i in range(x):
            if i * (x - i) > y:
                best += 1

        total *= best

    return total


def part_two():
    t, d = DATA
    x, y = int("".join(str(i) for i in t)), int("".join(str(j) for j in d))
    best = 0
    for i in range(x):
        if i * (x - i) > y:
            best += 1

    return best


aoc_lube.submit(year=2023, day=6, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=6, part=2, solution=part_two)
