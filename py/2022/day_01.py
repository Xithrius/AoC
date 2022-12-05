import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=1)
print(RAW)

def parse_raw():
    return [[int(y) for y in x.split('\n')] for x in RAW.split('\n\n')]

DATA = parse_raw()

def part_one():
    return max([sum(x) for x in DATA])

def part_two():
    return sum(sorted([sum(x) for x in DATA])[-3:])

aoc_lube.submit(year=2022, day=1, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=1, part=2, solution=part_two)
