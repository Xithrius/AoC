with open("./input.txt") as f:
    lst = list(map(int, f.read().strip().split(",")))

lst[1] = 12
lst[2] = 2


def main0():
    i = 0
    while True:
        if lst[i] == 1:
            lst[lst[i + 3]] = lst[lst[i + 1]] + lst[lst[i + 2]]
        elif lst[i] == 2:
            lst[lst[i + 3]] = lst[lst[i + 1]] * lst[lst[i + 2]]
        elif lst[i] == 99:
            return lst[0]

        i += 4


def main1():
    ...


print(main0())
print(main1())
