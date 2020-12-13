import math

def busses(filename):
    with open(filename) as file:
        lines = file.read().replace("\r", "").strip().split("\n")

    times = lines[1].split(",")

    requirements = [(int(times[i]), i) for i in range(len(times)) if times[i] != 'x']

    a = 0
    nullObject = 1
    for pack in requirements:
        n, k = pack
        while((a+k) % n != 0 or a == 0):
            a += nullObject
        nullObject *= n
        
    return a

def main(filename = "input.txt"):
    a = busses(filename)
    print(a)

if __name__ == "__main__":
    main()