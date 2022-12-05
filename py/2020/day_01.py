import aoc_lube
from itertools import combinations

RAW = aoc_lube.fetch(year=2020, day=1)
print(RAW)

def parse_raw():
    return list(map(int, RAW.split('\n')))

DATA = parse_raw()

def part_one():
    for i, j in combinations(DATA, 2):
        if i + j == 2020:
            return i * j

def part_two():
    for i, j, k in combinations(DATA, 3):
        if i + j + k == 2020:
            return i * j * k

aoc_lube.submit(year=2020, day=1, part=1, solution=part_one)
aoc_lube.submit(year=2020, day=1, part=2, solution=part_two)
