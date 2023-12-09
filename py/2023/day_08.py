import aoc_lube
import numpy as np


RAW = aoc_lube.fetch(year=2023, day=8)


def parse_raw():
    lst = [x for x in RAW.split("\n")]

    return lst


DATA = parse_raw()


def part_one():
    steps, nodes = (
        DATA[0],
        {y[0]: y[1][1:-1].split(", ") for y in [x.split(" = ") for x in DATA[2:-1]]},
    )

    current_node = "AAA"
    i = 0
    while current_node != "ZZZ":
        step = steps[i % len(steps)]
        current_node = nodes[current_node][0 if step == "L" else 1]

        i += 1

    return i


def part_two():
    steps, nodes = (
        list(DATA[0]),
        {y[0]: y[1][1:-1].split(", ") for y in [x.split(" = ") for x in DATA[2:]]},
    )

    current_nodes = [x for x in nodes.keys() if x[-1] == "A"]
    cycles = [0] * len(current_nodes)

    i = 0

    while any([x[-1] != "Z" for x in current_nodes]):
        step = steps[i % len(steps)]
        for j, node in enumerate(current_nodes):
            if not current_nodes[j].endswith("Z"):
                current_nodes[j] = nodes[node][0 if step == "L" else 1]
                cycles[j] += 1
        i += 1

    return np.lcm.reduce(cycles)


aoc_lube.submit(year=2023, day=8, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=8, part=2, solution=part_two)
