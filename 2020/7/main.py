with open("./input.txt") as f:
    text = [x.strip()[:-1] for x in f.readlines()]


def main0():
    t = [x.split("bags contain") for x in text]
    d = {}


print(main0())
