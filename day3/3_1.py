def main():
    filename = "input.txt"
    trees = 0
    x = 0
    y = 0
    dx = 3
    dy = 1
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if(y and y % dy == 0):
                x += dx
                if(line[x%len(line)] == '#'):
                    trees += 1
            y += 1
    print(trees)

if __name__ == "__main__":
    main()