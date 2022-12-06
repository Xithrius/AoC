import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=6)
print(RAW)

def parse_raw():
    return list(RAW.strip())

DATA = parse_raw()

def part_one():
    for i in range(0, len(DATA) - 4):
        element = DATA[i:i+4]
        if (len(set(element)) == 4):
            return i + 4

def part_two():
    for i in range(0, len(DATA) - 14):
        element = DATA[i:i+14]
        if (len(set(element)) == 14):
            return i + 14

aoc_lube.submit(year=2022, day=6, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=6, part=2, solution=part_two)
