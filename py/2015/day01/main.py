with open('./input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def main0():
    return sum(1 if x == '(' else -1 for x in text)


def main1():
    position = 0
    for index, move in enumerate(text):
        if move == '(':
            position += 1
        else:
            position -= 1
        if position < 0:
            return index + 1

print(main0())
print(main1())