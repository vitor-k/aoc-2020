import math

def busses(filename):
    with open(filename) as file:
        lines = file.read().replace("\r", "").strip().split("\n")

    et = int(lines[0])
    times = [int(x) for x in lines[1].split(",") if x != 'x']

    ebus = 0
    earliest = max(times)
    for time in times:
        if(et%time == 0 or time - (et % time) < earliest):
            earliest = time - (et % time) if et%time else 0
            ebus = time
    
    return ebus * earliest

def main(filename = "input.txt"):
    a = busses(filename)
    print(a)

if __name__ == "__main__":
    main()