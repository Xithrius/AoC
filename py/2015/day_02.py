import numpy as np
import aoc_lube

RAW = aoc_lube.fetch(year=2015, day=2)
print(RAW)

def parse_raw():
    return [[int(y) for y in x.split("x")] for x in RAW.split("\n")]

DATA = parse_raw()

def part_one():
    lst = [[x[0] * x[1], x[1] * x[2], x[0] * x[2]] * 2 for x in DATA]
    return sum(sum(x) + min(x) for x in lst)

def part_two():
    return sum((np.prod(j) + ((j[0] + j[1]) * 2)) for j in [sorted(i) for i in DATA])

aoc_lube.submit(year=2015, day=2, part=1, solution=part_one)
aoc_lube.submit(year=2015, day=2, part=2, solution=part_two)
