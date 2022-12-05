import aoc_lube

RAW = aoc_lube.fetch(year=2019, day=2)
print(RAW)

def parse_raw():
    return list(map(int, RAW.strip().split(',')))

DATA = parse_raw()

DATA[1] = 12
DATA[2] = 2

def part_one():
    i = 0
    while True:
        if DATA[i] == 1:
            DATA[DATA[i + 3]] = DATA[DATA[i + 1]] + DATA[DATA[i + 2]]
        elif DATA[i] == 2:
            DATA[DATA[i + 3]] = DATA[DATA[i + 1]] * DATA[DATA[i + 2]]
        elif DATA[i] == 99:
            return DATA[0]
        i += 4

def part_two():
    ...

aoc_lube.submit(year=2019, day=2, part=1, solution=part_one)
aoc_lube.submit(year=2019, day=2, part=2, solution=part_two)
