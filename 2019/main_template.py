from pathlib import Path
import sys

try:
    lst = sys.argv[1:]

except IndexError:
    with open(Path.cwd() / "input.txt", "r", encoding="utf-8") as f:
        lst = [x for x in f.readlines()]
