with open("./input.txt", "r", encoding="utf-8") as f:
    data = [list(x.strip()) for x in f.readlines()]

total = 0

for item in data:
    if len(item) == 0:
        continue
    half = len(item) // 2
    x = list(set(item[:half]).intersection(set(item[half:])))[0]
    if x.islower():
        total += ord(x) - 96
    else:
        total += ord(x) - 38
print(total)


total = 0
for i in range(0, len(data), 3):
    elements = [set(y) for y in data[i:i + 3]]
    a, b, c = elements
    x = list(a & b & c)[0]
    if x.islower():
        total += ord(x) - 96
    else:
        total += ord(x) - 38
print(total)
