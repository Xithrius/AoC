with open("./input.txt") as f:
    text = [list(x.strip()) for x in f.readlines()]


def main0():
    h_len = len(text[0])

    trees = sum(l[(i * 3) % h_len] == "#" for i, l in enumerate(text))

    print(trees)


def main1():
    tree_total = 1
    h_len = len(text[0])

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for x, y in slopes:
        tree_total *= sum(
            text[i][((i // y) * x) % h_len] == "#" for i in range(0, len(text), y)
        )

    print(tree_total)


if __name__ == "__main__":
    main0()
    main1()
