import math

def navigation(filename):
    with open(filename) as file:
        actions = file.read().replace("\r", "").strip().split("\n")

    x = 0
    y = 0

    wax = 10
    way = 1

    for line in actions:
        if(line[0] == 'N'):
            way += int(line[1:])
        elif(line[0] == 'S'):
            way -= int(line[1:])
        elif(line[0] == 'E'):
            wax += int(line[1:])
        elif(line[0] == 'W'):
            wax -= int(line[1:])
        elif(line[0] == 'L'):
            r = abs(complex(wax, way))
            phi = math.atan2(way,wax)
            phi += math.radians(int(line[1:]))
            wax = r*math.cos(phi)
            way = r*math.sin(phi)
        elif(line[0] == 'R'):
            r = abs(complex(wax, way))
            phi = math.atan2(way,wax)
            phi -= math.radians(int(line[1:]))
            wax = r*math.cos(phi)
            way = r*math.sin(phi)
        elif(line[0] == 'F'):
            units = int(line[1:])
            x += units * wax
            y += units * way
    
    return abs(x)+abs(y)

def main(filename = "input.txt"):
    a = navigation(filename)
    print(a)

if __name__ == "__main__":
    main()