from pathlib import Path

with open(Path.cwd() / 'input.txt', 'r', encoding='utf-8') as f:
    lst = [int(x.strip()) for x in f.readlines()]

fuel = 0
for mass in lst:
    while True:
        mass = int(mass / 3) - 2

        if mass > 0:
            fuel += mass
        else:
            break

print(fuel)
