from collections import Counter

with open("./input.txt") as f:
    text = f.read().split("\n\n")


def main0():
    return sum(map(len, [set("".join(x.split())) for x in text]))


def main1():
    return sum(
        sum(v == len(i.split("\n")) for v in Counter(i).values())
        for i in [j.strip() for j in text]
    )


print(main0())
print(main1())
