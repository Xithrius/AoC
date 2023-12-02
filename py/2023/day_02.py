import aoc_lube
import itertools

RAW = aoc_lube.fetch(year=2023, day=2)


def parse_raw():
    return [x for x in RAW.split("\n")]


DATA = parse_raw()


def part_one():
    check = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    ids = 0

    for line in DATA:
        id = int(line.split(":")[0].split()[-1])
        bags = list(
            map(
                lambda z: [int(z[0]), z[1]],
                [
                    x.strip().split()
                    for x in itertools.chain(
                        *[j.split(", ") for j in line.split(":")[1].split(";")]
                    )
                ],
            )
        )

        valid = True

        for bag in bags:
            amount, color = bag
            if amount > check[color]:
                valid = False
                break

        if valid:
            ids += id

    return ids


def part_two():
    total = 0
    for line in DATA:
        bags = list(
            map(
                lambda z: [int(z[0]), z[1]],
                [
                    x.strip().split()
                    for x in itertools.chain(
                        *[j.split(", ") for j in line.split(":")[1].split(";")]
                    )
                ],
            )
        )

        out = 1

        for c in ["red", "blue", "green"]:
            out *= max([amount for amount, color in bags if color == c])

        total += out

    return total


aoc_lube.submit(year=2023, day=2, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=2, part=2, solution=part_two)
