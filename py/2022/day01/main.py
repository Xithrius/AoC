with open("./input.txt", "r", encoding="utf-8") as f:
    data = [x for x in f.read().split("\n\n")]

x = [sum(int(y) for y in x.split("\n")) for x in data[:-1]]
print(max(x))
print(sum(sorted(x)[-3:]))
