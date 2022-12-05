import aoc_lube

RAW = aoc_lube.fetch(year=2015, day=1)
print(RAW)

def parse_raw():
    return list(RAW)

DATA = parse_raw()

def part_one():
    return DATA.count('(') - DATA.count(')')

def part_two():
    count = 0
    for i, item in enumerate(DATA):
        if count == -1:
            return i
        if item == '(':
            count += 1
        else:
            count -= 1

aoc_lube.submit(year=2015, day=1, part=1, solution=part_one)
aoc_lube.submit(year=2015, day=1, part=2, solution=part_two)
