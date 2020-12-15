
def docking(filename):
    with open(filename) as file:
        lines = file.read().replace("\r", "").strip().split("\n")

    oMask = 0
    xMask = ""
    memory = {}

    for line in lines:
        if(line[0:4] == "mask"):
            oMask = int(line[7:].replace('X', '0'), 2)
            eMask = int(line[7:].replace('0', '1').replace('X', '0'), 2)
            xMask = line[7:]
        else:
            address = line.split(']')[0][4:]
            value = int(line.split(" = ")[1])

            address = int(address) | oMask
            
            xs = 0
            tmpAddress = address
            memory[tmpAddress] = value
            xs = xMask.count('X')
            for j in range(2**xs):
                tmpAddress = address & eMask
                exes = 0
                for k in reversed(range(36)):
                    if(xMask[k] == 'X'):
                        tmpAddress = tmpAddress | (((j >> exes) & 1) << (35-k))
                        exes += 1
                memory[tmpAddress] = value
                    
    summy = 0
    for key in memory:
        summy += memory[key]
    return summy

def main(filename = "input.txt"):
    a = docking(filename)
    print(a)

if __name__ == "__main__":
    main()