def checkSlope(mountain, dx, dy):
    trees = 0
    x = 0
    y = 0
    for line in mountain:
        line = line.rstrip()
        if(y and y % dy == 0):
            x += dx
            if(line[x%len(line)] == '#'):
                trees += 1
        y += 1
    return trees

def main(filename = "input.txt"):
    with open(filename) as file:
        mountain = list(file)
    
    a = checkSlope(mountain, 1,1)
    print(a)
    b = checkSlope(mountain, 3,1)
    print(b)
    c = checkSlope(mountain, 5,1)
    print(c)
    d = checkSlope(mountain, 7,1)
    print(d)
    e = checkSlope(mountain, 1,2)
    print(e)
    print(a*b*c*d*e)

if __name__ == "__main__":
    main()