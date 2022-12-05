import aoc_lube

RAW = aoc_lube.fetch(year=2019, day=1)
print(RAW)

def parse_raw():
    return [int(x) for x in RAW.split('\n')]

DATA = parse_raw()

def part_one():
    return sum((x // 3) - 2 for x in DATA)

def part_two():
    total = 0
    for x in DATA:
        while x > 0:
            x = (x // 3) - 2
            if x > 0:
                total += x

    return total

aoc_lube.submit(year=2019, day=1, part=1, solution=part_one)
aoc_lube.submit(year=2019, day=1, part=2, solution=part_two)
