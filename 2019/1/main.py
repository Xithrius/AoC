from pathlib import Path

with open(Path.cwd() / 'input.txt', 'r') as f:
    lst = [int(x.strip()) for x in f.readlines()]

#fuel = []
#for mass in lst:
#    tmp = (int(mass / 3) - 2)
fuel = sum([int(mass / 3) - 2 for mass in lst])
print(fuel)
