import math

def navigation(filename):
    with open(filename) as file:
        actions = file.read().replace("\r", "").strip().split("\n")

    direction = 0 #east
    x = 0
    y = 0

    for line in actions:
        if(line[0] == 'N'):
            y += int(line[1:])
        elif(line[0] == 'S'):
            y -= int(line[1:])
        elif(line[0] == 'E'):
            x += int(line[1:])
        elif(line[0] == 'W'):
            x -= int(line[1:])
        elif(line[0] == 'L'):
            direction += int(line[1:])
        elif(line[0] == 'R'):
            direction -= int(line[1:])
        elif(line[0] == 'F'):
            units = int(line[1:])
            x += units * math.cos(2*math.pi*direction/360)
            y += units * math.sin(math.tau*direction/360)

    return abs(x)+abs(y)

def main(filename = "input.txt"):
    a = navigation(filename)
    print(a)

if __name__ == "__main__":
    main()