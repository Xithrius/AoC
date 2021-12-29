with open("input.txt") as f:
    text = [x.strip() for x in f.readlines()]


def main0():
    lst = [
        [value[0], int(value[1][1:]) * (-1 if value[1][0] == "-" else 1)]
        for index, value in enumerate([x.split() for x in text])
    ]
    indexes_hit = set()
    index = 0
    acc = 0
    while True:
        if index in indexes_hit:
            return acc
        else:
            indexes_hit.add(index)
        instruction, integer = lst[index][0], lst[index][1]
        if instruction == "acc":
            acc += integer
            index += 1
        elif instruction == "jmp":
            index += integer
        else:
            if index == len(lst) - 1:
                return acc
            index += 1


def main1():
    ...


print(main0())
print(main1())
