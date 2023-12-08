import aoc_lube

RAW = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
RAW = aoc_lube.fetch(year=2023, day=8)


def parse_raw():
    lst = [x for x in RAW.split("\n")]

    return lst


DATA = parse_raw()


def part_one():
    steps, nodes = DATA[0], {y[0]: y[1][1:-1].split(", ") for y in [x.split(" = ") for x in DATA[2:-1]]}

    print(steps, nodes)

    current_node = "AAA"
    i = 0
    while current_node != "ZZZ":
        step = steps[i % len(steps)]
        current_node = nodes[current_node][0 if step == "L" else 1]

        i += 1

    return i


# def part_two():
#     steps, nodes = list(DATA[0]), {y[0]: y[1][1:-1].split(", ") for y in [x.split(" = ") for x in DATA[2:]]}

#     current_nodes = [x for x in nodes.keys() if x[-1] == "A"]

#     i = 0
#     total = 0

#     while any([x[-1] != "Z" for x in current_nodes]):
#         step = steps[i % len(steps)]
#         for j, node in enumerate(current_nodes):
#             current_nodes[j] = nodes[node][0 if step == "L" else 1]

#         i += 1
#         total += 1

#     return total

def part_two():
    steps, nodes = list(DATA[0]), {y[0]: y[1][1:-1].split(", ") for y in [x.split(" = ") for x in DATA[2:]]}

    current_nodes = [x for x in nodes.keys() if x[-1] == "A"]
    cycles = [[-1, -1]] * len(current_nodes)

    i = 0
    total = 0

    while any([x[-1] != "Z" for x in current_nodes]):
        step = steps[i % len(steps)]

        for k, (start, _ )in enumerate(cycles):
            if start != -1:
                cycles[k][1] += start
            # total += start

        for j, node in enumerate(current_nodes):
            if current_nodes[j][-1] != "Z":
                current_nodes[j] = nodes[node][0 if step == "L" else 1]
            elif cycles[j][0] == -1:
                    cycles[j][0] = i
                    cycles[j][1] = 0

        i += 1

        if not all(x[0] != -1 for x in cycles):
            total += 1

    return sum([x[0] for x in cycles]) + total


# print(part_one())
# aoc_lube.submit(year=2023, day=8, part=1, solution=part_one)

# print(part_two())
aoc_lube.submit(year=2023, day=8, part=2, solution=part_two)
