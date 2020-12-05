def checkPass(filename):
    highest = 0
    with open(filename) as file:
        passlist = file.read().split()
    
    # B is 1, F is 0
    # R is 1, L is 0
    for line in passlist:
        line = line.strip()
        row = line[:7].replace("B", "1").replace("F", "0")
        column = line[7:].replace("R", "1").replace("L", "0")
        id = int(row+column, base=2)
        if(id > highest):
            highest = id
    return highest

def main(filename = "input.txt"):
    a = checkPass(filename)
    print(a)

if __name__ == "__main__":
    main()