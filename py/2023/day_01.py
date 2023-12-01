import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=1)

def parse_raw():
    return [list(x) for x in RAW.split('\n')]

DATA = parse_raw()
print(DATA)

def part_one():
    outer = 0
    for x in DATA:
        inner = []
        for j in x:
            if j.isdigit():
                inner.append(j)
        outer += int(inner[0] + inner[-1])

    return outer


digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def part_two():
    d: str = ["".join(a) for a in DATA]
    outer = 0
    for a in d:
        inner = []
        for i, b in enumerate(a):
            if b.isdigit():
                inner.append((i, b))
        for digit in digits:
            for x in range(len(a) - len(digit) + 1):
                if a[x:x + len(digit)] == digit:
                    inner.append((x, str(digits.index(digit) + 1)))

        lst = list(sorted(inner, key=lambda z: z[0]))

        outer += int(f"{lst[0][1]}{lst[-1][1]}")

    return outer


aoc_lube.submit(year=2023, day=1, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=1, part=2, solution=part_two)
