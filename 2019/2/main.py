from pathlib import Path
import sys


with open("input.txt", "r", encoding="utf-8") as f:
    lst = [int(x) for x in f.read().strip().split(",")]

lst[1] = 12
lst[2] = 2

index = 0
opcode = False

while True:
    integer = lst[index]

    if integer == 99:
        break
    elif integer == 1:
        opcode = True
        lst[lst[index + 3]] = lst[lst[index + 1]] + lst[lst[index + 2]]
    elif integer == 2:
        opcode == True
        lst[lst[index + 3]] = lst[lst[index + 1]] * lst[lst[index + 2]]

    if opcode:
        index += 4
    else:
        index += 1


print(lst[0])
