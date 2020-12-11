def jolt(filename):
    with open(filename) as file:
        joltList = [int(x) for x in file.read().replace("\r", "").strip().split("\n")]

    joltList = sorted(joltList)
    diffList = len(joltList) * [0]

    diffList[0] = joltList[0]
    for i in range(1, len(joltList)):
        diffList[i] = joltList[i] - joltList[i-1]

    return (diffList.count(3)+1) * diffList.count(1)

def main(filename = "input.txt"):
    a = jolt(filename)
    print(a)

if __name__ == "__main__":
    main()