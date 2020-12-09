from day_9_1 import XMAS

def weakness(filename, n):
    with open(filename) as file:
        codeList = file.read().replace("\r", "").strip().split("\n")
    
    roll = []

    for num in codeList:
        if(int(num) == n):
            roll = []
            continue
        roll.append(int(num))
        if(sum(roll) == n):
            return max(roll), min(roll)
        while(sum(roll) > n):
            roll.pop(0)
        if(sum(roll) == n):
            return max(roll), min(roll)
    print(roll)
    return 0

def main(filename = "input.txt"):
    a = XMAS(filename)
    b = weakness(filename, a)
    print(sum(b))

if __name__ == "__main__":
    main()