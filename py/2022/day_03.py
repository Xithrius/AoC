import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=3)
print(RAW)

def parse_raw():
    return [x for x in RAW.split('\n')]

DATA = parse_raw()

def part_one():
    total = 0
    for item in DATA:
        if len(item) == 0:
            continue
        half = len(item) // 2
        x = list(set(item[:half]).intersection(set(item[half:])))[0]
        if x.islower():
            total += ord(x) - 96
        else:
            total += ord(x) - 38
    return total

def part_two():
    total = 0
    for i in range(0, len(DATA), 3):
        elements = [set(y) for y in DATA[i:i + 3]]
        a, b, c = elements
        x = list(a & b & c)[0]
        if x.islower():
            total += ord(x) - 96
        else:
            total += ord(x) - 38
    return total

aoc_lube.submit(year=2022, day=3, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=3, part=2, solution=part_two)
