from collections import defaultdict
import aoc_lube

RAW = aoc_lube.fetch(year=2015, day=3)
print(RAW)

def parse_raw():
    return list(RAW)

DATA = parse_raw()

def part_one():
    locations = defaultdict(int)
    pos = [0, 0]

    for instruction in DATA:
        locations[f'{pos}'] += 1
        if instruction == '^':
            pos[1] += 1
        elif instruction == 'v':
            pos[1] -= 1
        elif instruction == '>':
            pos[0] += 1
        elif instruction == '<':
            pos[0] -= 1

    return len([i for i in locations.values() if i >= 1])

def part_two():
    ...

aoc_lube.submit(year=2015, day=3, part=1, solution=part_one)
aoc_lube.submit(year=2015, day=3, part=2, solution=part_two)
