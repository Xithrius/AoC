from collections import defaultdict
from threading import Thread

with open('./input.txt', 'r', encoding='utf-8') as f:
    text = list(f.read().strip())


def main0():
    locations = defaultdict(int)
    pos = [0, 0]

    for instruction in text:
        locations[f'{pos}'] += 1
        if instruction == '^':
            pos[1] += 1
        elif instruction == 'v':
            pos[1] -= 1
        elif instruction == '>':
            pos[0] += 1
        elif instruction == '<':
            pos[0] -= 1

    return len([i for i in locations.values() if i >= 1])

def main1():
    locations = defaultdict(int)
    pos, robo_pos = [0, 0], [0, 0]
    d = {
        '^': lambda x, y: [x, y + 1],
        'v': lambda x, y: [x, y - 1],
        '>': lambda x, y: [x + 1, y],
        '<': lambda x, y: [x - 1, y]
    }

    for i, j in zip(text[0::2], text[0:len(text) - 1:2]):
        locations[f'{pos}'] += 1
        locations[f'{robo_pos}'] += 1

        pos = [*d[i](*pos)]
        robo_pos = [*d[j](*robo_pos)]

    return len([i for i in locations.values() if i >= 1])

print(main0())
print(main1())

# 2357
# 3457
# 3051
# 6126