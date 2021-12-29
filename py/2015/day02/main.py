import numpy as np

with open("./input.txt", "r", encoding="utf-8") as f:
    text = [list(map(int, x.split("x"))) for x in f.readlines()]


def main0():
    lst = [[x[0] * x[1], x[1] * x[2], x[0] * x[2]] * 2 for x in text]
    return sum(sum(x) + min(x) for x in lst)


def main1():
    return sum((np.prod(j) + ((j[0] + j[1]) * 2)) for j in [sorted(i) for i in text])

print(main0())
print(main1())
