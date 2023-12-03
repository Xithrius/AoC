import re
import aoc_lube


RAW = aoc_lube.fetch(year=2023, day=3)


def parse_raw():
    return [x for x in RAW.split("\n")]


DATA = parse_raw()


def part_one():
    lst = [a for a in DATA]
    check = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    numbers = []
    final = 0

    for i, y in enumerate(lst):
        for m in re.finditer(r"(\d+)", y):
            numbers.append((i, m.start(), m.end()))

    for y, x0, x1 in numbers:
        checked = []
        integer = int(lst[y][x0:x1])
        for a, b in check:
            for i in range(x0, x1):
                if (y + a < 0) or (i + b < 0):
                    continue
                try:
                    c = lst[y + a][i + b]
                    if c != "." and not c.isdigit():
                        point = (y + a, i + b)
                        if point not in checked:
                            checked.append(point)
                except IndexError:
                    continue
        if len(checked):
            final += integer

    return final


def part_two():
    lst = [a for a in DATA]
    check = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    numbers = []
    final = 0

    for i, y in enumerate(lst):
        for m in re.finditer(r"(\d+)", y):
            numbers.append((i, m.start(), m.end()))

    for i, y in enumerate(lst):
        for j, x in enumerate(y):
            if x == "*":
                checked = []
                for a, b in check:
                    cy, cx = i + a, j + b
                    if (cy < 0) or (cx < 0):
                        continue
                    for number in numbers:
                        y0, x0, x1 = number
                        if cy == y0 and cx in range(x0, x1):
                            checked.append(number)

                checked = set(checked)
                if len(checked) == 2:
                    c0, c1 = checked
                    c0y, c0x0, c0x1 = c0
                    c1y, c1x0, c1x1 = c1
                    i0, i1 = int(lst[c0y][c0x0:c0x1]), int(lst[c1y][c1x0:c1x1])
                    final += i0 * i1

    return final


aoc_lube.submit(year=2023, day=3, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=3, part=2, solution=part_two)
