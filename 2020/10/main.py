import numpy as np

with open("./input.txt") as f:
    t = sorted(int(x) for x in f.readlines())


def main0():
    lst = np.diff(t, prepend=0)
    return sum(lst == 1) * (sum(lst == 3) + 1)


def main1():
    lst = [0, *t, t[-1] + 3]
    diff = np.diff(lst)

    combinations = 1


print(main0())
print(main1())
