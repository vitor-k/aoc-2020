
def docking(filename):
    with open(filename) as file:
        lines = file.read().replace("\r", "").strip().split("\n")

    aMask = (1 << 36) - 1
    oMask = 0
    memory = {}

    for line in lines:
        if(line[0:4] == "mask"):
            aMask = int(line[7:].replace('X', '1'), 2)
            oMask = int(line[7:].replace('X', '0'), 2)
        else:
            address = int(line.split(']')[0][4:])
            value = int(line.split(" = ")[1])
            value = (value & aMask) | oMask
            memory[address] = value
    summy = 0
    for key in memory:
        summy += memory[key]
    return summy

def main(filename = "input.txt"):
    a = docking(filename)
    print(a)

if __name__ == "__main__":
    main()