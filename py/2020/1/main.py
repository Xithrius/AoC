from pathlib import Path
from itertools import combinations

with open(Path.cwd() / "input.txt") as f:
    integers = [int(x) for x in f.readlines()]

for i, j, k in combinations(integers, 3):
    if i + j + k == 2020:
        print(i * j * k)
        break
