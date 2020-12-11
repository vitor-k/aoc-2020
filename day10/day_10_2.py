cache = []

def recCount(joltList, i=0):
    if(cache[i] != 0):
        pass #return cache[i]
    elif(i >= len(joltList) - 2):
        cache[i] = 1
    elif(joltList[i+1] - joltList[i] == 3 or joltList[i+2] - joltList[i] > 3):
        cache[i] = recCount(joltList, i+1)
    elif(i >= len(joltList) - 3 or joltList[i+3] - joltList[i] > 3):
        cache[i] = recCount(joltList, i+1) + recCount(joltList, i+2)
    else:
        cache[i] = recCount(joltList, i+1) + recCount(joltList, i+2) + recCount(joltList, i+3)
    return cache[i]


def jolt(filename):
    with open(filename) as file:
        joltList = [int(x) for x in file.read().replace("\r", "").strip().split("\n")]

    device = max(joltList) + 3

    joltList = sorted(joltList)
    joltList.append(device)
    joltList.insert(0,0)

    global cache
    cache = (len(joltList)) * [0]

    return recCount(joltList)

def main(filename = "input.txt"):
    a = jolt(filename)
    print(a)

if __name__ == "__main__":
    main()