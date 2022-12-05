import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=4)
print(RAW)

def parse_raw():
    return [x for x in RAW.split('\n')]

DATA = parse_raw()

def part_one():
    total = 0
    for item in DATA:
        element = item.split(",")
        a, b = element
        l = lambda w: [int(i) for i in w.split("-")]
        x, y = l(a), l(b)
        i, j = set(range(x[0], x[1] + 1)), set(range(y[0], y[1] + 1))
        z = i.intersection(j)
        if (z == i or z == j):
            total += 1
    return total

def part_two():
    total = 0
    for item in DATA:
        element = item.split(",")
        a, b = element
        l = lambda w: [int(i) for i in w.split("-")]
        x, y = l(a), l(b)
        i, j = set(range(x[0], x[1] + 1)), set(range(y[0], y[1] + 1))
        z = i.intersection(j)
        if len(z) > 0:
            total += 1
    return total

aoc_lube.submit(year=2022, day=4, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=4, part=2, solution=part_two)
