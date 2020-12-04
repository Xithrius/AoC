from pathlib import Path

with open(Path.cwd() / "input.txt", "r", encoding="utf-8") as f:
    text = f.readlines()


def main0():
    valid = 0
    for r, char, password in [x.split() for x in text]:
        char = char[0]
        r = [int(x.strip()) for x in r.split("-")]
        low, high = r[0], r[1]
        count_in_pass = password.count(char)
        if count_in_pass >= low and count_in_pass <= high:
            valid += 1
    return valid


def main1():
    valid = 0
    for r, char, password in [x.split() for x in text]:
        char = char[0]
        r = [int(x.strip()) - 1 for x in r.split("-")]
        i1, i2 = r[0], r[1]
        if password[i1] == char or password[i2] == char:
            if password[i1] == char and password[i2] == char:
                pass
            else:
                valid += 1
    return valid


if __name__ == "__main__":
    # print(main0())
    print(main1())
