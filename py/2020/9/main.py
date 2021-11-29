from itertools import permutations

with open("./input.txt") as f:
    text = [int(x) for x in f.readlines()]


def main0():
    for i in range(24, len(text)):
        integer = text[i + 1]
        summed = False
        for pair in permutations(text[i - 24 : i + 1], 2):
            if sum(pair) == integer and pair[0] != pair[1]:
                summed = True
        if not summed:
            return integer, i


def main1(flawed_integer, index_of_integer):
    for length in range(2, index_of_integer):
        lst2d = [text[i : i + length] for i in range(index_of_integer - length)]
        for lst in lst2d:
            if sum(lst) == flawed_integer:
                return min(lst) + max(lst)


flawed_integer, index = main0()
print(flawed_integer)
print(main1(flawed_integer, index))
