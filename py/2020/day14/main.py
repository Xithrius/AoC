from collections import defaultdict

with open("./input.txt") as f:
    text = [x.strip() for x in f.readlines()]


def main0():
    memory = defaultdict(int)
    for instruction in text:
        print(instruction)


def main1():
    ...


print(main0())
print(main1())
