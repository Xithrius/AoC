import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=2)
print(RAW)

def parse_raw():
    return [x for x in RAW.split('\n')]

DATA = parse_raw()

def part_one():
    ...

def part_two():
    ...

aoc_lube.submit(year=2022, day=2, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=2, part=2, solution=part_two)
