from functools import reduce
import numpy as np
import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=8)
# RAW = '''\
# 30373
# 25512
# 65332
# 33549
# 35390
# '''

def parse_raw():
    return [[int(y) for y in x] for x in RAW.splitlines()]

DATA = np.array(parse_raw())

def part_one():
    vis = 0
    s = DATA.shape
    y, x = s

    for i in range(y):
        for j in range(x):
            if i == 0 or j == 0 or i == y - 1 or j == x - 1:
                vis += 1
                continue
            n = DATA[i, j]
            row = DATA[i]
            col = DATA[:, j]
            if n > max(row[:j]) or n > max(row[j + 1:]) or n > max(col[:i]) or n > max(col[i + 1:]):
                vis += 1

    return vis

def score(tree: int, lst: list[int]) -> int:
    if len(lst) == 0:
        return 0
    vis = 0
    for t in lst:
        if tree > t:
            vis += 1
        elif tree <= t:
            vis += 1
            break

    return vis

def part_two():
    m_vis = 0
    s = DATA.shape
    y, x = s

    for i in range(y):
        for j in range(x):
            n = DATA[i, j]
            row = DATA[i]
            col = DATA[:, j]
            vis_lst = [row[:j][::-1], row[j + 1:], col[:i][::-1], col[i + 1:]]
            score_lst = [score(n, k) for k in vis_lst]
            vis = reduce(lambda x, y: x * y, score_lst)

            if vis > m_vis:
                m_vis = vis

    return m_vis

aoc_lube.submit(year=2022, day=8, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=8, part=2, solution=part_two)
