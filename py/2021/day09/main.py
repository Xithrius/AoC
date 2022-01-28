def main():
    lines = [[int(y) for y in x.strip()] for x in open('./input.txt').readlines()]

    print(lines)

if __name__ == '__main__':
    main()

