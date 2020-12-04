import re

with open("./input.txt", "r", encoding="utf-8") as f:
    text = f.read().split("\n\n")


def main0():
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid = sum(all(field in items for field in fields) for items in text)

    return valid


def main1():
    field_rules = {
        "byr": lambda x: int(x) in range(1920, 2003),
        "iyr": lambda x: int(x) in range(2010, 2021),
        "eyr": lambda x: int(x) in range(2020, 2031),
        "hgt": lambda x: int(x[:-2])
        in (range(150, 194) if x[-2:] == "cm" else range(59, 77)),
        "hcl": lambda x: bool(re.fullmatch(r"^#[0-9a-f]{6}$", x)),
        "ecl": lambda x: ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].count(x)
        == 1,
        "pid": lambda x: bool(re.fullmatch(r"^[0-9]{9}$", x)),
    }
    lst = [dict(y.strip().split(":") for y in x.strip().split()) for x in text]
    valid = 0
    for items in lst:
        try:
            if all([rule(items[field]) for field, rule in field_rules.items()]):
                valid += 1
        except (ValueError, KeyError):
            continue

    return valid


print(main0())
print(main1())
