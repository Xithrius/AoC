import numpy as np
import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=5)

RAW_STACKS = RAW.split('\n\n')[0]
RAW_MOVES = RAW.split('\n\n')[1]

STACKS = [list(x[1::2][::2]) for x in RAW_STACKS.split('\n')][:-1]
STACKS[0] = list(' ' * 3) + STACKS[0]
STACKS = np.array(STACKS)
STACKS = np.transpose(STACKS)
STACKS = np.array([np.delete(x, np.where(x == ' ')) for x in STACKS])

MOVES = [[int(y) for y in x.split()[1::2]] for x in RAW_MOVES.split('\n')]

def part_one():
    for (amount, start, end) in MOVES:
        to_move = STACKS[start - 1][:amount]
        STACKS[start - 1] = np.delete(STACKS[start - 1], np.s_[:amount])
        STACKS[end - 1] = np.insert(STACKS[end - 1], 0, np.flip(to_move), axis=0)
    return "".join(item[0] for item in STACKS)

def part_two():
    for (amount, start, end) in MOVES:
        to_move = STACKS[start - 1][:amount]
        STACKS[start - 1] = np.delete(STACKS[start - 1], np.s_[:amount])
        STACKS[end - 1] = np.insert(STACKS[end - 1], 0, to_move, axis=0)
    return "".join(item[0] for item in STACKS)

aoc_lube.submit(year=2022, day=5, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=5, part=2, solution=part_two)
