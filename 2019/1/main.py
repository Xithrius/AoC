with open('./input.txt') as f:
    text = [int(x.strip()) for x in f.readlines()]

def main0():
    return sum((x // 3) - 2 for x in text)

def main1():
    total = 0
    for x in text:
        while x > 0:
            x = (x // 3) - 2
            if x > 0:
                total += x

    return total


print(main0())
print(main1())
