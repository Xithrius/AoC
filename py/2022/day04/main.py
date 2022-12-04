with open("./input.txt", "r", encoding="utf-8") as f:
    data = [x for x in f.read().split("\n")]

total = 0
something = 0
for item in data:
    element = item.split(",")
    if len(element) != 2:
        continue
    a, b = element
    l = lambda w: [int(i) for i in w.split("-")]
    x, y = l(a), l(b)
    i, j = set(range(x[0], x[1] + 1)), set(range(y[0], y[1] + 1))
    z = i.intersection(j)
    if (z == i or z == j):
        total += 1
    if len(z) > 0:
        something += 1
print(total)
print(something)
