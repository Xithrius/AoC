with open("./input.txt", "r", encoding="utf-8") as f:
    data = [x.split() for x in f.read().split("\n")]

score = 0
d = {
    'A': 1,
    'B': 2,
    'C': 3,
}
for item in data:
    if len(item) == 0:
        continue
    (l, r) = item
    (a, b) = l, chr(ord(r) - 23)
    if (a > b):
        
    # if (ord_b > ord_a):
    #     score += d[b] + 6
    # elif (ord_b < ord_a):
    #     score += d[b]
    # else:
    #     score += d[b] + 3
print(score)
