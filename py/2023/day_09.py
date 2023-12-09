import aoc_lube


RAW = aoc_lube.fetch(year=2023, day=9)


def parse_raw():
    lst = [[int(y) for y in x.split()] for x in RAW.split("\n")]

    return lst


DATA = parse_raw()


def part_one():
    total = 0

    for ns in DATA:
        inner = [ns]
        index = 0
        while any(x != 0 for x in inner[index]):
            c = [
                inner[index][i + 1] - inner[index][i]
                for i in range(len(inner[index]) - 1)
            ]
            inner.append(c)
            index += 1
        inner[-1].append(0)

        for i in range(len(inner) - 1):
            inner[-i - 2].append(inner[-i - 1][-1] + inner[-i - 2][-1])

        total += inner[0][-1]

    return total


def part_two():
    total = 0

    for ns in DATA:
        inner = [ns]
        index = 0
        while any(x != 0 for x in inner[index]):
            c = [
                inner[index][i + 1] - inner[index][i]
                for i in range(len(inner[index]) - 1)
            ]
            inner.append(c)
            index += 1
        inner[-1].insert(0, 0)

        for i in range(len(inner) - 1):
            inner[-i - 2].insert(0, inner[-i - 2][0] - inner[-i - 1][0])

        total += inner[0][0]

    return total


aoc_lube.submit(year=2023, day=9, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=9, part=2, solution=part_two)
